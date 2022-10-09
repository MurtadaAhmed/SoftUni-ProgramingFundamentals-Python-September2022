fire_level_cell_value = input(). split("#")  # ['High = 89', 'Low = 28', 'Medium = 77', 'Low = 23']
water_available = int(input())
effort_needed = 0
total_fire = 0
cells_put_out = []
for level_value in fire_level_cell_value:  # High = 89
    level_value_split = level_value.split(" = ")  # ['High', '89']
    fire_level = level_value_split[0]  # High
    cell_value = int(level_value_split[1])  # 89
    if fire_level == "High" and 81 <= cell_value <= 125:
        if water_available >= cell_value:
            water_available -= cell_value
            effort_needed += 0.25 * cell_value
            total_fire += cell_value
            cells_put_out.append(cell_value)
    elif fire_level == "Medium" and 51 <= cell_value <= 80:
        if water_available >= cell_value:
            water_available -= cell_value
            effort_needed += 0.25 * cell_value
            total_fire += cell_value
            cells_put_out.append(cell_value)
    elif fire_level == "Low" and 1 <= cell_value <= 50:
        if water_available >= cell_value:
            water_available -= cell_value
            effort_needed += 0.25 * cell_value
            total_fire += cell_value
            cells_put_out.append(cell_value)
print("Cells:")
for cell in cells_put_out:
    print(f" - {cell}")
print(f"Effort: {effort_needed:.2f}")
print(f"Total Fire: {total_fire}")