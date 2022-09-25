sequence_of_elements = input().split()
command = input()
number_of_moves = 0
while command != "end":  # means indexes
    indexes = list(map(int, command.split()))  # getting the indexes as list of int
    first_index = indexes[0]
    second_index = indexes[1]

    length_of_elements = len(sequence_of_elements)
    if first_index == second_index or \
            first_index < 0 or second_index < 0 or \
            first_index >= length_of_elements or second_index >= length_of_elements:
        print("Invalid input! Adding additional elements to the board")
        number_of_moves += 1
        middle_of_list = int(length_of_elements / 2)
        sequence_of_elements.insert(middle_of_list, "-" + str(number_of_moves) + "a")
        sequence_of_elements.insert(middle_of_list, "-" + str(number_of_moves) + "a")
    elif sequence_of_elements[first_index] == sequence_of_elements[second_index]:
        number_of_moves += 1
        print(f"Congrats! You have found matching elements - {sequence_of_elements[first_index]}!")
        element_to_be_removed = sequence_of_elements[first_index]
        first_element_removed = sequence_of_elements.remove(element_to_be_removed)
        second_element_removed = sequence_of_elements.remove(element_to_be_removed)

    elif sequence_of_elements[first_index] != sequence_of_elements[second_index]:
        print("Try again!")
    if len(sequence_of_elements) == 0:  # when there are no elements left
        print(f"You have won in {number_of_moves} turns!")
        break  # to break the loop

    command = input()
if sequence_of_elements:
    print("Sorry you lose :(")
    print(" ".join(sequence_of_elements))
