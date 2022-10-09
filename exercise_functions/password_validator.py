def password_validator(password):
    password_is_valid = True
    if len(password) > 10 or len(password) < 6:
        print("Password must be between 6 and 10 characters")
        password_is_valid = False
    if not password.isalnum():
        print("Password must consist only of letters and digits")
        password_is_valid = False
    number_of_digits = 0
    for char in password:
        if char.isdigit():
            number_of_digits += 1
    if number_of_digits < 2:
        print("Password must have at least 2 digits")
        password_is_valid = False
    if password_is_valid:
        print("Password is valid")


password_input = input()
password_validator(password_input)