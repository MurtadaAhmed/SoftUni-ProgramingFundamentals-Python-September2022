# 1.get the input and add .lower as it is case-insensitive according to the task.
# 2.use . count for each of the requested words "Sand", "Water", "Fish", and "Sun" to count the occurrences.
# 3.print the sum of all the counts

# 1
command = input().lower()
# 2
sand_count = command.count("sand")
water_count = command.count("water")
fish_count = command.count("fish")
sun_count = command.count("sun")
# 3
print(sand_count + water_count + fish_count + sun_count)
