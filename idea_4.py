# 4. Find an print the words that contain 4 or more 'l's.

import scrabble 

for word in scrabble.wordlist:
    number_of_ls = 0
    for letter in word:
        if letter == "l":
            number_of_ls = number_of_ls + 1

    if number_of_ls >= 4:
        print(word)

