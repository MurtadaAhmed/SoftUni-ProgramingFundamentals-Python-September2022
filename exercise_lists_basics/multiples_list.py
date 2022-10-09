factor = int(input())
count = int(input())
list_of_numbers = []
new_factor = factor  # will be changed with each iteration
for number in range(count):
    list_of_numbers.append(new_factor)
    new_factor += factor  # adding the factor value to the new factor
print(list_of_numbers)