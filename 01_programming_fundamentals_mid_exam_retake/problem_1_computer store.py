total_price_without_taxes = 0
total_price_with_taxes = 0
taxes = 0
# in the next while loop, we gonna filter the valid prices, and add them to the total price
while True:
    command = input()  # could be a price or "regular" or "special"
    if command == "regular" or command == "special":
        break
    price = float(command)  # converting the command into float as it is a price
    if price <= 0:
        print("Invalid price!")
        continue  # take the next iteration without proceeding with the steps below
    total_price_without_taxes += price  # adding the current price to the total
    total_price_with_taxes += price * 1.20
    taxes += price * 0.20
if total_price_with_taxes == 0:
    print("Invalid order!")
else:  # if total_price_with_taxes > 0
    if command == "special":
        total_price_with_taxes = total_price_with_taxes * 0.90
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price_without_taxes:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price_with_taxes:.2f}$")