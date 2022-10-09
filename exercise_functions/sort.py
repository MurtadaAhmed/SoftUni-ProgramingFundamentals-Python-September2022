list_of_numbers = input().split()
list_of_integers = list(map(int, list_of_numbers))
sorted_list = sorted(list_of_integers)
print(sorted_list)