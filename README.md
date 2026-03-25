# 🕒 TEMPOSYNK - Intelligent Timetable Synchronization System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Django](https://img.shields.io/badge/Django-4.1.6-green.svg)](https://djangoproject.com)
[![SQLite](https://img.shields.io/badge/SQLite-3-blue.svg)](https://sqlite.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **Automated academic scheduling system that generates conflict-free timetables using intelligent algorithms**

## 📌 Overview

TEMPOSYNK is a comprehensive timetable management system designed for educational institutions. It eliminates manual scheduling headaches by automatically generating optimized timetables that respect all constraints including faculty availability, room capacity, course frequency, and workload distribution.
## 📸 Screenshots & Demo Video

### 🎥 Demo Video
Watch the complete walkthrough of TEMPOSYNK in action:

[![TEMPOSYNK Demo Video](https://img.shields.io/badge/Watch%20Demo-Video-red?style=for-the-badge&logo=youtube)](https://github.com/HitanDubey/TEMPOSYNK-Intelligent-Timetable-Synchronization-System/blob/main/Demmo%20Video.mp4)

<details>
<summary>Click to view demo video link</summary>

**📹 Demo Video:** [Click here to watch/download](https://github.com/HitanDubey/TEMPOSYNK-Intelligent-Timetable-Synchronization-System/blob/main/Demmo%20Video.mp4)

</details>

### 🖼️ Screenshots

#### 🏠 Home Page
*Landing page with 3D background animation and system overview*

![Home Page](home.png)

#### ℹ️ About Page
*System information, mission, vision, and technology stack*

![About Page](about.png)

#### 📝 Registration Page
*User sign-up with password strength validation*

![Registration Page](regi.png)

#### 📊 Dashboard
*Admin dashboard with quick access to all features*

![Dashboard](dashboard.png)

#### ⚙️ Timetable Generator
*Configuration page for generating timetables with program, semester, and batch selection*

![Generator Page](genpage.png)

#### 📅 Generated Timetable Output
*Conflict-free timetable display with faculty workload and lab utilization reports*

![Output Page](output.png)

---
### ✨ Key Features

- **🤖 Intelligent Algorithm** - Python-powered engine that processes complex scheduling constraints
- **📊 Conflict-Free Scheduling** - Ensures no overlapping classes or resource conflicts
- **👥 Faculty Management** - Track workloads and handle replacements seamlessly
- **🏛️ Resource Optimization** - Maximize utilization of lecture halls and laboratories
- **📱 Multiple Export Formats** - Download timetables as PDF, Excel, Word, or CSV
- **📈 Comprehensive Reports** - Faculty workload and lab utilization analytics
- **🔧 Real-time Adjustments** - Professor replacement without regenerating entire timetable
- **🎨 Modern UI** - Dark-themed responsive interface with smooth animations

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

```bash
# Clone the repository
git clone https://github.com/HitanDubey/TEMPOSYNK.git
cd TEMPOSYNK

# Install dependencies
pip install -r requirements.txt
# go to the main directory where you run your local server
cd autotime
cd tt
# Initialize database with sample data
python insert_data.py

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver