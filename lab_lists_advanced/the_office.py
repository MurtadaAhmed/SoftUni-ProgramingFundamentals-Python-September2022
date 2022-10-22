employees_happiness = input().split()
factor = int(input())
employees_happiness_multiplied = [int(x) * factor for x in employees_happiness]
number_of_employees = len(employees_happiness)
average_happiness = sum(employees_happiness_multiplied) / number_of_employees
happy_employees = list(filter(lambda x: x >= average_happiness, employees_happiness_multiplied))

if len(happy_employees) >= (number_of_employees / 2):

    print(f"Score: {len(happy_employees)}/{number_of_employees}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{number_of_employees}. Employees are not happy!")
