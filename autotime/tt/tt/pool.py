import sqlite3
from pathlib import Path
import os
import time

def ConnectionPool():
    """Return a (connection, cursor) tuple using SQLite only."""
    # Look for db.sqlite3 in the project root (parent of the tt directory)
    db_file = Path(__file__).resolve().parent.parent / 'db.sqlite3'
    
    if not db_file.exists():
        raise Exception(f"Database file not found at {db_file}")
    
    # Add timeout to prevent locking issues
    conn = sqlite3.connect(str(db_file), check_same_thread=False, timeout=20)
    
    # Enable WAL mode for better concurrency
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA synchronous=NORMAL")
    
    # Wrap the SQLite cursor so SQL like `select * from timetable.Program`
    # works by removing the `timetable.` schema prefix automatically.
    class CursorWrapper:
        def __init__(self, conn):
            self._conn = conn
            self._cur = conn.cursor()

        def _fix_query(self, q):
            if isinstance(q, str):
                return q.replace('timetable.', '')
            return q

        def execute(self, q, params=None):
            max_retries = 3
            for attempt in range(max_retries):
                try:
                    q2 = self._fix_query(q)
                    if params is None:
                        return self._cur.execute(q2)
                    return self._cur.execute(q2, params)
                except sqlite3.OperationalError as e:
                    if "database is locked" in str(e) and attempt < max_retries - 1:
                        time.sleep(0.5)  # Wait 0.5 seconds before retry
                        continue
                    raise e

        def executemany(self, q, seq):
            q2 = self._fix_query(q)
            return self._cur.executemany(q2, seq)

        def fetchone(self):
            return self._cur.fetchone()

        def fetchall(self):
            return self._cur.fetchall()
        
        def close(self):
            try:
                self._cur.close()
            except Exception:
                pass
        
        # Add property to expose rowcount from underlying cursor
        @property
        def rowcount(self):
            """Return the number of rows affected by the last execute"""
            return self._cur.rowcount

    cur = CursorWrapper(conn)
    return (conn, cur)