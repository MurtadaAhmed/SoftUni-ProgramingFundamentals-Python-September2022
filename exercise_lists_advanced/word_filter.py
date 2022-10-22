list_of_words = input().split()
even_list = [word for word in list_of_words if len(word) % 2 == 0]
for word in even_list:
    print(word)
