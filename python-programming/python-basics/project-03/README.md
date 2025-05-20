# 📘 Student Management System (Basic Python OOP)
This is a simple Python program that demonstrates basic object-oriented programming (OOP) concepts. It allows for adding, removing, updating, and searching for student records using Python classes, lists, and methods.

## 🚀 Features
Add a new student (name, ID, CGPA)

Remove a student by name

Update an existing student's record

Search and display a student’s details

## 🧠 Concepts Covered
Class and object creation

Constructors (__init__)

Instance variables and methods

Lists of objects

String formatting

Conditional logic

## 🏗️ Project Structure
Student: A class representing individual student data

StudentManagement: A class for managing student operations

## 📌 Example Usage

students_management = StudentManagement()

students_management.add_student('Ismail', 'U12', 3.12)
students_management.add_student('Ishaq', 'U13', 3.50)

students_management.search_student('Ismail')
students_management.remove_student('Ishaq')
students_management.update_student_record('Ismail', 'U12-NEW', 3.45)
💻 Technologies Used
Python 3.x

No external libraries (just core Python)