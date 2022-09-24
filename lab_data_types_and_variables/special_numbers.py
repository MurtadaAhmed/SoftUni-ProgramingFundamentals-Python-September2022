range_of_numbers = int(input())

for number in range(1, range_of_numbers + 1):  # we start from 1 as per the task
    sum_of_digits = 0  # will sum the digits of the current number
    number_as_string = str(number) # converted to string, so we can loop through its length (number of digits) using for
    for digit in range(len(number_as_string)):  # looping through the digits of each number
        sum_of_digits += int(number_as_string[digit])  # adding the current digit to the sum
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f"{number} -> True")
    else:
        print(f"{number} -> False")