list_of_cards = input().split()  # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
number_of_shuffles = int(input())
middle_of_cards = len(list_of_cards) // 2  # 4

for shuffle in range(number_of_shuffles):
    current_shuffle = []  # the result of the current shuffle will be added here
    first_half_of_cards = list_of_cards[0:middle_of_cards]  # ['a', 'b', 'c', 'd']
    second_half_of_cards = list_of_cards[middle_of_cards:]  # ['e', 'f', 'g', 'h']
# explanation for the next step: we loop with the length of any half (as they are equals). In each loop we add elements
    # of current index for each halves to the current_shuffle
    for i in range(len(first_half_of_cards)):
        current_shuffle.append(first_half_of_cards[i])
        current_shuffle.append(second_half_of_cards[i])
    list_of_cards = current_shuffle  # we make the original list equal to the current shuffle, so we can continue with
    # the next shuffle
print(list_of_cards)