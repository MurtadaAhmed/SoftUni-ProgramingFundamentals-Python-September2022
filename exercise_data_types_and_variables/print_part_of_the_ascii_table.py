start_char = int(input())
end_char = int(input())
for char in range(start_char, end_char + 1):  # +1 as it is inclusive
    print(f"{chr(char)}", end=" ")