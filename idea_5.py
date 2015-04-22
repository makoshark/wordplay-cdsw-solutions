# 5. Find and print the words that have all 5 vowels in alphabetical order.

import scrabble

vowels = ["a", "e", "i", "o", "u"]

for word in scrabble.wordlist:
    found_vowels = []

    for letter in word:
        if letter in vowels:
            found_vowels.append(letter)

    if found_vowels == vowels:
        print(word)

