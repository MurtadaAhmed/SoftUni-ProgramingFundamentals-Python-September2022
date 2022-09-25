people_waiting = int(input())
there_is_people = False  # this is to exclude the possibility that the people waiting are 0 from the beginning
if people_waiting:
    there_is_people = True # means that people_waiting is not 0 from the beginning
current_state_of_lift = list(map(int, input().split()))  # converting str input into a list of int
for index, wagon_capacity in enumerate(current_state_of_lift):
    if wagon_capacity < 4:  # which means it has capacity
        empty_seats = 4 - wagon_capacity  # calculating the empty seats
        if people_waiting >= empty_seats:  # which means we gonna fill the wagon
            people_waiting -= empty_seats
            current_state_of_lift[index] += empty_seats
        elif people_waiting < empty_seats:  # which means the wagon will have empty seats
            current_state_of_lift[index] += people_waiting
            people_waiting = 0
list_convered_into_str = [str(i) for i in current_state_of_lift]  # this is just to print the result using .join
if people_waiting:  # means no enough space
    print(f"There isn't enough space! {people_waiting} people in a queue!")
    print(" ".join(list_convered_into_str))
elif not there_is_people:  # there_is_people == False >> means the people were zero from the beginning
    print(" ".join(list_convered_into_str))
elif not people_waiting and current_state_of_lift[-1] < 4:  # means there is an empty space
    print("The lift has empty spots!")
    print(" ".join(list_convered_into_str))
elif not people_waiting and current_state_of_lift[-1] == 4:  # means it is full and no people is waiting
    print(" ".join(list_convered_into_str))
