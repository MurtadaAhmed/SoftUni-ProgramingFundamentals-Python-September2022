# 1.get the input for the first and second strings.
# 2.create a variable last_stringe, and make its value equal to the first string (will be used to comparision to avoid
# duplicates and to be update with value of every new sting to be compared with later).
# 3.for loop to loop through the len of any of the strings (as they are of equal lengths)
# - for each iteration, using slicing, take first string without the current index
# - for each iteration, using slicing, take the the second string till the current string
# - combine the two results above in a new string
# -if condition to check if the new string is equal to the variable created in #2:
# --if not, print the new string
# --if the same, ignore

# 1
first_string = input()
second_string = input()
# 2
last_string = first_string
# 3
for i in range(len(first_string)):
    first_part = first_string[i+1:]  # after the current index till the end of the string
    second_part = second_string[:i+1]  # from the beginning of the string till current string
    new_string = second_part + first_part
    if new_string != last_string:
        print(new_string)
        last_string = new_string
    else:
        continue
