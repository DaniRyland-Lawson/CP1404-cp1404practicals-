"""Word count occurrences in a string"""

# Need to get input from the user and add to an empty dictionary.

users_words = {}
user_text = input(str("Please enter a string of text: "))

words = user_text.split()
# Counting the words from the users input
for word in words:
    word_occurrence = users_words.get(word, 0)
    if word_occurrence is None:
        users_words[word] = 1
    else:
        users_words[word] = word_occurrence + 1

words = list(users_words.keys())
words.sort()
max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, users_words[word]))
