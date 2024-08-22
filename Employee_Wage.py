'''

@Author: Jayesh Patil
@Date: 2024-08-22
@Last Modified by: Jayesh Patil
@Title: Employee Wage Program


'''
import random

WAGE_PER_HOUR = 20
FULL_DAY_HOUR = 8
PART_TIME_DAY_HOUR = 4
WORKING_DAYS_PER_MONTH = 20

def check_attendance():
    """
        Description:
            Randomly selects from a list to check if the employee is present, part-time, or absent.
            0 for absent, 1 for full-time, 2 for part-time.

        Parameter:
            None

        Return:
            Returns 0, 1, or 2 to indicate absence, full-time, or part-time, respectively.
    """   

    attendance_list = [0, 1,2]
    random.shuffle(attendance_list) 
    return attendance_list[0]

def calculate_employee_wage(attendance):
    """
        Description:
            Calculate daily wage based on attendance.
            Uses global constants for wage per hour and hours per day.

        Parameters:
            attendance (int): Indicates whether the employee is absent (0), full-time (1), or part-time (2).

        Return:
            A tuple containing the calculated wage and the number of hours worked.
    """

    if attendance == 1:
        return WAGE_PER_HOUR * FULL_DAY_HOUR
    elif attendance == 2:
        return WAGE_PER_HOUR * PART_TIME_DAY_HOUR    
    else:
        return 0    

def calculate_monthly_wage():
    """
        Description:
            Calculate the monthly wage based on 20 working days and the employee's attendance.
            Store each day's wage in a list.

        Parameter:
            None

        Return:
            A containing the total wage for the month and the list of daily wages.
    """
    total_wage = 0
    daily_wages = []

    for day in range(WORKING_DAYS_PER_MONTH):
        attendance = check_attendance()
        daily_wage = calculate_employee_wage(attendance)
        daily_wages.append(daily_wage)
        total_wage += daily_wage

    return total_wage, daily_wages

def main():
    print("Welcome to Employee Wage Program")
    total_wage, daily_wages = calculate_monthly_wage()
    
    print(f"Daily wages for each day of the month:{daily_wages}")
    print(f"Total wage for the month is {total_wage}.")

if __name__ == "__main__":
    main()

