# 1.receive the input
# 2.create boolean voldemort_is_mentioned = False
# 3.while loop, while command != Welcome!:
# if condition, if commend == Voldemort:
# -print the statement, change voldemort_is_mentioned to true and break the loop
# else:
# -if len(command) <5
# -elif == 5 , and print the statement
# -elif ==6 , and print the statement
# elif >6 , and print the statement
# 4.outside while loop, if condition to check voldemort_is_mentioned is false:
# -print("Welcome to Hogwarts.")
# 1
command = input()
# 2
voldemort_is_mentioned = False
# 3
while command != "Welcome!":
    if command == "Voldemort":
        print("You must not speak of that name!")
        voldemort_is_mentioned = True
        break
    else:
        if len(command) < 5:
            print(f"{command} goes to Gryffindor.")
        elif len(command) == 5:
            print(f"{command} goes to Slytherin.")
        elif len(command) == 6:
            print(f"{command} goes to Ravenclaw.")
        elif len(command) > 6:
            print(f"{command} goes to Hufflepuff.")
    command = input()
# 4
if not voldemort_is_mentioned:
    print("Welcome to Hogwarts.")