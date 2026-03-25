import sqlite3
from sqlite3 import Error
import os
import random

def create_connection():
    """Create or open the SQLite database used by the Django app."""
    path = os.path.join(os.path.dirname(__file__), 'db.sqlite3')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    try:
        connection = sqlite3.connect(path)
        print("Connected to SQLite database at", path)
        return connection
    except Error as e:
        print(f"Error connecting to SQLite: {e}")
        return None

def insert_admin(connection):
    """Insert admin data"""
    cursor = connection.cursor()
    admin_data = [
        ('01', 'admin', 'admin@gmail.com', 'admin', 'admin')
    ]
    
    query = "INSERT INTO Admin (admin_id, name, email, username, password) VALUES (?, ?, ?, ?, ?)"
    cursor.executemany(query, admin_data)
    connection.commit()
    print(f"Inserted {cursor.rowcount} rows into Admin table")

def insert_program(connection):
    """Insert program data - ALL PROGRAMS with ALL SEMESTERS"""
    cursor = connection.cursor()
    program_data = []
    
    # Define all programs and their semesters
    programs_info = {
        'BTECH': 8,
        'BBA': 6,
        'BAJMC': 6,
        'BCA': 6,
        'BARCH': 8,
        'BSC-CS': 6,
        'BTECH-AIML': 8,
        'BTECH-AIDS': 8,
        'BTECH-CSE': 8
    }
    
    for program, max_semester in programs_info.items():
        for semester in range(1, max_semester + 1):
            program_data.append((program, str(semester)))
    
    query = "INSERT INTO Program (Program_name, semester_id) VALUES (?, ?)"
    cursor.executemany(query, program_data)
    connection.commit()
    print(f"Inserted {cursor.rowcount} rows into Program table")

