version = input().split(".")
version_as_integers = list(map(int, version))  # [1, 2, 3]
if version_as_integers[2] < 9:
    version_as_integers[2] += 1
elif version_as_integers[2] == 9:
    version_as_integers[2] = 0
    if version_as_integers[1] < 9:
        version_as_integers[1] += 1
    elif version_as_integers[1] == 9:
        version_as_integers[1] = 0
        version_as_integers[0] += 1

final_list_as_string = list(map(str, version_as_integers))  # converting the int list into str list
print(".".join(final_list_as_string))  # converting the list str into string