# 1.read the number_of_order
# 2.create variable total_price
# 3.create for loop for the number of the orders
# 3.for each iteration, we receive the following inputs:
# price_per_capsule
# days
# capsules_per_day
# *if condition to check if the inputs are within the reange
# -if the inputs are within the range:
# >>calculate the price by multiplying the inputs
# >>add the current price to total_price
# >> print "The price for the coffee is: ${price}"
#
# 4.outside the for loop print the totatl price:
# "Total: ${total_price}"
number_of_orders = int(input())
total_price = 0
for order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules_per_day < 1 or  capsules_per_day > 2000:
        continue
    price = price_per_capsule * days* capsules_per_day
    total_price += price
    print(f"The price for the coffee is: ${price:.2f}")
print(f"Total: ${total_price:.2f}")