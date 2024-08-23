'''
@Author: Jayesh Patil
@Date: 2024-08-23
@Last Modified by: Jayesh Patil
@Title: Employee Wage Program
'''
import random

class Employeewage:
    # Constants
    WAGE_PER_HOUR = 20
    FULL_DAY_HOUR = 8
    PART_TIME_DAY_HOUR = 4
    MAX_WORKING_DAYS = 20
    MAX_WORKING_HOURS = 100

    def __init__(self):
        """
        Description:
            Initializes the Employeewage class with total wage, hours, days, and daily wages.

        Parameters:
            None

        Return:
            None
        """
        self.total_wage = 0
        self.total_hours = 0
        self.total_days = 0
        self.daily_wages = []

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
    def calculate_employee_wage(cls, attendance):
        """
        Description:
            Calculates the daily wage and hours worked based on attendance.

        Parameters:
            attendance (int): 0 for absent, 1 for full-time, 2 for part-time.

        Return:
            tuple: Returns a tuple containing the daily wage (int) and hours worked (int).
        """
        match attendance:
            case 1:
                return cls.WAGE_PER_HOUR * cls.FULL_DAY_HOUR, cls.FULL_DAY_HOUR
            case 2:
                return cls.WAGE_PER_HOUR * cls.PART_TIME_DAY_HOUR, cls.PART_TIME_DAY_HOUR
            case _:
                return 0, 0

    def calculate_monthly_wage(self):
        """
        Description:
            Calculates the total wage, total hours, total days, and daily wages for the month.

        Parameters:
            None

        Return:
            tuple: Returns a tuple containing total wage (int), total hours (int),
                   total days (int), and a list of daily wages (list of int).
        """
        while self.total_days < self.MAX_WORKING_DAYS and self.total_hours < self.MAX_WORKING_HOURS:
            attendance = self.check_attendance()
            daily_wage, hours_worked = self.calculate_employee_wage(attendance)
            self.daily_wages.append(daily_wage)
            self.total_wage += daily_wage
            self.total_hours += hours_worked
            self.total_days += 1
        return self.total_wage, self.total_hours, self.total_days, self.daily_wages

def main():

    print("Welcome to Employee Wage Program")
    employee_wage = Employeewage()
    total_wage, total_hours, total_days, daily_wages = employee_wage.calculate_monthly_wage()
    print(f"Daily wages for each day of the month: {daily_wages}")
    print(f"\nTotal wage for the month is {total_wage}.")
    print(f"Total working days: {total_days}")
    print(f"Total working hours: {total_hours}")

if __name__ == "__main__":
    main()
