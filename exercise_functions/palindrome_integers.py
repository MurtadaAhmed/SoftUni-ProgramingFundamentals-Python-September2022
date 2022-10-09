def palindrome(num):
    for number in num:
        if number == number[::-1]:
            print("True")
        else:
            print("False")


list_of_numbers = input().split(", ")
palindrome(list_of_numbers)