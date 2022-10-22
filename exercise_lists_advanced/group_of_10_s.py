main_list = input().split(", ")
group_boundary = 10
lower_boundary = 0
total_processed_items = []
while len(main_list) != len(total_processed_items):
    current_list = []
    for i in main_list:
        if lower_boundary < int(i) <= group_boundary:
            current_list.append(int(i))
            total_processed_items.append(int(i))

    print(f"Group of {group_boundary}'s: {current_list}")
    group_boundary += 10
    lower_boundary += 10