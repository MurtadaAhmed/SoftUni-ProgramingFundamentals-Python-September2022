command = input()
to_do_list = [0 for x in range(10)]

while command != "End":
    split_command = command.split("-")  # ["2", "Walk the dog"]
    index = int(split_command[0]) - 1  # it is (-1) because according to the task, the indexes of the elements are
    # starting from one, while the index in the list is starting from zero, so we have to use -1 to equalizes it with
    # the indexes of the list
    to_do_order = split_command[1]
    to_do_list.pop(index)  # removing the zero from the list
    to_do_list.insert(index, to_do_order)  # inserting the specific order at the given index
    command = input()

to_do_list_without_zeros = [x for x in to_do_list if x != 0]

print(to_do_list_without_zeros)
