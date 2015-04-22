# 3. Find and print the longest word that has no vowels.

import scrabble

vowels = ['a', 'e', 'i', 'o', 'u']
words_without_vowels = []

for word in scrabble.wordlist:
    vowel_in_word = False
    for vowel in vowels:
        if vowel in word:
            vowel_in_word = True
    if not vowel_in_word:
        words_without_vowels.append(word)

longest_word_length = 0
longest_words = []
for word in words_without_vowels:
    if len(word) > longest_word_length:
        longest_words = [word]
        longest_word_length = len(word)
    elif len(word) == longest_word_length:
        longest_words.append(word)

for word in longest_words:
    print(word)

