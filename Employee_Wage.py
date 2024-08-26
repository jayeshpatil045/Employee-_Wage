'''
@Author: Jayesh Patil
@Date: 2024-08-25
@Last Modified by: Jayesh Patil
@Title: Employee Wage Program 
'''
import random

class EmpWageBuilder:
    def __init__(self, company_name, wage_per_hour, full_day_hour, part_time_day_hour, max_working_days, max_working_hours):
        """
        Description:
            Initializes the EmpWageBuilder instance with company-specific wage parameters.

        Parameters:
            company_name (str): The name of the company.
            wage_per_hour (int): The wage per hour for the employee.
            full_day_hour (int): The number of hours for a full day of work.
            part_time_day_hour (int): The number of hours for a part-time day of work.
            max_working_days (int): The maximum number of working days in the month.
            max_working_hours (int): The maximum number of working hours in the month.
        """
        self.company_name = company_name
        self.wage_per_hour = wage_per_hour
        self.full_day_hour = full_day_hour
        self.part_time_day_hour = part_time_day_hour
        self.max_working_days = max_working_days
        self.max_working_hours = max_working_hours
        self.total_wage = 0
        self.total_hours = 0
        self.total_days = 0
        self.daily_wages = []

    @staticmethod
    def check_attendance():
        """
        Description:
            Randomly selects from a list to check if the employee is present, part-time, or absent.

        Return:
            int: Returns 0, 1, or 2 to indicate absence, full-time, or part-time, respectively.
        """
        attendance_list = [0, 1, 2]
        random.shuffle(attendance_list)
        return attendance_list[0]

    def calculate_employee_wage(self, attendance):
        """
        Description:
            Calculates the daily wage and hours worked based on attendance.

        Parameters:
            attendance (int): 0 for absent, 1 for full-time, 2 for part-time.

        Return:
            tuple: Returns a tuple containing the daily wage (int) and hours worked (int).
        """
        match attendance:
            case 1:  # Full-time
                return self.wage_per_hour * self.full_day_hour, self.full_day_hour
            case 2:  # Part-time
                return self.wage_per_hour * self.part_time_day_hour, self.part_time_day_hour
            case _:  # Absent
                return 0, 0

    def calculate_monthly_wage(self):
        """
        Description:
            Calculates the total wage, total hours, total days, and daily wages for the month.

        Return:
            None
        """
        while self.total_days < self.max_working_days and self.total_hours < self.max_working_hours:
            attendance = self.check_attendance()
            daily_wage, hours_worked = self.calculate_employee_wage(attendance)
            self.daily_wages.append(daily_wage)
            self.total_wage += daily_wage
            self.total_hours += hours_worked
            self.total_days += 1


def main():
    companies = {
        "HCL": {"wage_per_hour": 20, "full_day_hour": 8, "part_time_day_hour": 4, "max_working_days": 20, "max_working_hours": 100},
        "TCS": {"wage_per_hour": 25, "full_day_hour": 8, "part_time_day_hour": 4, "max_working_days": 22, "max_working_hours": 120},
        "APEXON": {"wage_per_hour": 30, "full_day_hour": 8, "part_time_day_hour": 4, "max_working_days": 18, "max_working_hours": 90}
    }

    for company, params in companies.items():
        emp_wage_builder = EmpWageBuilder(company, params["wage_per_hour"], params["full_day_hour"],
                                           params["part_time_day_hour"], params["max_working_days"], params["max_working_hours"])
        emp_wage_builder.calculate_monthly_wage()

        # Print the results directly
        print(f"\nCalculating wages for {emp_wage_builder.company_name}:")
        print("Daily wages for each day of the month:")
        for day, wage in enumerate(emp_wage_builder.daily_wages, start=1):
            print(f"Day {day}: ${wage}")

        print(f"\nTotal wage for the month: {emp_wage_builder.total_wage}")
        print(f"Total working days: {emp_wage_builder.total_days}")
        print(f"Total working hours: {emp_wage_builder.total_hours}")

if __name__ == "__main__":
    main()
