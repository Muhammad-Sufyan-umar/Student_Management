# 🎓 Student Management System

A simple **Student Management System** built with Python using **Object-Oriented Programming (OOP)** concepts.

This project allows you to add, view, search, and delete student records through a simple command-line menu.

## 🚀 Features

* ➕ Add a new student
* 📋 View all student records
* 🔍 Search student by Roll Number
* 🗑️ Delete student record
* ⚠️ Prevent duplicate Roll Numbers
* 🚪 Exit the application

## 🛠️ Technologies Used

* **Python 3**
* **Object-Oriented Programming (OOP)**
* Classes and Objects
* Lists
* Loops
* Conditional Statements
* User Input

## 📂 Project Structure

```text
Student-Management-System/
│
├── student_management.py
└── README.md
```

## ▶️ How to Run

Make sure Python is installed on your computer.

Run the program using:

```bash
python student_management.py
```

## 💻 Menu

When you run the program, you will see:

```text
===== Student Management System =====
1. Add Student
2. View student
3. Search student
4. Delete student record
5. Exit
```

### 1️⃣ Add Student

Enter the student's:

* Roll Number
* Name
* GR Number

The program checks whether the Roll Number already exists before adding the student.

### 2️⃣ View Students

Displays all students currently stored in the system.

Example:

```text
=======Records========
Roll_No: 101 | Name: Ali | Gr_No: 12345
Roll_No: 102 | Name: Ahmed | Gr_No: 12346
```

### 3️⃣ Search Student

Searches for a student using their Roll Number.

```text
Enter Roll NO: 101
Roll_No: 101 | Name: Ali | Gr_No: 12345
```

If the student does not exist:

```text
Record Not Found
```

### 4️⃣ Delete Student

Deletes a student record using the Roll Number.

```text
Enter Roll Number to delete: 101
Record deleted successfully
```

### 5️⃣ Exit

Closes the Student Management System.

## 🧠 OOP Concepts Used

### `student` Class

Stores information about an individual student:

* `Roll_No`
* `name`
* `Gr_No`

### `Management` Class

Manages all student records and provides methods for:

* Adding students
* Displaying records
* Searching students
* Deleting students

## 📌 Note

Currently, student records are stored **temporarily in a Python list**. When the program is closed, the records are lost.

A future version can add **file handling or a database** to permanently store student records.

## 🔮 Future Improvements

* ✏️ Update student information
* 💾 Save records to a `.txt` or `.json` file
* 🔐 Add login/authentication
* 🗄️ Use SQLite/MySQL for permanent storage
* 🎨 Create a GUI version

## 👨‍💻 Author

**Muhammad Sufyan**

---

⭐ If you found this project useful, consider giving it a star!

