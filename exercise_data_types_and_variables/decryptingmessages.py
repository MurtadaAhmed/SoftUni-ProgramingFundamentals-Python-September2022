# The idea is get the ord of each line and add to it the key >> the result is number ASCII
# Then convert the ASCII number into character using chr, and add it to the message
# Repeat the same for each line
key = int(input())
number_of_lines = int(input())
message = ""  # where we gonna add the message to be printed
for i in range(number_of_lines):
    line = input()
    line_as_number = ord(line) + key
    line_as_char = chr(line_as_number)
    message += line_as_char
print(message)
