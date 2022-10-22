number_of_rooms = int(input())
free_chairs = 0
chairs_are_enough = True
for room in range(1, number_of_rooms +1):
    chairs_and_people = input().split()
    chairs = chairs_and_people[0]
    people = int(chairs_and_people[1])
    count_of_chairs = 0
    for i in chairs:
        count_of_chairs += 1  # to convert X into numbers
    if count_of_chairs < people:
        chairs_are_enough = False
        print(f"{people-count_of_chairs} more chairs needed in room {room}")
    else:
        free_chairs += count_of_chairs - people

if chairs_are_enough:
    print(f"Game On, {free_chairs} free chairs left")