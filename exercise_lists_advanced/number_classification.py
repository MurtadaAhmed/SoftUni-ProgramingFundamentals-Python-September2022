list_of_numbers = list(map(int, input().split(", ")))
positive_numbers = [number for number in list_of_numbers if number >= 0]
negative_numbers = [number for number in list_of_numbers if number < 0]
even_numbers = [number for number in list_of_numbers if number % 2 == 0]
odd_numbers = [number for number in list_of_numbers if number % 2 != 0]

positive_numbers_strings = list(map(str, positive_numbers))
negative_numbers_strings = list(map(str, negative_numbers))
even_numbers_string = list(map(str, even_numbers))
odd_numbers_string = list(map(str, odd_numbers))



print(f'Positive: {", ".join(positive_numbers_strings)}')
print(f'Negative: {", ".join(negative_numbers_strings)}')
print(f'Even: {", ".join(even_numbers_string)}')
print(f'Odd: {", ".join(odd_numbers_string)}')