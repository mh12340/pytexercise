import os

while True:

    # shows menu
    print("\nFile administration:\n")
    print("1. Write in file")
    print("2. Read file")
    print("3. Edit file")
    print("4. Delete file.")
    print("5. Close program.")

    #get userchoice
    choice = input("\nChoose an option (1-5): ")

    #close program when choice == 5
    if choice == '5':
        print("Program closed.")
        exit()

    #asks for the files name
    file = input("\nPlease choose file (txt1.txt or txt2.txt): ")

    #choice 1 to write and store it in chosen file
    if choice == '1':
        text = input("Please enter text to store in file: ")
        with open(file, 'w') as file_handle:
            file_handle.write(text)
        print(f"Text was added to {file} file.")

    #choice 2 to read the chosen file and print it
    if choice == '2':
        with open(file, 'r') as file_handle:
            content = file_handle.read()
        print(f"Reading file {file}: \n")
        print(content)

    #choice 3 to edit/append content in file
    if choice == '3':
        with open(file, 'r') as file_handle:
            content = file_handle.read()
        print(f"Current content in {file} file: ")
        print(content)

        new_content = input("Please enter new content to store in file.")
        with open(file, 'a') as file_handle:
            file_handle.write(new_content)
        print(f"File content updated.")

    #choice 4 to delete the chosen file
    if choice == '4':
        os.remove(file)
        print("File deleted.")





