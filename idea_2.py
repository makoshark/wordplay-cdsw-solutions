# 2. Find and print the words that end in "mt". How about "gry"?

import scrabble

for word in scrabble.wordlist:
    if word[-2:] == "mt":
        print(word)
    elif word[-3:] == "gry":
        print(word)

