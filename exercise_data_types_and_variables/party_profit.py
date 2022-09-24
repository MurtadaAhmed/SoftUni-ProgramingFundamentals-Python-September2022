from math import floor
group_size = int(input())
days_of_adventure = int(input())
coins = 0
for day in range(1, days_of_adventure + 1):

    if day % 10 == 0:  # has to be in beginning as it affect group size
        group_size -= 2
    if day % 15 == 0:
        group_size += 5  # has to be in beginning as it affect group size
    if day % 3 == 0:
        coins -= 3 * group_size
    if day % 5 == 0:
        coins += 20 * group_size
        if day % 3 == 0:
            coins -= 2 * group_size
    coins += 50  # earning every day
    coins -= 2 * group_size  # has to be in the end, as the first 2 conditions are affecting group size, and this value
    # depend on the group size
coins_per_companion = floor(coins / group_size)
print(f"{group_size} companions received {coins_per_companion} coins each.")