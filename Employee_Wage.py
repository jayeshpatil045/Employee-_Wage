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

def check_attendance():
    """
        Description:
            Randomly selects from a list to check if the employee is present or not.
            If 0, the employee is absent; if 1, the employee is present.

        Parameter:
            None

        Return:
            Returns 0 or 1 to indicate absence or presence, respectively.
    """   

    attendance_list = [0, 1,2]
    random.shuffle(attendance_list) 
    return attendance_list[0]

def calculate_daily_employee_wage():
    """

        Description:
            Calculate Employee Daily wages, wage per hour is 20 and full day hour is 8. 

        Parameter:
            None

        Return:
            Multiplication of wage per hour and full day hours.


    """
    return WAGE_PER_HOUR * FULL_DAY_HOUR

def part_time_employee_daily_wage():
    """

        Description:
            Calculate Daily wages for part time employee, wage per hour is 20 and haugh day hour is 4. 

        Parameter:
            None

        Return:
            Multiplication of part time day hours and wage per hour.

    """
    return PART_TIME_DAY_HOUR * WAGE_PER_HOUR

def main():
    print("Welcome to Employee Wage Program")
    attendance = check_attendance()
    if attendance == 1:
         print(f"Your daily wages is {calculate_daily_employee_wage()}.")
    elif attendance == 2:
        print(f"Employee Part time daily wage is {part_time_employee_daily_wage()}")     
    else:
        print("Employee is Absent ")

if __name__ == "__main__":
    main()
            

