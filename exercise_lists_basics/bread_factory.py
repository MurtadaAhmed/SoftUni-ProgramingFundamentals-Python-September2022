commands_values = input().split("|")  # ['rest-2', 'order-10', 'eggs-100', 'rest-10']
energy = 100
coins = 100
bakery_is_open = True  # will be changed inside for loop if we gonna beak the loop
for command_value in commands_values:
    command_value_split = command_value.split("-")  # ["rest", "2"]
    command = command_value_split[0]  # "rest"
    value = int(command_value_split[1])  # 2

    if command == "rest":
        current_energy = energy
        energy += value
        if energy > 100:
            energy = 100  # it should not exceed 100
        difference = energy - current_energy  # the earned amount (if any)
        print(f"You gained {difference} energy.")
        print(f"Current energy: {energy}.")

    elif command == "order":

        if energy >= 30:
            energy -= 30
            coins += value
            print(f"You earned {value} coins.")
        else:
            energy += 50
            if energy > 100:
                energy = 100  # because is should not exceed 100
            print("You had to rest!")

    else:
        if coins >= value:
            coins -= value
            print(f"You bought {command}.")
        else:
            bakery_is_open = False
            print(f"Closed! Cannot afford {command}.")
            break

if bakery_is_open:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")