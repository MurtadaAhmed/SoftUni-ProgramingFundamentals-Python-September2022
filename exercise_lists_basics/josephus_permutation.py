circle = input().split()  # [1,2,3,4,5,6,7]
kill_step = int(input())  # 3
result = []  # the final result with the executed people
counter = 0  # to know on which person we are (we start with 1 at the beginning of the loop)
# later we will use the if condition to see if we are on the third person
# if we reach to the end of the list, it will continue counting back from the beginning of the list

index = 0  # this is to know the current index that we are in, when the index become equal or more than the length of
# the list, we make it zero so we can go back to the beginning of the list
while len(circle) > 0:  # which means while we still have elements in the main list to loop through
    counter += 1  # person count number one

    if counter % kill_step == 0:  # to see if we are on the third person
        result.append(circle.pop(index))  # if we are on the third person, to add it in the new list (result) and remove
        # it from the main list (circle), we can find the specific element based on the current (index)
    else:
        index += 1  # to move to the next index if the person is not the third one

    if index >= len(circle):  # to know if we reach to the end of the list, we make the value 0, so we can go back to
        # the beginning of the list where the index is zero
        index = 0
print(result)
exit()
print(str(result).replace(" ", "").replace("'", ""))  # replace function works with strings, that is why we need to put
# str in the beginning.
# the first replace remove the empty spaces in the list, the second one remove the quotes from the list
# before we use the replace function above, the result is like this: ['3', '6', '2', '7', '5', '1', '4']
