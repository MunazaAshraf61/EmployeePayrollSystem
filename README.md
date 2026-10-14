# Employee Payroll System

## About the Project
The Employee Payroll System is a Python-based project developed to manage employee information and calculate salaries. It allows users to add employees, view their details, calculate net salary, search for employees, and generate payslips.


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

## Files in the Project
- `EmployyePayrollSystem.py` – Contains the main Python program.
- `payroll.csv` – Stores employee information and salary details.
- `payslip_100.txt` – An example of a generated employee payslip. Other payslips are created with filenames based on employee IDs.
- OUTPUT_01.png,OUTPUT_02.Png,OUTPUT_03.Png,OUTPUT_04.Png – screenshot showing the program running.
- README.md – provides information about the project.


## Salary Calculation
Net salary is calculated using the following formula:

**Net Salary = Basic Salary + Allowance − Deduction**

For example, if the basic salary is Rs. 30,000, the allowance is Rs. 5,000, and the deduction is Rs. 2,000, the net salary is Rs. 33,000.


Author: Munaza
Project: Employee Payroll System using Python
