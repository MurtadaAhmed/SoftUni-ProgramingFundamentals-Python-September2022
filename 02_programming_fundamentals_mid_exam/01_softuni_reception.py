current_hour_count = 0
first_employee_ability_per_hour = int(input())
second_employee_ability_per_hour = int(input())
third_employee_ability_per_hour = int(input())
number_of_students = int(input())
students_per_hour = first_employee_ability_per_hour + \
        second_employee_ability_per_hour + \
        third_employee_ability_per_hour
while number_of_students:  # while students are waiting
    current_hour_count += 1
    if current_hour_count % 4 != 0:  # because at every 4 th hour there is break
        if number_of_students >= students_per_hour:  # means the number of students waiting are bigger than current
            # employees ability
            number_of_students -= students_per_hour
        else:  # if students waiting are less than the capacity, means the employees will be able to handle them all
            # and their count will become 0
            number_of_students = 0
print(f"Time needed: {current_hour_count}h.")
