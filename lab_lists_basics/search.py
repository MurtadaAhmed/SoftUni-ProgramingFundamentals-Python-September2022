number_of_lines = int(input())
key_word = input()
list_of_all_sentences = []
list_of_sentences_with_keyword = []
for sentence in range(number_of_lines):
    current_sentence = input()
    list_of_all_sentences.append(current_sentence)
    if key_word in current_sentence:
        list_of_sentences_with_keyword.append(current_sentence)
print(list_of_all_sentences)
print(list_of_sentences_with_keyword)