def insert_courses(connection):
    """Insert courses data - COMPLETE DATA FOR ALL PROGRAMS"""
    cursor = connection.cursor()
    courses_data = []
    
    # ============ BTECH COURSES (All Semesters) ============
    btech_courses = [
        # Semester 1
        ('ECSE105-Lec', 'Computational Thinking and Programming', 3, 'BTECH', '1'),
        ('EMAT101-Lec', 'Engineering Calculus', 3, 'BTECH', '1'),
        ('EHSS103-Lec', 'New Age Life Skills', 2, 'BTECH', '1'),
        ('ECSE105-LAB', 'Computational Thinking Lab', 2, 'BTECH', '1'),
        ('EMAT101-LAB', 'Engineering Calculus Lab', 2, 'BTECH', '1'),
        ('EHSS103-LAB', 'Life Skills Lab', 1, 'BTECH', '1'),
        
        # Semester 2
        ('EECE105-Lec', 'Electrical & Electronics Engineering', 3, 'BTECH', '2'),
        ('CSET104-Lec', 'Object Oriented Programming using Java', 4, 'BTECH', '2'),
        ('CSET105-Lec', 'Digital Design', 3, 'BTECH', '2'),
        ('EECE105-LAB', 'Electrical & Electronics Lab', 2, 'BTECH', '2'),
        ('CSET104-LAB', 'Java Programming Lab', 2, 'BTECH', '2'),
        ('CSET105-LAB', 'Digital Design Lab', 2, 'BTECH', '2'),
        
        # Semester 3
        ('ECSE219-Lec', 'Statistical Machine Learning', 3, 'BTECH', '3'),
        ('ECSE215-Lec', 'Data Structures using C++', 4, 'BTECH', '3'),
        ('ECSE217-Lec', 'Microprocessors', 3, 'BTECH', '3'),
        ('ECSE219-LAB', 'Machine Learning Lab', 2, 'BTECH', '3'),
        ('ECSE215-LAB', 'Data Structures Lab', 2, 'BTECH', '3'),
        ('ECSE217-LAB', 'Microprocessors Lab', 2, 'BTECH', '3'),
        
        # Semester 4
        ('CSET301-Lec', 'Database Management Systems', 4, 'BTECH', '4'),
        ('CSET302-Lec', 'Operating Systems', 3, 'BTECH', '4'),
        ('CSET207-LAB', 'Computer Networks Lab', 2, 'BTECH', '4'),
        ('CSET210-LAB', 'Design Thinking Lab', 2, 'BTECH', '4'),
        
        # Semester 5
        ('CSET303-Lec', 'Software Engineering', 3, 'BTECH', '5'),
        ('CSET304-Lec', 'Web Technologies', 3, 'BTECH', '5'),
        ('CSET305-LAB', 'Web Development Lab', 2, 'BTECH', '5'),
        
        # Semester 6
        ('CSET306-Lec', 'Artificial Intelligence', 3, 'BTECH', '6'),
        ('CSET307-Lec', 'Compiler Design', 3, 'BTECH', '6'),
        ('CSET308-LAB', 'AI Lab', 2, 'BTECH', '6'),
        
        # Semester 7
        ('CSET309-Lec', 'Machine Learning', 3, 'BTECH', '7'),
        ('CSET310-Lec', 'Cloud Computing', 3, 'BTECH', '7'),
        ('CSET311-LAB', 'Cloud Computing Lab', 2, 'BTECH', '7'),
        
        # Semester 8
        ('CSET312-Lec', 'Big Data Analytics', 3, 'BTECH', '8'),
        ('CSET313-Lec', 'Cyber Security', 3, 'BTECH', '8'),
        ('CSET314-LAB', 'Project Work', 4, 'BTECH', '8'),
    ]
    courses_data.extend(btech_courses)
    
    # ============ BBA COURSES (All Semesters) ============
    bba_courses = [
        # Semester 1
        ('BBA101-Lec', 'Principles of Management', 3, 'BBA', '1'),
        ('BBA102-Lec', 'Business Economics', 3, 'BBA', '1'),
        ('BBA103-Lec', 'Financial Accounting', 3, 'BBA', '1'),
        ('BBA101-LAB', 'Management Skills Lab', 1, 'BBA', '1'),
        
        # Semester 2
        ('BBA104-Lec', 'Business Mathematics', 3, 'BBA', '2'),
        ('BBA105-Lec', 'Business Communication', 3, 'BBA', '2'),
        ('BBA106-Lec', 'Organizational Behavior', 3, 'BBA', '2'),
        ('BBA102-LAB', 'Communication Lab', 1, 'BBA', '2'),
        
        # Semester 3
        ('BBA201-Lec', 'Marketing Management', 3, 'BBA', '3'),
        ('BBA202-Lec', 'Human Resource Management', 3, 'BBA', '3'),
        ('BBA203-Lec', 'Business Statistics', 3, 'BBA', '3'),
        ('BBA201-LAB', 'Marketing Research Lab', 1, 'BBA', '3'),
        
        # Semester 4
        ('BBA204-Lec', 'Business Law', 3, 'BBA', '4'),
        ('BBA205-Lec', 'Financial Management', 3, 'BBA', '4'),
        ('BBA206-Lec', 'Operations Management', 3, 'BBA', '4'),
        ('BBA203-LAB', 'Business Analytics Lab', 1, 'BBA', '4'),
        
        # Semester 5
        ('BBA301-Lec', 'Entrepreneurship', 3, 'BBA', '5'),
        ('BBA302-Lec', 'Business Ethics', 3, 'BBA', '5'),
        ('BBA303-Lec', 'International Business', 3, 'BBA', '5'),
        ('BBA301-LAB', 'Business Plan Lab', 2, 'BBA', '5'),
        
        # Semester 6
        ('BBA304-Lec', 'Strategic Management', 3, 'BBA', '6'),
        ('BBA305-Lec', 'Consumer Behavior', 3, 'BBA', '6'),
        ('BBA306-Lec', 'Digital Marketing', 3, 'BBA', '6'),
        ('BBA302-LAB', 'Digital Marketing Lab', 2, 'BBA', '6'),
    ]
    courses_data.extend(bba_courses)
    
    # ============ BAJMC COURSES (All Semesters) ============
    bajmc_courses = [
        # Semester 1
        ('BJMC101-Lec', 'Introduction to Journalism', 3, 'BAJMC', '1'),
        ('BJMC102-Lec', 'Media Communication', 3, 'BAJMC', '1'),
        ('BJMC103-Lec', 'Writing for Media', 3, 'BAJMC', '1'),
        ('BJMC104-Lec', 'Media Ethics', 2, 'BAJMC', '1'),
        ('BJMC105-LAB', 'Media Lab', 2, 'BAJMC', '1'),
        
        # Semester 2
        ('BJMC201-Lec', 'Reporting & Editing', 3, 'BAJMC', '2'),
        ('BJMC202-Lec', 'Media Laws', 3, 'BAJMC', '2'),
        ('BJMC203-Lec', 'Photojournalism', 3, 'BAJMC', '2'),
        ('BJMC204-LAB', 'Photography Lab', 2, 'BAJMC', '2'),
        
        # Semester 3
        ('BJMC301-Lec', 'Broadcast Journalism', 3, 'BAJMC', '3'),
        ('BJMC302-Lec', 'Media Management', 3, 'BAJMC', '3'),
        ('BJMC303-Lec', 'Communication Research', 3, 'BAJMC', '3'),
        ('BJMC304-LAB', 'Video Production Lab', 2, 'BAJMC', '3'),
        
        # Semester 4
        ('BJMC401-Lec', 'Digital Media', 3, 'BAJMC', '4'),
        ('BJMC402-Lec', 'Public Relations', 3, 'BAJMC', '4'),
        ('BJMC403-Lec', 'Advertising', 3, 'BAJMC', '4'),
        ('BJMC404-LAB', 'Audio Production Lab', 2, 'BAJMC', '4'),
        
        # Semester 5
        ('BJMC501-Lec', 'Development Communication', 3, 'BAJMC', '5'),
        ('BJMC502-Lec', 'Media Criticism', 3, 'BAJMC', '5'),
        ('BJMC503-LAB', 'Multimedia Lab', 2, 'BAJMC', '5'),
        
        # Semester 6
        ('BJMC601-Lec', 'Media Research', 3, 'BAJMC', '6'),
        ('BJMC602-LAB', 'Portfolio Development', 4, 'BAJMC', '6'),
    ]
    courses_data.extend(bajmc_courses)
    
    # ============ BCA COURSES (All Semesters) ============
    bca_courses = [
        # Semester 1
        ('BCA101-Lec', 'Programming in C', 4, 'BCA', '1'),
        ('BCA102-Lec', 'Mathematics for Computing', 3, 'BCA', '1'),
        ('BCA103-Lec', 'Digital Electronics', 3, 'BCA', '1'),
        ('BCA101-LAB', 'C Programming Lab', 2, 'BCA', '1'),
        
        # Semester 2
        ('BCA104-Lec', 'Data Structures', 4, 'BCA', '2'),
        ('BCA105-Lec', 'Object Oriented Programming', 3, 'BCA', '2'),
        ('BCA102-LAB', 'Data Structures Lab', 2, 'BCA', '2'),
        
        # Semester 3
        ('BCA201-Lec', 'Database Management Systems', 3, 'BCA', '3'),
        ('BCA202-Lec', 'Operating Systems', 3, 'BCA', '3'),
        ('BCA203-Lec', 'Computer Networks', 3, 'BCA', '3'),
        ('BCA201-LAB', 'DBMS Lab', 2, 'BCA', '3'),
        
        # Semester 4
        ('BCA204-Lec', 'Web Technologies', 3, 'BCA', '4'),
        ('BCA205-Lec', 'Software Engineering', 3, 'BCA', '4'),
        ('BCA202-LAB', 'Web Development Lab', 2, 'BCA', '4'),
        
        # Semester 5
        ('BCA301-Lec', 'Java Programming', 4, 'BCA', '5'),
        ('BCA302-Lec', 'Python Programming', 3, 'BCA', '5'),
        ('BCA301-LAB', 'Java Lab', 2, 'BCA', '5'),
        
        # Semester 6
        ('BCA303-Lec', 'Artificial Intelligence', 3, 'BCA', '6'),
        ('BCA304-Lec', 'Cloud Computing', 3, 'BCA', '6'),
        ('BCA302-LAB', 'Project Work', 4, 'BCA', '6'),
    ]
    courses_data.extend(bca_courses)
    
    # ============ BARCH COURSES (All Semesters) ============
    barch_courses = [
        # Semester 1
        ('ARCH101-Lec', 'Architectural Design Basics', 4, 'BARCH', '1'),
        ('ARCH102-Lec', 'Building Materials', 3, 'BARCH', '1'),
        ('ARCH103-Lec', 'Architectural Drawing', 3, 'BARCH', '1'),
        ('ARCH104-Lec', 'History of Architecture', 3, 'BARCH', '1'),
        ('ARCH105-STD', 'Design Studio', 4, 'BARCH', '1'),
        
        # Semester 2
        ('ARCH201-Lec', 'Building Construction', 3, 'BARCH', '2'),
        ('ARCH202-Lec', 'Structural Systems', 3, 'BARCH', '2'),
        ('ARCH203-Lec', 'Climatology', 2, 'BARCH', '2'),
        ('ARCH204-STD', 'Studio II', 4, 'BARCH', '2'),
        
        # Semester 3
        ('ARCH301-Lec', 'Urban Design', 3, 'BARCH', '3'),
        ('ARCH302-Lec', 'Landscape Architecture', 3, 'BARCH', '3'),
        ('ARCH303-Lec', 'Working Drawing', 3, 'BARCH', '3'),
        ('ARCH304-STD', 'Studio III', 4, 'BARCH', '3'),
        
        # Semester 4
        ('ARCH401-Lec', 'Building Services', 3, 'BARCH', '4'),
        ('ARCH402-Lec', 'Estimation & Costing', 3, 'BARCH', '4'),
        ('ARCH403-Lec', 'Environmental Studies', 2, 'BARCH', '4'),
        ('ARCH404-STD', 'Studio IV', 4, 'BARCH', '4'),
        
        # Semester 5
        ('ARCH501-Lec', 'Housing', 3, 'BARCH', '5'),
        ('ARCH502-Lec', 'Building Economics', 3, 'BARCH', '5'),
        ('ARCH503-STD', 'Studio V', 4, 'BARCH', '5'),
        
        # Semester 6
        ('ARCH601-Lec', 'Urban Planning', 3, 'BARCH', '6'),
        ('ARCH602-Lec', 'Professional Practice', 3, 'BARCH', '6'),
        ('ARCH603-STD', 'Studio VI', 4, 'BARCH', '6'),
        
        # Semester 7
        ('ARCH701-Lec', 'Architectural Conservation', 3, 'BARCH', '7'),
        ('ARCH702-Lec', 'Research Methods', 2, 'BARCH', '7'),
        ('ARCH703-STD', 'Studio VII', 4, 'BARCH', '7'),
        
        # Semester 8
        ('ARCH801-THESIS', 'Architectural Thesis', 8, 'BARCH', '8'),
    ]
    courses_data.extend(barch_courses)
    
    # ============ BSC-CS COURSES (All Semesters) ============
    bsccs_courses = [
        # Semester 1
        ('BSCS101-Lec', 'Programming Fundamentals', 4, 'BSC-CS', '1'),
        ('BSCS102-Lec', 'Discrete Mathematics', 3, 'BSC-CS', '1'),
        ('BSCS103-Lec', 'Digital Logic', 3, 'BSC-CS', '1'),
        ('BSCS104-LAB', 'Programming Lab', 2, 'BSC-CS', '1'),
        
        # Semester 2
        ('BSCS201-Lec', 'Data Structures', 4, 'BSC-CS', '2'),
        ('BSCS202-Lec', 'Computer Organization', 3, 'BSC-CS', '2'),
        ('BSCS203-LAB', 'Data Structures Lab', 2, 'BSC-CS', '2'),
        
        # Semester 3
        ('BSCS301-Lec', 'Database Systems', 3, 'BSC-CS', '3'),
        ('BSCS302-Lec', 'Operating Systems', 3, 'BSC-CS', '3'),
        ('BSCS303-Lec', 'Computer Networks', 3, 'BSC-CS', '3'),
        ('BSCS304-LAB', 'DBMS Lab', 2, 'BSC-CS', '3'),
        
        # Semester 4
        ('BSCS401-Lec', 'Web Technologies', 3, 'BSC-CS', '4'),
        ('BSCS402-Lec', 'Software Engineering', 3, 'BSC-CS', '4'),
        ('BSCS403-LAB', 'Web Development Lab', 2, 'BSC-CS', '4'),
        
        # Semester 5
        ('BSCS501-Lec', 'Python Programming', 3, 'BSC-CS', '5'),
        ('BSCS502-Lec', 'Java Programming', 3, 'BSC-CS', '5'),
        ('BSCS503-LAB', 'Python Lab', 2, 'BSC-CS', '5'),
        
        # Semester 6
        ('BSCS601-Lec', 'Machine Learning', 3, 'BSC-CS', '6'),
        ('BSCS602-Lec', 'Cloud Computing', 3, 'BSC-CS', '6'),
        ('BSCS603-LAB', 'Project Work', 4, 'BSC-CS', '6'),
    ]
    courses_data.extend(bsccs_courses)
    
    # ============ BTECH-AIML COURSES (All Semesters) ============
    aiml_courses = [
        # Semester 1
        ('AIML101-Lec', 'Python for AI', 3, 'BTECH-AIML', '1'),
        ('AIML102-Lec', 'Linear Algebra', 3, 'BTECH-AIML', '1'),
        ('AIML103-Lec', 'Probability & Statistics', 3, 'BTECH-AIML', '1'),
        ('AIML104-LAB', 'Python Lab', 2, 'BTECH-AIML', '1'),
        
        # Semester 2
        ('AIML201-Lec', 'Data Structures', 3, 'BTECH-AIML', '2'),
        ('AIML202-Lec', 'Database Systems', 3, 'BTECH-AIML', '2'),
        ('AIML203-Lec', 'Discrete Mathematics', 3, 'BTECH-AIML', '2'),
        ('AIML204-LAB', 'Data Structures Lab', 2, 'BTECH-AIML', '2'),
        
        # Semester 3
        ('AIML301-Lec', 'Machine Learning Fundamentals', 4, 'BTECH-AIML', '3'),
        ('AIML302-Lec', 'Data Visualization', 3, 'BTECH-AIML', '3'),
        ('AIML303-LAB', 'ML Lab', 2, 'BTECH-AIML', '3'),
        
        # Semester 4
        ('AIML401-Lec', 'Deep Learning', 4, 'BTECH-AIML', '4'),
        ('AIML402-Lec', 'Natural Language Processing', 3, 'BTECH-AIML', '4'),
        ('AIML403-LAB', 'Deep Learning Lab', 2, 'BTECH-AIML', '4'),
        
        # Semester 5
        ('AIML501-Lec', 'Computer Vision', 3, 'BTECH-AIML', '5'),
        ('AIML502-Lec', 'Reinforcement Learning', 3, 'BTECH-AIML', '5'),
        ('AIML503-LAB', 'Computer Vision Lab', 2, 'BTECH-AIML', '5'),
        
        # Semester 6
        ('AIML601-Lec', 'Generative AI', 3, 'BTECH-AIML', '6'),
        ('AIML602-Lec', 'MLOps', 3, 'BTECH-AIML', '6'),
        ('AIML603-LAB', 'AI Project', 4, 'BTECH-AIML', '6'),
        
        # Semester 7
        ('AIML701-Lec', 'AI Ethics', 2, 'BTECH-AIML', '7'),
        ('AIML702-Lec', 'Big Data Analytics', 3, 'BTECH-AIML', '7'),
        ('AIML703-LAB', 'Industry Project', 4, 'BTECH-AIML', '7'),
        
        # Semester 8
        ('AIML801-THESIS', 'AI Research Thesis', 6, 'BTECH-AIML', '8'),
    ]
    courses_data.extend(aiml_courses)
    
    # ============ BTECH-AIDS COURSES (All Semesters) ============
    aids_courses = [
        # Semester 1
        ('AIDS101-Lec', 'Data Science Fundamentals', 3, 'BTECH-AIDS', '1'),
        ('AIDS102-Lec', 'Statistics for Data Science', 3, 'BTECH-AIDS', '1'),
        ('AIDS103-Lec', 'Python Programming', 3, 'BTECH-AIDS', '1'),
        ('AIDS104-LAB', 'Python Lab', 2, 'BTECH-AIDS', '1'),
        
        # Semester 2
        ('AIDS201-Lec', 'Data Structures', 3, 'BTECH-AIDS', '2'),
        ('AIDS202-Lec', 'Database Management', 3, 'BTECH-AIDS', '2'),
        ('AIDS203-Lec', 'Probability Theory', 3, 'BTECH-AIDS', '2'),
        ('AIDS204-LAB', 'Data Structures Lab', 2, 'BTECH-AIDS', '2'),
        
        # Semester 3
        ('AIDS301-Lec', 'Data Visualization', 3, 'BTECH-AIDS', '3'),
        ('AIDS302-Lec', 'Machine Learning', 4, 'BTECH-AIDS', '3'),
        ('AIDS303-LAB', 'ML Lab', 2, 'BTECH-AIDS', '3'),
        
        # Semester 4
        ('AIDS401-Lec', 'Big Data Analytics', 3, 'BTECH-AIDS', '4'),
        ('AIDS402-Lec', 'Statistical Analysis', 3, 'BTECH-AIDS', '4'),
        ('AIDS403-LAB', 'Big Data Lab', 2, 'BTECH-AIDS', '4'),
        
        # Semester 5
        ('AIDS501-Lec', 'Data Mining', 3, 'BTECH-AIDS', '5'),
        ('AIDS502-Lec', 'Business Analytics', 3, 'BTECH-AIDS', '5'),
        ('AIDS503-LAB', 'Data Mining Lab', 2, 'BTECH-AIDS', '5'),
        
        # Semester 6
        ('AIDS601-Lec', 'Deep Learning', 3, 'BTECH-AIDS', '6'),
        ('AIDS602-Lec', 'Cloud Computing', 3, 'BTECH-AIDS', '6'),
        ('AIDS603-LAB', 'Deep Learning Lab', 2, 'BTECH-AIDS', '6'),
        
        # Semester 7
        ('AIDS701-Lec', 'Data Engineering', 3, 'BTECH-AIDS', '7'),
        ('AIDS702-LAB', 'Industry Project', 4, 'BTECH-AIDS', '7'),
    ]
    courses_data.extend(aids_courses)
    
    # ============ BTECH-CSE COURSES (All Semesters) ============
    cse_courses = [
        # Semester 1
        ('CSE101-Lec', 'Programming in C', 4, 'BTECH-CSE', '1'),
        ('CSE102-Lec', 'Engineering Mathematics I', 4, 'BTECH-CSE', '1'),
        ('CSE103-Lec', 'Physics for Engineers', 3, 'BTECH-CSE', '1'),
        ('CSE104-Lec', 'Engineering Chemistry', 3, 'BTECH-CSE', '1'),
        ('CSE105-LAB', 'C Programming Lab', 2, 'BTECH-CSE', '1'),
        ('CSE106-LAB', 'Physics Lab', 2, 'BTECH-CSE', '1'),
        
        # Semester 2
        ('CSE201-Lec', 'Data Structures', 4, 'BTECH-CSE', '2'),
        ('CSE202-Lec', 'Engineering Mathematics II', 3, 'BTECH-CSE', '2'),
        ('CSE203-Lec', 'Digital Logic Design', 3, 'BTECH-CSE', '2'),
        ('CSE204-Lec', 'Object Oriented Programming', 3, 'BTECH-CSE', '2'),
        ('CSE205-LAB', 'Data Structures Lab', 2, 'BTECH-CSE', '2'),
        ('CSE206-LAB', 'Digital Logic Lab', 2, 'BTECH-CSE', '2'),
        
        # Semester 3
        ('CSE301-Lec', 'Database Management Systems', 4, 'BTECH-CSE', '3'),
        ('CSE302-Lec', 'Discrete Mathematics', 3, 'BTECH-CSE', '3'),
        ('CSE303-Lec', 'Computer Organization', 3, 'BTECH-CSE', '3'),
        ('CSE304-Lec', 'Operating Systems', 3, 'BTECH-CSE', '3'),
        ('CSE305-LAB', 'DBMS Lab', 2, 'BTECH-CSE', '3'),
        ('CSE306-LAB', 'OS Lab', 2, 'BTECH-CSE', '3'),
        
        # Semester 4
        ('CSE401-Lec', 'Computer Networks', 3, 'BTECH-CSE', '4'),
        ('CSE402-Lec', 'Design & Analysis of Algorithms', 4, 'BTECH-CSE', '4'),
        ('CSE403-Lec', 'Software Engineering', 3, 'BTECH-CSE', '4'),
        ('CSE404-Lec', 'Theory of Computation', 3, 'BTECH-CSE', '4'),
        ('CSE405-LAB', 'Networks Lab', 2, 'BTECH-CSE', '4'),
        ('CSE406-LAB', 'Algorithms Lab', 2, 'BTECH-CSE', '4'),
        
        # Semester 5
        ('CSE501-Lec', 'Web Technologies', 3, 'BTECH-CSE', '5'),
        ('CSE502-Lec', 'Compiler Design', 3, 'BTECH-CSE', '5'),
        ('CSE503-Lec', 'Artificial Intelligence', 3, 'BTECH-CSE', '5'),
        ('CSE504-Lec', 'Computer Graphics', 3, 'BTECH-CSE', '5'),
        ('CSE505-LAB', 'Web Development Lab', 2, 'BTECH-CSE', '5'),
        ('CSE506-LAB', 'AI Lab', 2, 'BTECH-CSE', '5'),
        
        # Semester 6
        ('CSE601-Lec', 'Machine Learning', 3, 'BTECH-CSE', '6'),
        ('CSE602-Lec', 'Cloud Computing', 3, 'BTECH-CSE', '6'),
        ('CSE603-Lec', 'Information Security', 3, 'BTECH-CSE', '6'),
        ('CSE604-Lec', 'Mobile Computing', 3, 'BTECH-CSE', '6'),
        ('CSE605-LAB', 'ML Lab', 2, 'BTECH-CSE', '6'),
        ('CSE606-LAB', 'Cloud Computing Lab', 2, 'BTECH-CSE', '6'),
        
        # Semester 7
        ('CSE701-Lec', 'Big Data Analytics', 3, 'BTECH-CSE', '7'),
        ('CSE702-Lec', 'Internet of Things', 3, 'BTECH-CSE', '7'),
        ('CSE703-Lec', 'Deep Learning', 3, 'BTECH-CSE', '7'),
        ('CSE704-LAB', 'IoT Lab', 2, 'BTECH-CSE', '7'),
        ('CSE705-LAB', 'Project Phase I', 3, 'BTECH-CSE', '7'),
        
        # Semester 8
        ('CSE801-Lec', 'Blockchain Technology', 3, 'BTECH-CSE', '8'),
        ('CSE802-Lec', 'Quantum Computing', 3, 'BTECH-CSE', '8'),
        ('CSE803-LAB', 'Project Phase II', 6, 'BTECH-CSE', '8'),
    ]
    courses_data.extend(cse_courses)
    
    # Insert all courses
    query = "INSERT INTO Courses (course_code, course_name, frequency, Program_name, semester_id) VALUES (?, ?, ?, ?, ?)"
    cursor.executemany(query, courses_data)
    connection.commit()
    print(f"Inserted {len(courses_data)} rows into Courses table")

