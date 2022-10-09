from math import sqrt, floor


def distance_calculator(x1, y1, x2, y2, x3, y3, x4, y4):
    first_digonal_length = sqrt(x1 ** 2 + y1 ** 2)  # first diagonal length from the center
    second_digonal_length = sqrt(x2 ** 2 + y2 ** 2)  # second diagonal length from the center
    third_digonal_length = sqrt(x3 ** 2 + y3 ** 2) # third diagonal length from the center
    fourth_digonal_length = sqrt(x4 ** 2 + y4 ** 2) # fourth diagonal length from the center

    first_line = first_digonal_length + second_digonal_length
    second_line = third_digonal_length + fourth_digonal_length

    if first_line >= second_line:
        if first_digonal_length <= second_digonal_length:
            print(f"({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})")
        else:
            print(f'({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})')
    else:
        if third_digonal_length <= fourth_digonal_length:
            print(f"({floor(x3)}, {floor(y3)})({floor(x4)}, {floor(y4)})")
        else:
            print(f'({floor(x4)}, {floor(y4)})({floor(x3)}, {floor(y3)})')


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

# calling the first function:
distance_calculator(x1, y1, x2, y2, x3, y3, x4, y4)