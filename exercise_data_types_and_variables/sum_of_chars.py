number_of_lines = int(input())
sum_of_char = 0
for char in range(number_of_lines):
    character = input()
    sum_of_char += ord(character)
print(f"The sum equals: {sum_of_char}")