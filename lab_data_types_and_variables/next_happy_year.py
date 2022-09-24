year = int(input())
is_happy_year = False  # will be changed to True when the happy year is found, and this will break while loop

while not is_happy_year:  # while is_happy_year == False
    year_as_set = set()  # we will add the year digits as set to get unique digits only as per the task
    year += 1  # for each loop increasing the year by one
    year_as_string = str(year)  # converted to str so we can use it to get the length of the year in the for loop
    for digit in range(len(year_as_string)):  # looping through each digit of the year and adding it to the set
        year_as_set.add(year_as_string[digit])
    if len(year_as_string) == len(year_as_set):  # because the year should have 4 digits, and if the set has 4 digits
        # this means that it is special year, as all the digits are unique
        is_happy_year = True  # this will break the loop in the next iteration
        print(year)
