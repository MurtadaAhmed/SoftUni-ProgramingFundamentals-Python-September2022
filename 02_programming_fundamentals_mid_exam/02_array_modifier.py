list_of_values = input().split()
list_of_values_as_integers = [int(number) for number in list_of_values]
command = input()
while command != "end":
    command_as_list = command.split()
    if "swap" in command:
        index_1 = int(command_as_list[1])
        index_2 = int(command_as_list[2])
        current_first_element = list_of_values_as_integers[index_1]
        current_second_element = list_of_values_as_integers[index_2]
        list_of_values_as_integers[index_1] = current_second_element
        list_of_values_as_integers[index_2] = current_first_element
    elif "multiply" in command:
        index_1 = int(command_as_list[1])
        index_2 = int(command_as_list[2])
        list_of_values_as_integers[index_1] *= list_of_values_as_integers[index_2]
    elif "decrease" in command:
        for index, number in enumerate(list_of_values_as_integers):
            list_of_values_as_integers[index] -= 1
    command = input()
list_of_values_as_strings = [str(number) for number in list_of_values_as_integers]
print(", ".join(list_of_values_as_strings))