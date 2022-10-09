product_name = input()
product_quantity = int(input())


def total_price(name, quantity):
    result = 0
    if name == "coffee":
        result = quantity * 1.50
    elif name == "water":
        result = quantity * 1.00
    elif name == "coke":
        result = quantity * 1.40
    elif name == "snacks":
        result = quantity * 2.00
    return result


final_result = total_price(product_name, product_quantity)
print(f"{final_result:.2f}")