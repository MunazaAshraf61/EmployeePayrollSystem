# Employee Payroll System

## About the Project
The Employee Payroll System is a Python-based project developed to manage employee information and calculate salaries. It allows users to add employees, view their details, calculate net salary, search for employees, and generate payslips.

This project was created to practice object-oriented programming concepts in Python.

## Features
- Add new employees with their details.
- Display all employee records.
- Calculate net salary.
- Search for an employee using their ID.
- Generate and save employee payslips.
- Save payroll information in a CSV file.
- Handle invalid inputs and file-related errors.

## Technologies Used
- Python
- CSV file handling
- Object-Oriented Programming (OOP)

## OOP Concepts Used
- **Classes and Objects:** Used to organize employee information and payroll operations.
- **Inheritance:** `SalariedEmployee` inherits from the abstract `Employee` class.
- **Abstraction:** The `Employee` class uses Python's `abc` module and an abstract method for salary calculation.
- **Exception Handling:** Used to handle invalid inputs and file-related errors.

## Files Created
- `EmployyePayrollSystem.py` – Contains the main Python program.
- `payroll.csv` – Stores employee information and salary details.
- `payslip_100.txt` – An example of a generated employee payslip. Other payslips are created with filenames based on employee IDs.

## How to Run
1. Install Python 3 on your computer.
2. Download or clone this repository.
3. Open the project folder in VS Code or another Python editor.
4. Run the Python file:

   ```bash
   python EmployyePayrollSystem.py
   ```

5. Select an option from the menu and follow the instructions.

## Salary Calculation
Net salary is calculated using the following formula:

**Net Salary = Basic Salary + Allowance − Deduction**

For example, if the basic salary is Rs. 30,000, the allowance is Rs. 5,000, and the deduction is Rs. 2,000, the net salary is Rs. 33,000.

## Learning Outcome
This project helped me understand how to use classes, inheritance, abstraction, file handling, and exception handling in Python while developing a basic employee payroll management system.