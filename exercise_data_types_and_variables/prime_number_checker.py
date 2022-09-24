number_to_be_checked = int(input())
counter = 0  # this should be 2 for the number to be prime (which means the number is divided only by itself and 1
for number in range(1, number_to_be_checked + 1):
    if number_to_be_checked % number == 0:
        counter += 1
if counter == 2:
    print(True)
else:
    print(False)