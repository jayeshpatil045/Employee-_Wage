'''
@Author: Jayesh Patil
@Date: 2024-08-26
@Last Modified by: Jayesh Patil
@Title: Employee Wage Program 
'''
import random

class EmployeeWage:
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
        self.total_wage = 0
        self.total_hours = 0
        self.total_days = 0
        self.daily_wages = []

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
            Calculate the monthly wage based on the condition of total working hours or days.

        Parameters:
            None

        Returns:
            None
        """
        while self.total_days < self.max_working_days and self.total_hours < self.max_working_hours:
            attendance = self.check_attendance()
            daily_wage, hours_worked = self.calculate_employee_wage(attendance)
            self.daily_wages.append(daily_wage)
            self.total_wage += daily_wage
            self.total_hours += hours_worked
            self.total_days += 1

    def display_wages(self):
        """
        Description:
            Display the daily wages and the total wage for the month.

        Parameters:
            None

        Returns:
            None
        """
        print(f"{self.company_name} - Daily wages for each day of the month:")
        for day, wage in enumerate(self.daily_wages, start=1):
            print(f"Day {day}: ${wage}")

        print(f"\nTotal wage for the month for {self.company_name} is ${self.total_wage}.")
        print(f"Total working days: {self.total_days}")
        print(f"Total working hours: {self.total_hours}")


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

    def add_company(self, company_name, wage_per_hour, max_working_days, max_working_hours, full_day_hour, part_time_day_hour):
        """
        Description:
            Adds a company to the list and computes its total wage.

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
        company = EmployeeWage(company_name, wage_per_hour, max_working_days, max_working_hours, full_day_hour, part_time_day_hour)
        company.calculate_monthly_wage()
        self.companies.append(company)

    def display_all_wages(self):
        """
        Description:
            Displays the wages for all companies.

        Parameters:
            None

        Returns:
            None
        """
        for company in self.companies:
            company.display_wages()

    def display_wage_sep(self, company_name):
        """
        Description:
            Displays the wages for a specific company.

        Parameters:
            company_name (str): Name of the company to display wages for.

        Returns:
            None
        """
        for company in self.companies:
            if company.company_name == company_name:
                company.display_wages()
                return
        print(f"No data found for company: {company_name}")

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
        print("2. Display All Company Wages")
        print("3. Display Specific Company Wage")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            company_name = input("Enter the company name: ")
            wage_per_hour = int(input("Enter wage per hour: "))
            max_working_days = int(input("Enter maximum working days per month: "))
            max_working_hours = int(input("Enter maximum working hours per month: "))
            full_day_hour = int(input("Enter full day working hours: "))
            part_time_day_hour = int(input("Enter part-time working hours: "))
            
            builder.add_company(company_name, wage_per_hour, max_working_days, max_working_hours, full_day_hour, part_time_day_hour)
        
        elif choice == 2:
            builder.display_all_wages()

        elif choice == 3:
            company_name = input("Enter the company name to display wage details: ")
            builder.display_wage_sep(company_name)
        
        elif choice == 4:
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
