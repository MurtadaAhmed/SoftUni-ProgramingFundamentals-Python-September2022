list_of_sums = input().split(", ")
list_of_sums_as_integers = list(map(int, list_of_sums))  # converting the list into integers
number_of_beggars = int(input())
final_list = []  # where we gonna put the sums for each beggar
current_beggar_index = 0  # will be increased after each while loop, to move from one beggar to another
while current_beggar_index < number_of_beggars:  # to loop through all the beggars
    current_beggar_sum = 0  # current beggar sum, will increase after each for loop
# next step explanation: the for loop will loop through the list_of_sums_as_integers, starting from the index of the
    # current beggar, ending by the length of the list, and the step is the number of the beggars
    for index in range(current_beggar_index, len(list_of_sums_as_integers), number_of_beggars):
        current_beggar_sum += list_of_sums_as_integers[index]
    final_list.append(current_beggar_sum)  # adding the sum of the current beggar to the final list
    current_beggar_index += 1  # increased by one so we can loop through the next beggar
print(final_list)