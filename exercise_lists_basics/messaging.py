numbers_sequence = input().split()
string = input()

string_length = len(string)
string_list = list(string)  # we converted it into a list, so that we can remove elements from it
final_word = ""
for numbers in numbers_sequence:  # ['9992', '562', '8933']
    integers_sum = 0  # this will be the index of the character in the string
    for num in numbers:  # sum the digits in '9992'
        integers_sum += int(num)
    while integers_sum >= string_length:  # if the index is bigger than the length of string
        integers_sum -= string_length  # we remove the length of the string from the index number, so we can count
        # the index again from the beginning of the string (so that we can find always a valid index)

    final_word += string_list[integers_sum]  # adding the character of the current index in the final word
    string_list.remove(string_list[integers_sum])  # removing the character of the current index from the string list

print(final_word)
