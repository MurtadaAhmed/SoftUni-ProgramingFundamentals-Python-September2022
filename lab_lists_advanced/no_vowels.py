vowels = ['a', 'o', 'u', 'e', 'i']
command = input()
text_without_vowels = [x for x in command if x.lower() not in vowels]
print("".join(text_without_vowels))