def insert_professors(connection):
    """Insert professor data with MAXIMUM faculty names - 300+ professors"""
    cursor = connection.cursor()
    
    # COMPREHENSIVE LIST OF 300+ INDIAN PROFESSOR NAMES
    professor_names = [
        # Senior Professors (40)
        "Dr. Rajesh Kumar", "Dr. Sunita Sharma", "Prof. Anil Gupta", "Dr. Priya Singh",
        "Prof. Suresh Patel", "Dr. Meena Venkatesh", "Prof. Vikram Malhotra", "Dr. Kavita Reddy",
        "Prof. Rakesh Joshi", "Dr. Deepa Nair", "Prof. Manoj Tiwari", "Dr. Pooja Desai",
        "Prof. Harish Rao", "Dr. Lata Krishnan", "Prof. Sanjay Mehta", "Dr. Anita Thakur",
        "Prof. R. Krishnamurthy", "Dr. Vasudha Sharma", "Prof. M. Rajasekhar", "Dr. Uma Shankar",
        "Prof. T. Srinivasan", "Dr. Padma Subramanian", "Prof. Venkatesh Iyer", "Dr. Shanti Prasad",
        "Prof. Narayan Murthy", "Dr. Sudha Rao", "Prof. Gopalakrishnan", "Dr. Nirmala Devi",
        "Prof. Balakrishnan", "Dr. Chandrika Singh", "Prof. Dinesh Gupta", "Dr. Sheela Menon",
        "Prof. Ramesh Chandra", "Dr. Neelam Saxena", "Prof. K. Venkataraman", "Dr. Shobha Rani",
        "Prof. M. Srinivasan", "Dr. Radhika Krishnan", "Prof. Anand Tiwari", "Dr. Malini Iyer",
        
        # Associate Professors (50)
        "Dr. Alok Mishra", "Dr. Nidhi Kapoor", "Dr. Prakash Iyer", "Dr. Swati Choudhury",
        "Dr. Ravi Shankar", "Dr. Divya Menon", "Dr. Ashok Bhatia", "Dr. Reena George",
        "Dr. Mohan Das", "Dr. Shalini Verma", "Dr. Karthik Subramanian", "Dr. Jyoti Singh",
        "Dr. Venkat Raman", "Dr. Neha Gupta", "Dr. Sridhar Rajan", "Dr. Preeti Sharma",
        "Dr. Amitabh Bachchan", "Dr. Jaya Sharma", "Dr. Amit Shah", "Dr. Rajnath Singh",
        "Dr. Smriti Irani", "Dr. Piyush Goyal", "Dr. Nirmala Sitharaman", "Dr. S. Jaishankar",
        "Dr. Arvind Kejriwal", "Dr. Mamata Banerjee", "Dr. Yogi Adityanath", "Dr. Nitish Kumar",
        "Dr. Naveen Patnaik", "Dr. Hemant Soren", "Dr. Bhupesh Baghel", "Dr. Ashok Gehlot",
        "Dr. Shivraj Chouhan", "Dr. Devendra Fadnavis", "Dr. Eknath Shinde", "Dr. Uddhav Thackeray",
        "Dr. M.K. Stalin", "Dr. Pinarayi Vijayan", "Dr. Siddaramaiah", "Dr. B.S. Yediyurappa",
        "Dr. K. Chandrashekar Rao", "Dr. Jagan Mohan Reddy", "Dr. N. Chandrababu Naidu", "Dr. Himanta Sarma",
        "Dr. Manik Saha", "Dr. Conrad Sangma", "Dr. Neiphiu Rio", "Dr. Pema Khandu",
        "Dr. Prem Singh", "Dr. Trivendra Rawat", "Dr. Pushkar Dhami",
        
        # Assistant Professors (60)
        "Prof. Amit Khanna", "Prof. Ritu Jain", "Prof. Deepak Saxena", "Prof. Anjali Nair",
        "Prof. Vikas Yadav", "Prof. Sneha Pillai", "Prof. Sandeep Kaur", "Prof. Megha Patel",
        "Prof. Rahul Bose", "Prof. Shweta Pandey", "Prof. Jitendra Singh", "Prof. Kanika Ahuja",
        "Prof. Manish Thakur", "Prof. Neelam Reddy", "Prof. Gaurav Bhatnagar", "Prof. Rachna Mehra",
        "Prof. Karan Johar", "Prof. Farah Khan", "Prof. Rohit Shetty", "Prof. Zoya Akhtar",
        "Prof. Anurag Kashyap", "Prof. Vikramaditya Motwane", "Prof. Dibakar Banerjee", "Prof. Shoojit Sircar",
        "Prof. Aamir Khan", "Prof. Shah Rukh Khan", "Prof. Salman Khan", "Prof. Akshay Kumar",
        "Prof. Ranbir Kapoor", "Prof. Ranveer Singh", "Prof. Hrithik Roshan", "Prof. Saif Ali Khan",
        "Prof. Deepika Padukone", "Prof. Priyanka Chopra", "Prof. Alia Bhatt", "Prof. Kareena Kapoor",
        "Prof. Katrina Kaif", "Prof. Anushka Sharma", "Prof. Vidya Balan", "Prof. Kangana Ranaut",
        "Prof. Sachin Tendulkar", "Prof. Virat Kohli", "Prof. MS Dhoni", "Prof. Rohit Sharma",
        "Prof. Jasprit Bumrah", "Prof. Hardik Pandya", "Prof. Rishabh Pant", "Prof. KL Rahul",
        "Prof. Sunil Chhetri", "Prof. Baichung Bhutia", "Prof. Mary Kom", "Prof. PV Sindhu",
        "Prof. Saina Nehwal", "Prof. Neeraj Chopra", "Prof. Hima Das", "Prof. Milkha Singh",
        
        # Your Requested Names (included)
        "Prof. Vikal Singh", "Prof. Kana Ram", "Prof. Jinka Prasad", "Prof. Mahendra Singh",
        "Prof. Sanjay People", "Dr. Vikram Rathore", "Prof. Neeraj Kumar", "Dr. Sheela Menon",
        "Prof. Harsh Vardhan", "Dr. Yog Raj", "Prof. Ayush Singh", "Dr. Mayank Gupta",
        "Prof. Saurabh Mishra", "Dr. Ashwin Krishnan", "Prof. Namit Khanna", "Dr. Joe Mathew",
        "Prof. Shamshad Husain", "Dr. Faisal Talib", "Dr. Mohd. Sharique", "Mr. Faisal Alam",
        "Mr. Asad Mohammed Khan", "Mr. Muneeb Hasan Khan", "Mr. Misbahur Rahman Warsi",
        "Mr. Izharauddin", "Mr. Tameem Ahmad", "Mr. Nadeem Akhtar", "Dr. Saiful Islam",
        "Dr. Rashid Ali", "Prof. M.M. Sufyan Beg", "Prof. Nesar Ahmad", "Prof. Ash Mohammad Abbas",
        "Prof. Mohammad Sarosh Umar",
        
        # More Names (100+ additional)
        "Dr. Arjun Reddy", "Prof. Bhavana Rao", "Dr. Chandra Sekhar", "Prof. Divya Spandana",
        "Dr. Eswar Prasad", "Prof. Gayatri Devi", "Dr. Hemanth Kumar", "Prof. Indira Gandhi",
        "Dr. Jagdish Chandra", "Prof. Kalpana Chawla", "Dr. Lakshmi Mittal", "Prof. Madhavan Nair",
        "Dr. Narayana Murthy", "Prof. Omana Kurian", "Dr. Prathap Reddy", "Prof. Queenie Singh",
        "Dr. Ratan Tata", "Prof. Sudha Murty", "Dr. Thirumalai", "Prof. Usha Kiran",
        "Dr. Ved Prakash", "Prof. William Singh", "Dr. Xavier Fernandez", "Prof. Yash Chopra",
        "Dr. Zubin Mehta", "Prof. Aishwarya Rai", "Dr. Bhim Rao", "Prof. Chiranjeevi",
        "Dr. Dev Anand", "Prof. Esha Gupta", "Dr. Farooq Abdullah", "Prof. Ghulam Nabi",
        "Dr. Hema Malini", "Prof. Irrfan Khan", "Dr. Jaya Prada", "Prof. Kamal Haasan",
        "Dr. Leela Samson", "Prof. M. Night Shyamalan", "Dr. Naseeruddin Shah", "Prof. Om Puri",
        "Dr. Pankaj Kapur", "Prof. Qazi Mukarram", "Dr. Raj Kapoor", "Prof. Shabana Azmi",
        "Dr. Tabu", "Prof. Urmila Matondkar", "Dr. Vyjayanthimala", "Prof. Waheeda Rehman",
        "Dr. Yana Gupta", "Prof. Zayed Khan", "Dr. Aditya Roy", "Prof. Bhumi Pednekar",
        "Dr. Chitrangada Singh", "Prof. Disha Patani", "Dr. Elli Avram", "Prof. Fatima Sana",
        "Dr. Genelia D'Souza", "Prof. Hansika Motwani", "Dr. Ileana D'Cruz", "Prof. Jacqueline Fernandez",
        "Dr. Kiara Advani", "Prof. Lara Dutta", "Dr. Malaika Arora", "Prof. Nargis Fakhri",
        "Dr. Omkara", "Prof. Parineeti Chopra", "Dr. Raveena Tandon", "Prof. Shilpa Shetty",
        "Dr. Tamannaah Bhatia", "Prof. Upen Patel", "Dr. Vidyut Jammwal", "Prof. Yami Gautam",
        "Dr. Zarine Khan", "Prof. Ahan Shetty", "Dr. Boman Irani", "Prof. Chunky Pandey",
        "Dr. Darsheel Safary", "Prof. Emraan Hashmi", "Dr. Fardeen Khan", "Prof. Govinda",
        "Dr. Himesh Reshammiya", "Prof. Imran Khan", "Dr. Jackie Shroff", "Prof. Kunaal Roy",
        "Dr. Luv Sinha", "Prof. Mohnish Bahl", "Dr. Nana Patekar", "Prof. Omkar Kapoor",
        "Dr. Piyush Mishra", "Prof. Raj Babbar", "Dr. Sanjay Dutt", "Prof. Tusshar Kapoor",
        "Dr. Uday Chopra", "Prof. Vivek Oberoi", "Dr. Wamiqa Gabbi", "Prof. Yash Dasgupta",
        "Dr. Zareen Khan", "Prof. Akhil Akkineni", "Dr. Bhagyashree", "Prof. Celina Jaitly",
        "Dr. Dino Morea", "Prof. Esha Deol", "Dr. Fawad Khan", "Prof. Gulshan Grover",
        "Dr. Harsh Nagar", "Prof. Inder Kumar", "Dr. Johnny Lever", "Prof. Kader Khan",
        "Dr. Lilette Dubey", "Prof. Mahima Chaudhry", "Dr. Nivedita Joshi", "Prof. Padmini Kolhapure",
        "Dr. Rimi Sen", "Prof. Shakti Kapoor", "Dr. Tinnu Anand", "Prof. Upasana Singh",
        "Dr. Vindu Singh", "Prof. Yashpal Sharma", "Dr. Zakir Hussain"
    ]
    
    # Get all courses
    cursor.execute("SELECT course_code, Program_name FROM Courses")
    courses = cursor.fetchall()
    
    professor_data = []
    professor_id = 1
    
    # Assign 3-5 professors per course for MAXIMUM coverage
    for course in courses:
        course_code = course[0]
        program = course[1]
        
        # Assign 4-6 professors per course
        num_professors = random.randint(4, 6)
        selected_profs = random.sample(professor_names, min(num_professors, len(professor_names)))
        
        for prof_name in selected_profs:
            # Generate professor ID (T001, T002, etc.)
            prof_id = f"T{professor_id:03d}"
            
            # Generate phone number
            phone = 9000000000 + professor_id
            
            # Generate email
            email_name = prof_name.lower().replace('dr. ', '').replace('prof. ', '').replace('mr. ', '')
            email_name = email_name.replace(' ', '.').replace('(', '').replace(')', '')
            email = f"{email_name}@college.edu"
            
            professor_data.append((prof_id, prof_name, course_code, str(phone), email))
            professor_id += 1
    
    # Insert in batches
    batch_size = 100
    for i in range(0, len(professor_data), batch_size):
        batch = professor_data[i:i+batch_size]
        query = "INSERT INTO Professor (Professor_id, Professor_name, course_code, Phone_number, Email_ID) VALUES (?, ?, ?, ?, ?)"
        cursor.executemany(query, batch)
        connection.commit()
        print(f"Inserted batch {i//batch_size + 1} of professors")
    
    print(f"Total Inserted {len(professor_data)} rows into Professor table")

