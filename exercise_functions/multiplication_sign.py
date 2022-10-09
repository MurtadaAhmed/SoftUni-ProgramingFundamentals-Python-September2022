def multiplication_result(num1, num2, num3):
    numbers_list = [num1, num2, num3]
    negative_count = 0
    zero_count = 0
    is_zero = False
    for i in numbers_list:
        if i == 0:
            zero_count += 1
            is_zero = True
            print("zero")
            break  # because we find one zero, it means the result of multiplication will be zero
        elif i < 0:
            negative_count += 1

    if not is_zero and negative_count == 1 or negative_count == 3:
        print("negative")
    elif not is_zero and negative_count == 0 or negative_count == 2 :  # when negative count either 2 or zero, which
        # means the multiplication will be positive
        print("positive")


first_number = int(input())
second_number = int(input())
third_number = int(input())

multiplication_result(first_number, second_number, third_number)