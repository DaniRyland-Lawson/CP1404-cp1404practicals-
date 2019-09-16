"""Word count occurrences in a string"""


# Need to get input from the user and add to an empty dictionary.
def main():
    user_string = {}
    user_text = input("Please enter a string of text: ")

    words = user_text.split()
    # Counting the words from the users input
    for word in words:
        occurrence = user_string.get(word, 0)
        if occurrence is None:
            user_string[word] = 1
        else:
            user_string[word] = occurrence + 1

    words = list(user_string.keys())
    words.sort()
    max_length = max((len(word) for word in words))
    for word in words:
        print("{:{}} : {}".format(word, max_length, user_string[word]))


main()
