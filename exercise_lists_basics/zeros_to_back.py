command = input().split(", ")
count = 0

for i in command:
    if "0" in i:
        count += 1

while "0" in command and count > 0: # this ensure the loop will run for the number of zeros that we have in the list
    command.remove("0")
    command.append("0")
    count -= 1

integer_list = [int(a) for a in command]  # convert the str list into int list

print(integer_list)