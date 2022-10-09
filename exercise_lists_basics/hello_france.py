items_collection = input().split("|")
initial_budget = float(input())
profit = 0
train_ticket_price = 150
sum_all_new_prices = 0

for item in items_collection:  # ["Clothes->43.30", "Shoes->25.25"]
    single_item = item.split("->")  # ['Clothes', '43.30']
    item_name = single_item[0]
    item_price = float(single_item[1])
    if item_name == "Clothes":
        if item_price <= 50.00:
            if initial_budget >= item_price:
                initial_budget -= item_price
                new_item_price = item_price * 1.40
                profit += new_item_price - item_price
                sum_all_new_prices += new_item_price
                print(f"{new_item_price:.2f}", end=" ")

    elif item_name == "Shoes":
        if item_price <= 35.00:
            if initial_budget >= item_price:
                initial_budget -= item_price
                new_item_price = item_price * 1.40
                profit += new_item_price - item_price
                sum_all_new_prices += new_item_price
                print(f"{new_item_price:.2f}", end=" ")

    elif item_name == "Accessories":
        if item_price <= 20.50:
            if initial_budget >= item_price:
                initial_budget -= item_price
                new_item_price = item_price * 1.40
                profit += new_item_price - item_price
                sum_all_new_prices += new_item_price
                print(f"{new_item_price:.2f}", end=" ")

print()
print(f"Profit: {profit:.2f}")
final_budget = sum_all_new_prices + initial_budget
if final_budget >= train_ticket_price:
    print("Hello, France!")
else:
    print("Not enough money.")







# the second solution below gives the same result, but judge gives 0:


# items_received = input().split("|")  # ['Clothes->43.30', 'Shoes->25.25', 'Clothes->36.52', 'Clothes->20.90',
# # 'Accessories->15.60']
# budget = float(input())
# profit = 0
# items_new_prices_list = []
# train_ticket_cost = 150
# max_clothes_price = 50.00
# max_shoes_price = 35.00
# max_accessories_price = 20.50
#
# for current_item_price in items_received:  # Clothes->43.30
#     item_price_split = current_item_price.split("->")  # ['Clothes', '43.30']
#     price = float(item_price_split[1])  # 43.30
#     if "Clothes" in item_price_split:
#         if price <= max_clothes_price and price <= budget:
#             budget -= price  # removing the price from the budget
#             new_price = price * 1.40  # price of bought item increased by 40%
#             new_price_formatted = float(f"{new_price:.2f}")
#             items_new_prices_list.append(new_price_formatted)  # added to the list of new prices
#             profit += new_price - price  # profit we got from this buying/selling
#     elif "Shoes" in item_price_split:
#         if price <= max_shoes_price and price <= budget:
#             budget -= price  # removing the price from the budget
#             new_price = price * 1.40  # price of bought item increased by 40%
#             new_price_formatted = float(f"{new_price:.2f}")
#             items_new_prices_list.append(new_price_formatted)  # added to the list of new prices
#             profit += new_price - price  # profit we got from this buying/selling
#     elif "Accessories" in item_price_split:
#         if price <= max_accessories_price and price <= budget:
#             budget -= price  # removing the price from the budget
#             new_price = price * 1.40  # price of bought item increased by 40%
#             new_price_formatted = float(f"{new_price:.2f}")
#             items_new_prices_list.append(new_price_formatted)  # added to the list of new prices
#             profit += new_price - price  # profit we got from this buying/selling
# items_new_prices_list_as_strings = list(map(str, items_new_prices_list))
# print(" ".join(items_new_prices_list_as_strings))
# print(f"Profit: {profit:.2f}")
#
# final_budget = budget + sum(items_new_prices_list)
# if final_budget >= train_ticket_cost:
#     print("Hello, France!")
# else:
#     print("Not enough money.")