def insert_labs(connection):
    """Insert lab data - 100+ labs"""
    cursor = connection.cursor()
    lab_data = []
    
    # Building A Labs (A Block)
    for i in range(1, 21):
        lab_data.append((f'101-A-LA-{i:02d}', str(random.choice([25,30,35,40]))))
        lab_data.append((f'201-A-LA-{i:02d}', str(random.choice([25,30,35,40]))))
        lab_data.append((f'301-A-LA-{i:02d}', str(random.choice([25,30,35,40]))))
    
    # Building B Labs (B Block)
    for i in range(1, 21):
        lab_data.append((f'101-B-LA-{i:02d}', str(random.choice([25,30,35,40]))))
        lab_data.append((f'201-B-LA-{i:02d}', str(random.choice([25,30,35,40]))))
        lab_data.append((f'301-B-LA-{i:02d}', str(random.choice([25,30,35,40]))))
    
    # Building C Labs (C Block)
    for i in range(1, 21):
        lab_data.append((f'C{i:02d}-LA', str(random.choice([25,30,35,40]))))
    
    # Building D Labs (D Block)
    for i in range(1, 21):
        lab_data.append((f'D{i:02d}-LA', str(random.choice([25,30,35,40]))))
    
    # Department Labs
    dept_labs = [
        ('CSE-LAB-01', '50'), ('CSE-LAB-02', '45'), ('CSE-LAB-03', '40'),
        ('ECE-LAB-01', '40'), ('ECE-LAB-02', '35'), ('ECE-LAB-03', '30'),
        ('MECH-LAB-01', '35'), ('MECH-LAB-02', '30'), ('MECH-LAB-03', '25'),
        ('CIVIL-LAB-01', '30'), ('CIVIL-LAB-02', '25'), ('CIVIL-LAB-03', '20'),
        ('PHY-LAB-01', '30'), ('PHY-LAB-02', '25'), ('CHEM-LAB-01', '30'),
        ('BIO-LAB-01', '25'), ('BIO-LAB-02', '20'), ('AI-LAB-01', '35'),
        ('ROBO-LAB-01', '30'), ('IOT-LAB-01', '25'), ('ML-LAB-01', '35'),
        ('DATA-SCI-LAB', '40'), ('CLOUD-LAB', '35'), ('CYBER-LAB', '30'),
    ]
    lab_data.extend(dept_labs)
    
    query = "INSERT INTO Lab (Lab_id, Lab_capacity) VALUES (?, ?)"
    cursor.executemany(query, lab_data)
    connection.commit()
    print(f"Inserted {len(lab_data)} rows into Lab table")

