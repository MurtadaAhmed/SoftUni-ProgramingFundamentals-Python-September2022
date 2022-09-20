# 1.read the divisor
# 2.read the boundary
# 3.create a variable current_biggest_number = 0
# 3.create for loop with the boundary as the maximum value per the task
# 4.for each iteraion, we % the current iterator by the divisor to see if it is == 0:
# -if it is == 0, we need to check if it is the current biggest result by comparing it with the variable:
# --if it is begger than it, we need to replace its value with it
divisor = int(input())
boundary = int(input())
current_biggest_number = 0
for number in range(boundary+1):  # as the boundary is inclusive based on the task
    if number % divisor == 0:
        if number > current_biggest_number:
            current_biggest_number = number
print(current_biggest_number)