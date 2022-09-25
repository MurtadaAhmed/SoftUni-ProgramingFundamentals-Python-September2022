sequence_of_numbers = input().split()
sequence_of_numbers_as_integers = [int(number) for number in sequence_of_numbers] # converted to int so we can get the
# sum and the average number
sum_of_numbers = sum(sequence_of_numbers_as_integers)
count_of_numbers = len(sequence_of_numbers_as_integers)
average_number = sum_of_numbers / count_of_numbers
list_of_big_numbers = []  # where we gonna store the biggest numbers
sequence_of_numbers_as_integers_sorted = sorted(sequence_of_numbers_as_integers, reverse=True)  # we arrange it in
# descending order, so that in the next loop we can start looping from the biggest ones, and then append the top 5
# biggest ones in list_of_big_numbers
for number in sequence_of_numbers_as_integers_sorted:
    if number > average_number:
        list_of_big_numbers.append(number)
        if len(list_of_big_numbers) == 5:  # if we get the biggest 5 numbers, we break the loop
            break

if list_of_big_numbers:
    list_as_string = [str(number) for number in list_of_big_numbers] # converted to str list so we can use .join below
    print(" ".join(list_as_string))
else:  # when we don't have biggest numbers (means the list_of_big_numbers is empty_
    print("No")