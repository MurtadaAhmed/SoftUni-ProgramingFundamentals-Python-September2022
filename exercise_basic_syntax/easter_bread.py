# 1.receive the input for budget and the price for flour.
# 2.price for egg is 0.75 * price of flour.
# 3.price for liter milk is 1.25 * price of flour, then divide it by 4 to get it for 0.250 l milk
# 4.claculate the price for one loaf = flour + egg + milk 0.250 l
# 5.calcualate how many loaves we can make with this budget by dividing budget / price of one loaf (int)
# 6.create a variable for colorred egg = 0
# 7.create for loop, for the number of the loaves we have:
# - for every iteration, colorred egg + 3
# - for every 3rd iteration: colorred egg + 3 and also lose the colorred eggs with the amount ({current_bread_count} - 2)
# 8.outside for loop, calculate the price of the made loaves, and subtract it from the budget to get the money left,
# then print:
#     "You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left}BGN left."
# formatted to the second decimal

# 1
budget = float(input())
flour_price = float(input())
# 2
egg_price = 0.75 * flour_price
# 3
milk_250_price = (1.25 * flour_price) / 4
# 4
price_one_loaf = flour_price + egg_price + milk_250_price
# 5
number_of_loaves = int(budget/price_one_loaf)
# 6
colored_eggs = 0
# 7
for current_loaf_count in range(1, number_of_loaves + 1):
    colored_eggs += 3
    if current_loaf_count % 3 == 0:
        colored_eggs -= current_loaf_count - 2
# 8
price_of_made_loaves = number_of_loaves * price_one_loaf
money_left = budget - price_of_made_loaves
print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")