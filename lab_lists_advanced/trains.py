number_of_wagons = int(input())
train = [0 for x in range(number_of_wagons)]
command = input()

while command != "End":  # add 20
    split_command = command.split()  # ["add", "20"]

    if "add" in split_command:  # ["add", "20"]
        people = int(split_command[1])
        train[-1] += people  # adding them in the last wagon
    elif "insert" in split_command:  # ["insert", "0", "15"]
        index = int(split_command[1])
        people = int(split_command[2])
        train[index] += people
    elif "leave" in split_command:  # ["leave", "0", "5"]
        index = int(split_command[1])
        people = int(split_command[2])
        train[index] -= people
    command = input()

print(train)
