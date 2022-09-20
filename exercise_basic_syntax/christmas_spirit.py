# 1. get the input for the quantity_of_decoration and days_left.
# 2.enter the values from the table for the price and the points for each decoration.
# 3.create empty variables for total_cost and total_points (required to be printed in the end).
# 4.for loop based on the days left:
# ** if current_day % 11 == 0 >> increase quantity_of_decoration + 2 (this has to be the first condition
# as the quantity will affect the result from the other conditions below)
# a - if current_day % 2 == 0 >> add the price * quantity /points for ornament  to the variables in 2.
# b - if current_day % 3 == 0 >> add the price * quantity /points for Skirt + Garland  to the variables in 2.
# c - if current_day % 5 == 0 >> add the price * quantity /points for Lights  to the variables in 2:
# -- if this days is also current_day % 3 == 0 >> increase points + 30.
# d- if current_day % 10 == 0 >> lose points - 20
# + add (the price of one) to the varialbe of each skirt, garlands, and lights.
# 5.outside the for loop, check if the last day is 10th:
# - if so >> decrese points - 30.
# 6.print:
# "Total cost: {total_cost}"
# "Total spirit: {total_points}"

# 1
quantity_of_decoration = int(input())
days_left = int(input())
# 2
ornament_price = 2
ornament_points = 5
skirt_price = 5
skirt_points = 3
garland_price = 3
garland_points = 10
lights_price = 15
lights_points = 17
# 3
total_cost = 0
total_points = 0
# 4
for current_day in range(1, days_left + 1):
    if current_day % 11 == 0:  # **
        quantity_of_decoration += 2
    if current_day % 2 == 0: #a
        total_cost += ornament_price * quantity_of_decoration
        total_points += ornament_points
    if current_day % 3 == 0:  #b
        total_cost += (skirt_price + garland_price) * quantity_of_decoration
        total_points += skirt_points + garland_points
    if current_day % 5 == 0:  #c
        total_cost += lights_price * quantity_of_decoration
        total_points += lights_points
        if current_day % 3 == 0:
            total_points += 30
    if current_day % 10 == 0:  #d
        total_points -= 20
        total_cost += skirt_price + garland_price + lights_price
#5
if days_left % 10 == 0:
    total_points -= 30
#6
print(f"Total cost: {total_cost}\nTotal spirit: {total_points}")
