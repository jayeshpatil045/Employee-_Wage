'''
@Author: Jayesh Patil
@Date: 2024-08-28
@Last Modified by: Jayesh Patil
@Title: Employee Wage Program 
'''

import random
from abc import ABC, abstractmethod

class ComputeWage(ABC):
    @abstractmethod
    def calculate_monthly_wage(self):
        pass
    @abstractmethod
    def calculate_employee_wage(self):
        pass
    @abstractmethod
    def add_employee(self, employee_name):
        pass
    @abstractmethod
    def display_wages(self):
        pass

class EmployeeWage(ComputeWage):
    def __init__(self, company_name, wage_per_hour, max_working_days, max_working_hours, full_day_hour, part_time_day_hour):
        """
        Description:
            Initializes the EmployeeWage object with company details and tracking variables.
        
        Parameters:
            company_name (str): Name of the company.
            wage_per_hour (int): Wage per hour for the company.
            max_working_days (int): Maximum working days per month for the company.
            max_working_hours (int): Maximum working hours per month for the company.
            full_day_hour (int): Full day working hours.
            part_time_day_hour (int): Part-time working hours.
        
        Returns:
            None
        """
        self.company_name = company_name
        self.wage_per_hour = wage_per_hour
        self.max_working_days = max_working_days
        self.max_working_hours = max_working_hours
        self.full_day_hour = full_day_hour
        self.part_time_day_hour = part_time_day_hour
        self.employees = {}

    def add_employee(self, employee_name):
        """
        Description:
            Adds an employee to the company.
        
        Parameters:
            employee_name (str): Name of the employee.
        
        Returns:
            None
        """
        self.employees[employee_name] = {
            "total_wage": 0,
            "total_hours": 0,
            "total_days": 0,
            "daily_wages": []
        }

    @classmethod
    def check_attendance(cls):
        """
        Description:
            Randomly selects from a list to check if the employee is present, part-time, or absent.
        
        Parameters:
            None
        
        Returns:
            int: 0 if absent, 1 if full-time, 2 if part-time.
        """
        attendance_list = [0, 1, 2]
        random.shuffle(attendance_list)
        return attendance_list[0]

    def calculate_employee_wage(self, attendance):
        """
        Description:
            Calculate daily wage based on attendance using a match-case statement.
        
        Parameters:
            attendance (int): Attendance status (0: absent, 1: full-time, 2: part-time).
        
        Returns:
            tuple: A tuple containing the calculated daily wage and hours worked.
        """
        match attendance:
            case 1:  # Full-time
                return self.wage_per_hour * self.full_day_hour, self.full_day_hour
            case 2:  # Part-time
                return self.wage_per_hour * self.part_time_day_hour, self.part_time_day_hour
            case _:
                return 0, 0  # Absent

    def calculate_monthly_wage(self):
        """
        Description:
            Calculate the monthly wage for each employee based on the condition of total working hours or days.
        
        Parameters:
            None
        
        Returns:
            None
        """
        for employee_name in self.employees:
            while self.employees[employee_name]["total_days"] < self.max_working_days and \
                  self.employees[employee_name]["total_hours"] < self.max_working_hours:
                attendance = self.check_attendance()
                daily_wage, hours_worked = self.calculate_employee_wage(attendance)
                self.employees[employee_name]["daily_wages"].append(daily_wage)
                self.employees[employee_name]["total_wage"] += daily_wage
                self.employees[employee_name]["total_hours"] += hours_worked
                self.employees[employee_name]["total_days"] += 1

    def display_wages(self):
        """
        Description:
            Display the daily wages and the total wage for each employee in the company.
        
        Parameters:
            None
        
        Returns:
            None
        """
        for employee_name, data in self.employees.items():
            print(f"\n{self.company_name} - Wages for {employee_name}:")
            for day, wage in enumerate(data["daily_wages"], start=1):
                print(f"Day {day}: ${wage}")

            print(f"Total wage for {employee_name} for the month is {data['total_wage']}.")
            print(f"Total working days: {data['total_days']}")
            print(f"Total working hours: {data['total_hours']}")

