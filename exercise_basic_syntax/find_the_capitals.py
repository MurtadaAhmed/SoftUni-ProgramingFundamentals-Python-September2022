# 1.get the input.
# 2.create an empty list, where we gonna add the indexes of the capital letters
# 2.for loop through the length of the string from the input:
# - for each iteration, check if the current letter is capital (using .isupper()),
# and add its index to the list using append.
# 3.print the list.

# 1
string = input()
# 2
list_of_capital_indexes = []
# 3
for index in range(len(string)):
    if string[index].isupper():
        list_of_capital_indexes.append(index)
# 4
print(list_of_capital_indexes)