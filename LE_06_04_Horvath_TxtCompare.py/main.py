import difflib

#ask for userinput
input_text1 = str(input("Please enter the first sentence: "))
input_text2 = str(input("Please enter the second sentence to compare them: "))

#split into list of words
words1 = input_text1.split()
words2 = input_text2.split()

#compares the two lists for differences
diff = list(difflib.ndiff(words1, words2))

#extracts different words
differing_words = [line for line in diff if line.startswith('- ') or line.startswith('+ ')]

#prints differing words if there are any
if differing_words:
    print("Words that are different between the texts:")
    for word in differing_words:
        print(word)
else:
    print("The texts are the same.")

