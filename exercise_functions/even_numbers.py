
numbers = input().split(" ")
integer_list = list(map(int, numbers))  # converting the list into int
even_nums = list(filter(lambda x: x % 2 == 0, integer_list))
print(even_nums)
