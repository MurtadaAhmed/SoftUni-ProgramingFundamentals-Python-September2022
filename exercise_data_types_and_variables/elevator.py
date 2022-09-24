number_of_people = int(input())
capacity = int(input())
number_of_courses = int(number_of_people / capacity)
if number_of_people % capacity != 0: # which means there are people left in the end less than the capacity
    number_of_courses += 1
print(number_of_courses)