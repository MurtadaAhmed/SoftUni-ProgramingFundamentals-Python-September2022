list_of_numbers = input().split()
list_of_integers = list(map(int, list_of_numbers))
print(f"The minimum number is {min(list_of_integers)}")
print(f"The maximum number is {max(list_of_integers)}")
print(f"The sum number is: {sum(list_of_integers)}")