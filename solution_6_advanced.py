import scrabble

# Print the longest word where every character is unique.  I used a Set for
# this which we'll talk about today.

# Don't worry: you didn't miss anything if you don't know what a set is. We
# didn't teach it, but if you are reading this, you get a bonus!

# A set is a container like a list or a dict, except that *each element can be
# stored only once*.  Think of it like the keys of a dict, except there isn't
# any value associated with each key.  I use Sets to count digits below. Feel
# free to look up the Set online and try it in the interpreter.

new_words = []
for word in scrabble.wordlist:
    local_chars = {}
    if len(word) == len(set(word)): # Wait what!? See if you can figure out why this works.
        new_words.append(word)

# Reuse my code for longest word, (in this case, the code to track all
# occurences) from the advanced solution.

longest_so_far = []
length_of_longest_word = 0

for word in new_words:
    if len(word) > length_of_longest_word:
        length_of_longest_word = len(word)
        longest_so_far = [word]
    elif len(word) == length_of_longest_word:
        longest_so_far.append(word)

print(longest_so_far)
