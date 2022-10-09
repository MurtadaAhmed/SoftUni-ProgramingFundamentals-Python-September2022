list_of_numbers = input().split()
list_of_numbers_as_integers = list(map(int, list_of_numbers))
number_of_loops = int(input())
for loop in range(number_of_loops):
    current_smallest_number = min(list_of_numbers_as_integers)  # finding the current smallest number in the list
    list_of_numbers_as_integers.remove(current_smallest_number)  # removing the current smallest number from the list

# converting the int list into str list:
list_converted_into_strings = []
for number in range(len(list_of_numbers_as_integers)):
    list_converted_into_strings.append(str(list_of_numbers_as_integers[number]))

# printing the str list as str
print(", ".join(list_converted_into_strings))