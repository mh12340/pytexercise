import os

#Use this program to view/create/delete directory.
#Enter wanted operation, enter path. Now the program will create/delete/show directory in specified path.

while True:
    #shows menu
    print("\nDirectory administration:\n")
    print("1. Show directory")
    print("2. Create directory")
    print("3. Delete directory")
    print("4. Close program.")

    #get userchoice
    choice = input("\nChoose an option (1-4): ")

    if choice == '1':
        #show directory
        path = input("Enter directory path: ")
        if os.path.exists(path):
            print(f"Content of '{path}':")
            #iterates through every item in the directory
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                #distinguishes between file/directory
                if os.path.isdir(item_path):
                    print(f"[D] {item}")
                else:
                    print(f"[F] {item}")
        else:
            print("Path doesn't exist.")

    elif choice == '2':
        #create directory
        path = input("Enter path to create new directory: ")
        try:
            #creates directory in given path
            os.makedirs(path)
            print(f"Directory '{path}' created.")
            #file exists error
        except FileExistsError:
            print("Directory exists already.")
            #no permission error
        except PermissionError:
            print("You don't have permission to create the directory.")

    elif choice == '3':
        #delete directory
        path = input("Enter path to delete directory: ")
        try:
            #deletes empty directory in given path
            os.rmdir(path)
            print(f"Directory '{path}' deleted.")
            #file not found error
        except FileNotFoundError:
            print("Directory not found.")
            #no permission error
        except PermissionError:
            print("You don't have permission to delete the directory.")

    elif choice == '4':
        #close program
        print("Program closed.")
        break

    else:
        print("Invalid operation. Please choose one of the options provided(1, 2, 3, 4).")
