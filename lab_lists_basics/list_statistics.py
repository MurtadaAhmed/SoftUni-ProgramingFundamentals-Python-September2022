number_of_inputs = int(input())
list_of_positive_numbers = []
list_of_negative_numbers = []

for number in range(number_of_inputs):
    current_number = int(input())
    if current_number >= 0:
        list_of_positive_numbers.append(current_number)
    else:
        list_of_negative_numbers.append(current_number)

print(f"{list_of_positive_numbers}\n{list_of_negative_numbers}")
print(f"Count of positives: {len(list_of_positive_numbers)}")
print(f"Sum of negatives: {sum(list_of_negative_numbers)}")