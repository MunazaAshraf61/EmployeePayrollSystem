import csv
import os
from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, emp_id, name, department):
        self.emp_id = emp_id
        self.name = name
        self.department = department

    @abstractmethod
    def calculate_salary(self):
        pass

    def display_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")


class SalariedEmployee(Employee):
    def __init__(self, emp_id, name, department, basic_salary, allowance, deduction):
        super().__init__(emp_id, name, department)
        self.basic_salary = basic_salary
        self.allowance = allowance
        self.deduction = deduction

    def calculate_salary(self):
        return self.basic_salary + self.allowance - self.deduction


class PayrollSystem:
    def __init__(self, filename="payroll.csv"):
        self.filename = filename
        self.employees = {}
        self.load_data()

    #load employee data from CSV file
    def load_data(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, "r", newline="") as file:
                    reader = csv.DictReader(file)

                    for row in reader:
                        employee = SalariedEmployee(
                            row["emp_id"],
                            row["name"],
                            row["department"],
                            float(row["basic_salary"]),
                            float(row["allowance"]),
                            float(row["deduction"])
                        )
                        self.employees[employee.emp_id] = employee

        except (OSError, csv.Error, ValueError, KeyError) as e:
            print(f"Error loading payroll data: {e}")

    #save employee data to CSV file
    def save_data(self):
        try:
            with open(self.filename, "w", newline="") as file:
                fieldnames = [
                    "emp_id", "name", "department",
                    "basic_salary", "allowance", "deduction"
                ]

                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()

                for employee in self.employees.values():
                    writer.writerow({
                        "emp_id": employee.emp_id,
                        "name": employee.name,
                        "department": employee.department,
                        "basic_salary": employee.basic_salary,
                        "allowance": employee.allowance,
                        "deduction": employee.deduction
                    })

        except (OSError, csv.Error) as e:
            print(f"Error saving payroll data: {e}")
        else:
            print("Payroll data saved successfully.")

    #add a new employee
    def add_employee(self):
        try:
            emp_id = input("Enter employee ID: ").strip()

            if not emp_id:
                print("Employee ID cannot be empty.")
                return

            if emp_id in self.employees:
                print("An employee with this ID already exists.")
                return

            name = input("Enter employee name: ").strip()
            department = input("Enter department: ").strip()

            if not name or not department:
                print("Name and department cannot be empty.")
                return

            basic_salary = float(input("Enter basic salary: "))
            allowance = float(input("Enter allowance: "))
            deduction = float(input("Enter deduction: "))

            if basic_salary < 0 or allowance < 0 or deduction < 0:
                print("Salary, allowance, and deduction cannot be negative.")
                return

            if deduction > basic_salary + allowance:
                print("Deduction cannot exceed the total salary before deductions.")
                return

            employee = SalariedEmployee(
                emp_id, name, department,
                basic_salary, allowance, deduction
            )

            self.employees[emp_id] = employee
            print("Employee added successfully.")

            self.save_data()

        except ValueError:
            print("Invalid input. Please enter valid numeric amounts.")

    #display all employees
    def display_employees(self):
        if not self.employees:
            print("No employee records found.")
            return

        for employee in self.employees.values():
            print("\n-----------------------------")
            employee.display_details()
            print(f"Basic Salary: Rs. {employee.basic_salary:.2f}")
            print(f"Allowance: Rs. {employee.allowance:.2f}")
            print(f"Deduction: Rs. {employee.deduction:.2f}")
            print(f"Net Salary: Rs. {employee.calculate_salary():.2f}")

    #search for an employee
    def search_employee(self):
        emp_id = input("Enter employee ID to search: ").strip()

        employee = self.employees.get(emp_id)

        if employee:
            print("\nEmployee found:")
            employee.display_details()
            print(f"Net Salary: Rs. {employee.calculate_salary():.2f}")
        else:
            print("Employee not found.")

    #generate a payslip
    def generate_payslip(self):
        emp_id = input("Enter employee ID for payslip: ").strip()

        employee = self.employees.get(emp_id)

        if not employee:
            print("Employee not found.")
            return

        net_salary = employee.calculate_salary()

        payslip = (
            "\n========== EMPLOYEE PAYSLIP ==========\n"
            f"Employee ID: {employee.emp_id}\n"
            f"Name: {employee.name}\n"
            f"Department: {employee.department}\n"
            "--------------------------------------\n"
            f"Basic Salary: Rs. {employee.basic_salary:.2f}\n"
            f"Allowance: Rs. {employee.allowance:.2f}\n"
            f"Deduction: Rs. {employee.deduction:.2f}\n"
            "--------------------------------------\n"
            f"Net Salary: Rs. {net_salary:.2f}\n"
            "======================================\n"
        )

        print(payslip)

        # Save the payslip in a separate text file
        try:
            filename = f"payslip_{employee.emp_id}.txt"

            with open(filename, "w", encoding="utf-8") as file:
                file.write(payslip)

            print(f"Payslip saved as {filename}.")

        except OSError as e:
            print(f"Error saving payslip: {e}")



def main():
    payroll = PayrollSystem()

    while True:
        print("\n===== EMPLOYEE PAYROLL SYSTEM =====")
        print("1. Add Employee")
        print("2. Display All Employees")
        print("3. Calculate Salary")
        print("4. Generate Payslip")
        print("5. Search Employee")
        print("6. Save Payroll Data")
        print("7. Exit")

        try:
            choice = int(input("Enter your choice (1-7): "))

            if choice == 1:
                payroll.add_employee()

            elif choice == 2:
                payroll.display_employees()

            elif choice == 3:
                payroll.search_employee()

            elif choice == 4:
                payroll.generate_payslip()

            elif choice == 5:
                payroll.search_employee()

            elif choice == 6:
                payroll.save_data()

            elif choice == 7:
                payroll.save_data()
                print("Exiting Employee Payroll System. Goodbye!")
                break

            else:
                print("Invalid choice. Please select between 1 and 7.")

        except ValueError:
            print("Invalid input. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
