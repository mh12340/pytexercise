#open file
file_path = r'C:\Users\16675\PycharmProjects\pythonProject3\txtfile.txt'
file = open(file_path, 'r', encoding='utf-8')

#read the file
text = file.read()

#close the file
file.close()

#split the text into words
words = text.split()

#start with empty string for longest word
longest_word = ''

#updates longest word if word > longest_word
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

#print result
print("The longest word is:", longest_word)
print("It's", len(longest_word), "characters long.")