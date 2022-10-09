def data_types(command, number):
    if command == "int":
        return int(number) * 2
    elif command == "real":
        return f'{(float(number) * 1.5):.2f}'
    elif command == "string":
        return f"${number}$"


command = input()
number = input()

print(data_types(command, number))