# initialize a set to store unique words
unique_words = set()

while True:
    # ask for user input
    input_text = input("Please enter words separated with a space to store them in list or 'q' to quit: ")

    if input_text == 'q':
        print("Program closed.")
        break

    # split the input into a list of words and add them to the set
    words = input_text.split()
    unique_words.update(words)

    # print the current state of unique_words
    print("Current list of unique words:", list(unique_words))