# vowels = ['a','e','i','o','u','A','E','I','O','U']
# word = input("Enter a word: ") #pranali
# found = []
# for letter in word:
#     if letter in vowels:
#         if letter not in found:
#             found.append(letter)
# print(found)
# print("word:",word,len(found))


vowels = ['A','E','I','O','U']
word = input("Enter a word: ") #pranali
found = []
for letter in word:
    if letter.upper() in vowels:
        if letter.upper() not in found:
            found.append(letter.upper())
print(found)
print("word:",word,len(found))
