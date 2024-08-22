'''

@Author: Jayesh Patil
@Date: 2024-08-22
@Last Modified by: Jayesh Patil
@Title: Employee Wage Program


'''
import random
def Check_Attendance():
    """
    Description:
        Randomly selects from a list to check if the employee is present or not.
        If 0, the employee is absent; if 1, the employee is present.

    Parameter:
        None

    Return:
        Returns 0 or 1 to indicate absence or presence, respectively.
    """   

    attendance_list = [0, 1]
    random.shuffle(attendance_list) 
    return attendance_list[0]

def main():
    print("Welcome to Employee Wage Program ")
    attendance = Check_Attendance()
    if attendance == 1:
        print("Employee is Present ")
    else:
        print("Employee is Absent ")

if __name__ == "__main__":
    main()
            

