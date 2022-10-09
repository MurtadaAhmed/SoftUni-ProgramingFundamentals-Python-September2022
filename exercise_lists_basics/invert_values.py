numbers = input()
numbers_as_list = list(map(int, numbers.split()))  # str converted into str list, and then into int list
for number_index in range(len(numbers_as_list)):
    numbers_as_list[number_index] = numbers_as_list[number_index] * -1
print(numbers_as_list)