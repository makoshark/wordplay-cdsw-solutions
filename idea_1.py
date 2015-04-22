# 1. Find and print the words that start with "ee".

import scrabble

for word in scrabble.wordlist:
    if word[0:2] == "ee":
        print(word)
