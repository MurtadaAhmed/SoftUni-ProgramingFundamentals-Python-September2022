number_of_lines = int(input())

for i in range(1, number_of_lines + 1):
    number = int(input())
    if number % 2 != 0:
        print(f"{number} is odd!")
        break
else:  # if there is no odd number
    print("All numbers are even.")