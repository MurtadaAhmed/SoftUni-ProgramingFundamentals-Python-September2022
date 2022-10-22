numbers = input().split(", ")
indices_of_even_numbers = []
for index, number in enumerate(numbers):
    if int(number) % 2 == 0:
        indices_of_even_numbers.append(int(index))
print(indices_of_even_numbers)
