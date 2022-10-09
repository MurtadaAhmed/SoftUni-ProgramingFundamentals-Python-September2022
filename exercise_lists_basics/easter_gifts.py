list_of_gifts = input().split()
command = input()
while command != "No Money":
    split_command = command.split()
    if "OutOfStock" in split_command:  # ["OutOfStock", "Eggs"]
        while split_command[1] in list_of_gifts:  # we use while because we need to replace all the elements
            index_of_element = list_of_gifts.index(split_command[1])  # getting the index of element
            list_of_gifts[index_of_element] = "None"  # replacing the element at that index with "None"
    elif "Required" in split_command:  # ["Required", "Spoon", "2"]
        if len(list_of_gifts) > int(split_command[2]) >= 0:  # checking if the index is valid
            list_of_gifts[int(split_command[2])] = split_command[1]  # replace element at the specific index with
            # the given gift
    elif "JustInCase" in split_command:  # ["JustInCase", "ChocolateEgg"]
        list_of_gifts.pop()
        list_of_gifts.append(split_command[1])
    command = input()

while "None" in list_of_gifts:  # removing "None"(s) from the list
    list_of_gifts.remove("None")

print(" ".join(list_of_gifts))  # printing the list as strings