def insert_lectures(connection):
    """Insert lecture hall data - 150+ lecture halls"""
    cursor = connection.cursor()
    lecture_data = []
    
    # Large Lecture Halls
    large_halls = [
        ('AUDI-01', '500'), ('AUDI-02', '400'), ('AUDI-03', '350'),
        ('CONV-HALL-01', '600'), ('CONV-HALL-02', '550'), ('SEMINAR-01', '300'),
        ('SEMINAR-02', '250'), ('SEMINAR-03', '200'), ('LT-01', '180'),
        ('LT-02', '150'), ('LT-03', '120'), ('LT-04', '100'),
    ]
    lecture_data.extend(large_halls)
    
    # Building A Lecture Halls
    for i in range(1, 31):
        lecture_data.append((f'101-A-LH-{i:02d}', str(random.choice([60,75,90,120]))))
        lecture_data.append((f'201-A-LH-{i:02d}', str(random.choice([60,75,90,120]))))
        lecture_data.append((f'301-A-LH-{i:02d}', str(random.choice([60,75,90,120]))))
        lecture_data.append((f'401-A-LH-{i:02d}', str(random.choice([60,75,90,120]))))
    
    # Building B Lecture Halls
    for i in range(1, 31):
        lecture_data.append((f'101-B-LH-{i:02d}', str(random.choice([60,75,90,120]))))
        lecture_data.append((f'201-B-LH-{i:02d}', str(random.choice([60,75,90,120]))))
        lecture_data.append((f'301-B-LH-{i:02d}', str(random.choice([60,75,90,120]))))
    
    # Building C Lecture Halls
    for i in range(1, 31):
        lecture_data.append((f'C{i:02d}-LH', str(random.choice([60,75,90,120]))))
    
    # Building D Lecture Halls
    for i in range(1, 31):
        lecture_data.append((f'D{i:02d}-LH', str(random.choice([60,75,90,120]))))
    
    # Department Lecture Halls
    dept_halls = [
        ('CSE-LH-01', '120'), ('CSE-LH-02', '100'), ('CSE-LH-03', '90'),
        ('ECE-LH-01', '90'), ('ECE-LH-02', '80'), ('ECE-LH-03', '75'),
        ('MECH-LH-01', '85'), ('MECH-LH-02', '80'), ('MECH-LH-03', '75'),
        ('CIVIL-LH-01', '80'), ('CIVIL-LH-02', '75'), ('CIVIL-LH-03', '70'),
        ('MBA-LH-01', '75'), ('MBA-LH-02', '70'), ('MBA-LH-03', '65'),
        ('BCA-LH-01', '70'), ('BCA-LH-02', '65'), ('BCA-LH-03', '60'),
        ('BBA-LH-01', '70'), ('BBA-LH-02', '65'), ('BBA-LH-03', '60'),
        ('ARCH-LH-01', '65'), ('ARCH-LH-02', '60'), ('ARCH-LH-03', '55'),
    ]
    lecture_data.extend(dept_halls)
    
    query = "INSERT INTO Lecture (lecture_id, lecture_capacity) VALUES (?, ?)"
    cursor.executemany(query, lecture_data)
    connection.commit()
    print(f"Inserted {len(lecture_data)} rows into Lecture table")

