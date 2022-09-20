# 1.get the input, and convert it to list using split.
# 2.reverse the list order using slicing (this is to track the place of the wolf easier).
# 3.for loop through the length of the list from the input:
# -if the wolf is at the index 0 of the reversed list (meaning closest animal to me), we need to print the message:
# "Please go away and stop eating my sheep" and break the loop
# -elif the current iteration at index i is wolf, we need to print the message:
# "Oi! Sheep number {i}! You are about to be eaten by a wolf!"(we keep the order of the sheep as {i} similar to the wolf
# as in the task the order starts from 1 and not from 0, so the result will be accurate this way)

# 1
sheep_list = input().split(", ")
# 2
reversed_list = sheep_list[::-1]
# 3
for i in range(len(reversed_list)):
    if reversed_list[0] == "wolf":
        print("Please go away and stop eating my sheep")
        break
    elif reversed_list[i] == "wolf":
        print(f"Oi! Sheep number {i}! You are about to be eaten by a wolf!")