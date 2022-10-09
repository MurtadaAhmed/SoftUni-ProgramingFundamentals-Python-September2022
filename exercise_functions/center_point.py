# math.sqrt() to get the square root
# the idea is to calculate the digonal lenth of each resulting rectangle, and then we compare the 2 results to see
# which one is bigger

from math import sqrt, floor # to get the square root in line 9 and 10


def distance_calculator(x1, y1, x2, y2):
    first_digonal_length = sqrt(x1 ** 2 + y1 ** 2)
    second_digonal_length = sqrt(x2 ** 2 + y2 ** 2)
    if first_digonal_length <= second_digonal_length:
        print(f"({int(x1)}, {int(y1)})")
    else:
        print(f'({int(x2)}, {int(y2)})')


x1 = floor(float(input()))
y1 = floor(float(input()))
x2 = floor(float(input()))
y2 = floor(float(input()))

distance_calculator(x1, y1, x2, y2)