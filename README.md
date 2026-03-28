# 📋 Student Report Card System

A complete command-line application built in Python to manage student records, calculate GPA, and generate report cards — with persistent data storage using JSON.

---

## 🚀 Features

- ➕ Add new students (name + roll number)
- 📝 Add subject-wise marks for each student
- 📊 Auto-calculate GPA based on average marks
- 🧾 Generate formatted report cards
- 👥 View all students at a glance
- 🏆 Find the top-performing student
- 💾 Data persists across sessions (saved to JSON file)

---

## 🧠 GPA Scale

| Average Marks | GPA  |
|---------------|------|
| Above 90      | 10.0 |
| Above 80      | 9.0  |
| Above 70      | 8.0  |
| Above 60      | 7.0  |
| Above 50      | 6.0  |
| 50 or below   | 0.0 (Fail) |

---

## 🗂️ Project Structure

```
student-report-card/
│
├── student_report_card.py   # Main application
├── students_data.json       # Auto-generated data file (after first run)
└── README.md                # You're reading this!
```

---

## ▶️ How to Run

```bash
python student_report_card.py
```

No external libraries needed. Uses only Python built-ins (`json`, `os`).

---

## 📸 Menu Preview

```
╔══════════════════════════════════╗
║   STUDENT REPORT CARD SYSTEM     ║
╠══════════════════════════════════╣
║  1. Add Student                  ║
║  2. Add Marks                    ║
║  3. View Report (one student)    ║
║  4. View All Students            ║
║  5. Top Student                  ║
║  6. Exit                         ║
╚══════════════════════════════════╝
```

---

## 🧪 Sample Report Card Output

```
=============================================
       STUDENT REPORT CARD
=============================================
  Name        : Swetank Kumar
  Roll Number : 101
---------------------------------------------
  Subject              Marks
---------------------------------------------
  Python                  88
  Math                    75
  English                 92
---------------------------------------------
  Average               85.00
  GPA                     9.0
  Result: ✅ PASS
=============================================
```

---

## 💡 Concepts Used

| Concept         | Where Used                        |
|-----------------|-----------------------------------|
| Dictionaries    | Student records, marks storage    |
| Lists           | Storing all students              |
| Functions       | Modular code (8 functions)        |
| For Loops       | Searching, calculating totals     |
| While Loop      | Main menu                         |
| If/Elif/Else    | GPA logic, menu choices           |
| Typecasting     | Converting input to int           |
| f-Strings       | Formatted report card output      |
| File I/O (JSON) | Persistent data storage           |

---

## 👨‍💻 Author

**Swetank Kumar**  
B.Tech CSE | Python Backend Developer (in progress)  

- 🔗 [LinkedIn](https://www.linkedin.com/in/swetank-kumar-703086307)  
- 🐙 [GitHub](https://github.com/Swetu07)  
- 💻 [LeetCode](https://leetcode.com/swetu07)

---

Built as part of a structured Python learning roadmap — from basics to backend development.
