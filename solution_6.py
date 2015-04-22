import scrabble

# Print the longest word where every character is unique.
# I use a double loop in this. Note that I also re-use my "longest word" logic
# from the easy solution to (2).

# See the advanced solution for a shorter way to do this.

new_words = []
for word in scrabble.wordlist:
    unique_letters = []
    duplicated_letters = False
    for character in word:
        # have we seen this character before?
        if character in unique_letters:
            duplicated_letters = True
        else:
            # store the character
            unique_letters.append(character)

    if not duplicated_letters:
        new_words.append(word)

# Reuse my code for longest word
longest_so_far = []
longest_length = 0
for word in new_words:
    if len(word) > longest_length:
        longest_so_far = [word]
        longest_length = len(word)
    elif len(word) == longest_length:
        longest_so_far.append(word)

print(longest_so_far)
