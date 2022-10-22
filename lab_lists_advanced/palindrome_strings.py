list_of_words = input().split()
given_word = input()
palindromes = []
for word in list_of_words:
    if word == word[::-1]:  # means it is palindrome
        palindromes.append(word)

counts_of_given_word = palindromes.count(given_word)  # count of the given_word in the palindromes

print(palindromes)
print(f"Found palindrome {counts_of_given_word} times")
