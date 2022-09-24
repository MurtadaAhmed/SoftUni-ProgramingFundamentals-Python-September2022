number_of_lines = int(input())
last_input = ""  # will use this to find out the order of brackets
is_balanced = True  # will be changed to False if the condition is not met and to break the loop
for line in range(number_of_lines):
    command = input()
    if command not in ["(", ")"]:
        continue  # meaning that if it is random string, we read the next iteration
# now we will check we are starting with closing bracket, or if we are getting 2 opening brackets
    if (last_input == "" and command == ")") or last_input == command:
        is_balanced = False
        break
    last_input = command  # to compare the result in the next iteration
if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