def ensure_data_quality(connection):
    """Verify data quality"""
    cursor = connection.cursor()
    
    # Count total professors
    cursor.execute("SELECT COUNT(*) FROM Professor")
    prof_count = cursor.fetchone()[0]
    print(f"Total professors in database: {prof_count}")
    
    # Count total courses
    cursor.execute("SELECT COUNT(*) FROM Courses")
    course_count = cursor.fetchone()[0]
    print(f"Total courses in database: {course_count}")
    
    # Check courses per program
    cursor.execute("""
        SELECT Program_name, COUNT(*) as course_count 
        FROM Courses 
        GROUP BY Program_name 
        ORDER BY Program_name
    """)
    program_courses = cursor.fetchall()
    print("\nCourses per program:")
    for prog, count in program_courses:
        print(f"  {prog}: {count} courses")
    
    # Check professors per course
    cursor.execute("""
        SELECT course_code, COUNT(*) as prof_count 
        FROM Professor 
        GROUP BY course_code 
        ORDER BY prof_count DESC 
        LIMIT 10
    """)
    top_courses = cursor.fetchall()
    print("\nTop 10 courses with most professors:")
    for course, count in top_courses:
        print(f"  {course}: {count} professors")
    
    # Verify no course is without professor
    cursor.execute("""
        SELECT c.course_code, c.course_name 
        FROM Courses c 
        LEFT JOIN Professor p ON c.course_code = p.course_code 
        WHERE p.course_code IS NULL
    """)
    missing = cursor.fetchall()
    if missing:
        print(f"\nWARNING: {len(missing)} courses have NO professors!")
        for course in missing[:5]:
            print(f"  {course[0]} - {course[1]}")
    else:
        print("\n✓ All courses have at least one professor assigned")

