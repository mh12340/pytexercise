#initialize list to store peoples data
people = []

#function to add a person to list
def add_person():
    name = input("Enter the person's name: ")

#asks for age and prevents wrong input
    while True:
        try:
            age = int(input("Enter the person's age: "))
            break
        except ValueError:
            print("Please enter age in numbers.")

#asks for userinput
    email = input("Enter the person's email: ")
    person = f"{name}, {age}, {email}"
    people.append(person)
    print(f"{name} has been added.")

#function to save the people list to a file
def export_to_file(filename):
    with open(filename, 'a') as file:  # 'a' to append to the file
        for person in people:
            file.write(person + '\n')
    print(f"List saved to {filename}.")

#function to read the people list from a file
def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            print(f"\nPeople in {filename}:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"{filename} not found.")


#function to filter list by name and save to filtered list
def filter_and_export(filename):
    #reads peoples list first to get up to date list
    people_file = input("Enter the filename to read the full list from (for ex. people.txt): ")
    try:
        with open(people_file, 'r') as file:
            people_from_file = [line.strip() for line in file]  #read people from file and strips \n
    except FileNotFoundError:
        print(f"{people_file} not found. Can't filter.")
        return

    #filters list
    name_to_filter = input("Enter the name to filter: ")
    filtered_list = [person for person in people_from_file if name_to_filter in person]

    #if there's names to filter, append them to filtered_list
    if filtered_list:
        with open(filename, 'a') as file:
            for person in filtered_list:
                file.write(person + '\n')
        print(f"Filtered list saved to {filename}.")
    else:
        print(f"No one found with the name {name_to_filter}.")

#function to read a filtered file and display it
def read_filtered_file(filename):
    try:
        with open(filename, 'r') as file:
            print(f"\nFiltered people in {filename}:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"{filename} not found.")

#menu + userinput
def menu():
    while True:
        print("\nManagement")
        print("1. Add a person to the list")
        print("2. Save the list to a file")
        print("3. Read people from a file")
        print("4. Filter list by name and save")
        print("5. Read filtered list")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_person()
        elif choice == '2':
            filename = input("Enter the filename to save (for ex. people.txt): ")
            export_to_file(filename)
        elif choice == '3':
            filename = input("Enter the filename to read (for ex. people.txt): ")
            read_from_file(filename)
        elif choice == '4':
            filename = input("Enter the filename to save the filtered list (for ex. filtered.txt): ")
            filter_and_export(filename)
        elif choice == '5':
            filename = input("Enter the filename to read the filtered list (for ex. filtered.txt): ")
            read_filtered_file(filename)
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

#start program
menu()
