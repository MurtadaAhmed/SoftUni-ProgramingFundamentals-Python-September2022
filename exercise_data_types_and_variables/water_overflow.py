number_of_fills = int(input())
capacity = 255
filled_amount = 0
for i in range(number_of_fills):
    one_fill = int(input())
    if capacity >= one_fill:  # means there is still capacity
        capacity -= one_fill
        filled_amount += one_fill
    else:
        print("Insufficient capacity!")
print(filled_amount)