def main():
    """Main function to run all insertions"""
    print("=" * 60)
    print("STARTING COMPREHENSIVE DATA INSERTION")
    print("=" * 60)
    
    connection = create_connection()
    
    if connection:
        try:
            cursor = connection.cursor()
            
            # Drop existing tables
            cursor.executescript("""
            DROP TABLE IF EXISTS Admin;
            DROP TABLE IF EXISTS Program;
            DROP TABLE IF EXISTS Courses;
            DROP TABLE IF EXISTS Professor;
            DROP TABLE IF EXISTS Lab;
            DROP TABLE IF EXISTS Lecture;
            """)
            
            # Create fresh tables
            cursor.executescript("""
            CREATE TABLE Admin (
                admin_id TEXT PRIMARY KEY,
                name TEXT,
                email TEXT,
                username TEXT,
                password TEXT
            );
            
            CREATE TABLE Program (
                Program_name TEXT,
                semester_id TEXT,
                PRIMARY KEY (Program_name, semester_id)
            );
            
            CREATE TABLE Courses (
                course_code TEXT PRIMARY KEY,
                course_name TEXT,
                frequency INTEGER,
                Program_name TEXT,
                semester_id TEXT
            );
            
            CREATE TABLE Professor (
                Professor_id TEXT PRIMARY KEY,
                Professor_name TEXT,
                course_code TEXT,
                Phone_number TEXT,
                Email_ID TEXT,
                FOREIGN KEY (course_code) REFERENCES Courses(course_code)
            );
            
            CREATE TABLE Lab (
                Lab_id TEXT PRIMARY KEY,
                Lab_capacity TEXT
            );
            
            CREATE TABLE Lecture (
                lecture_id TEXT PRIMARY KEY,
                lecture_capacity TEXT
            );
            """)
            connection.commit()
            print("✓ Tables created successfully")
            
            # Insert all data
            insert_admin(connection)
            insert_program(connection)
            insert_courses(connection)
            insert_professors(connection)
            insert_labs(connection)
            insert_lectures(connection)
            
            # Verify data quality
            ensure_data_quality(connection)
            
            print("\n" + "=" * 60)
            print("✅ ALL DATA INSERTED SUCCESSFULLY!")
            print("=" * 60)
            
            # Final counts
            cursor.execute("SELECT COUNT(*) FROM Admin"); admin = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM Program"); prog = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM Courses"); course = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM Professor"); prof = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM Lab"); lab = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM Lecture"); lec = cursor.fetchone()[0]
            
            print(f"\nFINAL DATABASE SUMMARY:")
            print(f"  Admins: {admin}")
            print(f"  Programs: {prog}")
            print(f"  Courses: {course}")
            print(f"  Professors: {prof}")
            print(f"  Labs: {lab}")
            print(f"  Lecture Halls: {lec}")
            print("=" * 60)
            
        except Error as e:
            print(f"❌ Error inserting data: {e}")
            connection.rollback()
        finally:
            cursor.close()
            connection.close()
            print("Database connection closed")

if __name__ == "__main__":
    main()




    # 2. Delete the existing database
# rm db.sqlite3

# # 3. Run the new insert_data.py
# python insert_data.py

# # 4. Run Django migrations
# python manage.py migrate

# # 5. Start server
# python manage.py runserver