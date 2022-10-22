string = input().split()
number_of_words = len(string)
current_index = 0
word_digits = ""
word_strings = ""

while number_of_words > 0:
    for i in string[current_index]:  # for first word
        if i.isdigit():
            word_digits += i
        else:
            word_strings += i

    letter_from_digit = chr(int(word_digits))  # digit converted into str
    complete_new_word = letter_from_digit + word_strings  # the new word without replacing the positions of the letters
    # in the next lines, converting the string into list, swapping the second and the last letters as the task request,
    # and then convert the list back into a string and print it:
    list_from_string = list(complete_new_word)
    list_from_string[1], list_from_string[-1] = list_from_string[-1], list_from_string[1]
    the_final_string = "".join(list_from_string)
    print(the_final_string, end=" ")
    # the following lines is to empty the values for the next loop
    word_digits = ""
    word_strings = ""
    # increase the index to loop through the next word, and reduce the word count for the while loop to stop when we
    # process all the words
    current_index += 1
    number_of_words -= 1