#ask user_input and what to get rid of in user_input
user_input = input("Please enter the text you want to encrypt: ")
user_rid = input("Please enter the characters to get rid of in your message(without spaces): ")

#creates list and removes both uppercase and lowercase characters
get_rid_of = []

for char in user_rid:
    get_rid_of.append(char.lower())
    get_rid_of.append(char.upper())

#assigns user_input to user_decrypted
user_decrypted = user_input

#creates encrypted text by removing characters
user_encrypted = ''.join([char for char in user_input if char not in get_rid_of])

#print the encrypted text
print(user_encrypted)

#asks if user wants to decrypt or stop program
user_question = input("Please type 'decrypt' to decrypt the message again or anything else to quit: ")

#if decrypt then decrypt and close program, if anything else close program
if user_question == 'decrypt':
    print(user_decrypted)
else:
    print("Program closed.")
    exit()