class EmpWageBuilder:
    def __init__(self):
        """
        Description:
            Initializes the EmpWageBuilder object to manage multiple companies.
        
        Parameters:
            None
        
        Returns:
            None
        """
        self.companies = []

    def add_company(self, company_name, wage_per_hour, max_working_days, max_working_hours, full_day_hour, part_time_day_hour, num_employees):
        """
        Description:
            Adds a company to the list, computes its total wage, and adds employees.
        
        Parameters:
            company_name (str): Name of the company.
            wage_per_hour (int): Wage per hour for the company.
            max_working_days (int): Maximum working days per month for the company.
            max_working_hours (int): Maximum working hours per month for the company.
            full_day_hour (int): Full day working hours.
            part_time_day_hour (int): Part-time working hours.
            num_employees (int): Number of employees to add to the company.
        
        Returns:
            None
        """
        company = EmployeeWage(company_name, wage_per_hour, max_working_days, max_working_hours, full_day_hour, part_time_day_hour)
        for _ in range(num_employees):
            employee_name = input(f"Enter employee name for {company_name}: ")
            company.add_employee(employee_name)
        company.calculate_monthly_wage()
        self.companies.append(company)

    def add_employee_to_company(self):
        """
        Description:
            Adds an employee to a specific company after it has been created.
        
        Parameters:
            None
        
        Returns:
            None
        """
        company_name = input("Enter the name of the company to add an employee: ")
        for company in self.companies:
            if company.company_name == company_name:
                employee_name = input(f"Enter employee name for {company_name}: ")
                company.add_employee(employee_name)
                company.calculate_monthly_wage()
                print(f"Employee {employee_name} added to {company_name}.")
                return
        print(f"Company {company_name} not found.")

    def modify_company_details(self):
        """
        Description:
            Modify the details of an existing company.
        
        Parameters:
            None
        
        Returns:
            None
        """
        company_name = input("Enter the name of the company to modify: ")
        for company in self.companies:
            if company.company_name == company_name:
                print(f"Modifying details for {company_name}.")
                company.wage_per_hour = int(input("Enter new wage per hour: "))
                company.max_working_days = int(input("Enter new maximum working days per month: "))
                company.max_working_hours = int(input("Enter new maximum working hours per month: "))
                company.full_day_hour = int(input("Enter new full day working hours: "))
                company.part_time_day_hour = int(input("Enter new part-time working hours: "))
                return
        print(f"Company {company_name} not found.")

    def display_all_wages(self):
        """
        Description:
            Displays the wages for all companies and their employees.
        
        Parameters:
            None
        
        Returns:
            None
        """
        for company in self.companies:
            company.display_wages()

    def get_total_wage_by_company(self, company_name):
        """
        Description:
            Get the total wage for a specific company by summing up all employees' wages.
        
        Parameters:
            company_name (str): Name of the company.
        
        Returns:
            int: Total wage for the company or None if the company is not found.
        """
        for company in self.companies:
            if company.company_name == company_name:
                total_wage = sum(employee["total_wage"] for employee in company.employees.values())
                return total_wage
        return None

def main():
    """
    Description:
        Main function to run the Employee Wage Program.
    
    Parameters:
        None
    
    Returns:
        None
    """
    print("Welcome to Employee Wage Program for Multiple Companies")
    builder = EmpWageBuilder()

    while True:
        print("\nEmployee Wage Program Menu")
        print("1. Add Company and Calculate Wage")
        print("2. Modify Company Details")
        print("3. Add Employee to Specific Company")
        print("4. Display All Company Wages")
        print("5. Get Total Wage by Company")
        print("6. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            company_name = input("Enter the company name: ")
            wage_per_hour = int(input("Enter wage per hour: "))
            max_working_days = int(input("Enter maximum working days per month: "))
            if max_working_days > 30:
                print("Error: Maximum working days cannot exceed 30. Please enter a valid number.")
                continue
            max_working_hours = int(input("Enter maximum working hours per month: "))
            full_day_hour = int(input("Enter full day working hours: "))
            part_time_day_hour = int(input("Enter part-time working hours: "))
            num_employees = int(input(f"Enter the number of employees in {company_name}: "))
            
            builder.add_company(company_name, wage_per_hour, max_working_days, max_working_hours, full_day_hour, part_time_day_hour, num_employees)
        
        elif choice == 2:
            builder.modify_company_details()
        
        elif choice == 3:
            builder.add_employee_to_company()

        elif choice == 4:
            builder.display_all_wages()

        elif choice == 5:
            company_name = input("Enter the company name to get total wage: ")
            total_wage = builder.get_total_wage_by_company(company_name)
            if total_wage is not None:
                print(f"Total wage for {company_name}: {total_wage}")
            else:
                print(f"Company {company_name} not found.")
        
        elif choice == 6:
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
