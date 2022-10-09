numbers_sequence = input().split()  # ['29', '13', '9', '0', '13', '0', '21', '0', '14', '82', '12']
middle_number = int(len(numbers_sequence) / 2)  # 5 (the finish line index)
left_numbers = numbers_sequence[:middle_number]  # ['29', '13', '9', '0', '13']
right_numbers = numbers_sequence[-1:-(middle_number+1):-1]  # ['12', '82', '14', '0', '21']

sum_left_numbers = 0
sum_right_numbers = 0

for l_number in left_numbers:
    if l_number == "0":
        sum_left_numbers *= 0.80
    sum_left_numbers += int(l_number)

for r_number in right_numbers:
    if r_number == "0":
        sum_right_numbers *= 0.80
    sum_right_numbers += int(r_number)

if sum_left_numbers < sum_right_numbers:
    print(f"The winner is left with total time: {sum_left_numbers:.1f}")
else:
    print(f"The winner is right with total time: {sum_right_numbers:.1f}")
