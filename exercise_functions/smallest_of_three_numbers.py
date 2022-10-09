def smallest_number(num1, num2, num3):
    list_of_numbers = [num1, num2, num3]
    smallest_num = min(list_of_numbers)
    return smallest_num


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(smallest_number(first_number, second_number, third_number))
