'''
@Author: Jayesh Patil
@Date: 2024-08-24
@Last Modified by: Jayesh Patil
@Title: Employee Wage Program for Multiple Companies
'''
import random

class Employeewage:
    @classmethod
    def check_attendance(cls):
        """
        Description:
            Randomly selects from a list to check if the employee is present, part-time, or absent.
            0 for absent, 1 for full-time, 2 for part-time.

        Parameters:
            None

        Return:
            int: Returns 0, 1, or 2 to indicate absence, full-time, or part-time, respectively.
        """
        attendance_list = [0, 1, 2]
        random.shuffle(attendance_list)
        return attendance_list[0]

    @classmethod
    def calculate_employee_wage(cls, wage_per_hour, full_day_hour, part_time_day_hour, attendance):
        """
        Description:
            Calculates the daily wage and hours worked based on attendance and company-specific parameters.

        Parameters:
            wage_per_hour (int): The wage per hour for the employee.
            full_day_hour (int): The number of hours for a full day of work.
            part_time_day_hour (int): The number of hours for a part-time day of work.
            attendance (int): 0 for absent, 1 for full-time, 2 for part-time.

        Return:
            tuple: Returns a tuple containing the daily wage (int) and hours worked (int).
        """
        match attendance:
            case 1:
                return wage_per_hour * full_day_hour, full_day_hour
            case 2:
                return wage_per_hour * part_time_day_hour, part_time_day_hour
            case _:
                return 0, 0

    @classmethod
    def calculate_monthly_wage(cls, wage_per_hour, full_day_hour, part_time_day_hour, max_working_days, max_working_hours):
        """
        Description:
            Calculates the total wage, total hours, total days, and daily wages for the month for a specific company.

        Parameters:
            wage_per_hour (int): The wage per hour for the employee.
            full_day_hour (int): The number of hours for a full day of work.
            part_time_day_hour (int): The number of hours for a part-time day of work.
            max_working_days (int): The maximum number of working days in the month.
            max_working_hours (int): The maximum number of working hours in the month.

        Return:
            tuple: Returns a tuple containing total wage (int), total hours (int), total days (int), and a list of daily wages (list of int).
        """
        total_wage = 0
        total_hours = 0
        total_days = 0
        daily_wages = []

        while total_days < max_working_days and total_hours < max_working_hours:
            attendance = cls.check_attendance()
            daily_wage, hours_worked = cls.calculate_employee_wage(wage_per_hour, full_day_hour, part_time_day_hour, attendance)
            daily_wages.append(daily_wage)
            total_wage += daily_wage
            total_hours += hours_worked
            total_days += 1

        return total_wage, total_hours, total_days, daily_wages

def main():
   
    companies = {
        "HCL": {"wage_per_hour": 20, "full_day_hour": 8, "part_time_day_hour": 4, "max_working_days": 20, "max_working_hours": 100},
        "TCS": {"wage_per_hour": 25, "full_day_hour": 8, "part_time_day_hour": 4, "max_working_days": 22, "max_working_hours": 120},
        "APEXON": {"wage_per_hour": 30, "full_day_hour": 8, "part_time_day_hour": 4, "max_working_days": 18, "max_working_hours": 90}
    }

    for company, params in companies.items():
        print(f"\nCalculating wages for {company}:")
        total_wage, total_hours, total_days, daily_wages = Employeewage.calculate_monthly_wage(
            params["wage_per_hour"],
            params["full_day_hour"],
            params["part_time_day_hour"],
            params["max_working_days"],
            params["max_working_hours"]
        )
        print(f"Daily wages: {daily_wages}")
        print(f"Total wage for the month: {total_wage}")
        print(f"Total working days: {total_days}")
        print(f"Total working hours: {total_hours}")

if __name__ == "__main__":
    main()
