# 1.get the input
# 2.create an empty list, where we gonna add each single digit there separately.
# 3.loop through the length of the string from the input:
# - for each iteration, take the digit in the current index , and add it to the list.
# this way we add all the digits in the list
# 4.sort the list using the sort with (Reverse) to arrange the list in descending order (as required by the task).
# 5.print the sorted list as string using .join

# 1
number = input()
# 2
numbers_in_list = []
# 3
for digit_index in range(len(number)):
    numbers_in_list.append(number[digit_index])
# 4
numbers_in_list.sort(reverse=True)
# 5
print("".join(numbers_in_list))