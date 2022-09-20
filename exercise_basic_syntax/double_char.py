# 1.receive the input command.
# 2.while loop while command != "End"
# -check if the command != "SoftUni":
# --create a an empty string new_string
# --for loop based on the commaned:
# ---in eact iterarion, current letter * 2
# ---add it to the new_string
# --outside for loop, print the new_string
# -outside the if command, take the input again

command = input()
while command != "End":
    if command != "SoftUni":
        new_string = ""
        for letter in command:
            new_string += letter * 2
        print(new_string)
    command = input()