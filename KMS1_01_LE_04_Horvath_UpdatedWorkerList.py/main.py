from datetime import datetime
import re
from email_validator import validate_email, EmailNotValidError

#initialize lists
worker_infos = []
filtered_infos = []

#first name validation
def first_name_check(first_name):
    if len(first_name) < 2 or len(first_name) > 20:
        return "\nInvalid name. Name must be between 2 and 20 letters."
    elif not re.match("^[A-Za-z]+$", first_name):
        return "\nInvalid name. Only alphabetic letters allowed."
    return None

#last name validation
def last_name_check(last_name):
    if len(last_name) < 2 or len(last_name) > 20:
        return "\nInvalid name. Name must be between 2 and 20 letters."
    elif not re.match("^[A-Za-z]+$", last_name):
        return "\nInvalid name. Only alphabetic letters allowed."
    return None

#position validation
def position_check(position):
    if len(position) < 2 or len(position) > 20:
        return "\nInvalid input. Position must be between 2 and 20 letters."
    elif not re.match("^[A-Za-z]+$", position):
        return "\nInvalid input. Only alphabetic letters allowed."
    return None

#birthday validation
def birthday_check(birthday):
    try:
        birth_date = datetime.strptime(birthday, "%d.%m.%Y")
        today = datetime.now()
        if birth_date > today:
            return "\nInvalid: Birthday cannot be in the future."
        return None
    except ValueError:
        return "\nInvalid date format. Please use DD.MM.YYYY."

#phone number validation
def phone_number_check(phone_number):
    if len(phone_number) != 11:
        return "\nInvalid phone number. Phone number must be 11 digits."
    elif not phone_number.isdigit():
        return "\nInvalid phone number. Only digits allowed."
    return None

#email validation
def email_check(e_mail):
    try:
        validate_email(e_mail)
        return None
    except EmailNotValidError as e:
        return f"Invalid email: {str(e)}"

#collect and validate worker info
def collect_worker_info():
    while True:
        first_name = input("Please enter first name: ")
        error = first_name_check(first_name)
        if error:
            print(error)
        else:
            break

    while True:
        last_name = input("Please enter last name: ")
        error = last_name_check(last_name)
        if error:
            print(error)
        else:
            break

    while True:
        position = input("Please enter position: ")
        error = position_check(position)
        if error:
            print(error)
        else:
            break

    home_address = input("Please enter home address: ")

    while True:
        birthday = input("Please enter birthday (DD.MM.YYYY): ")
        error = birthday_check(birthday)
        if error:
            print(error)
        else:
            break

    while True:
        phone_number = input("Please enter phone number (for example: 06641234567): ")
        error = phone_number_check(phone_number)
        if error:
            print(error)
        else:
            break

    while True:
        e_mail = input("Please enter e-mail: ")
        error = email_check(e_mail)
        if error:
            print(error)
        else:
            break

    #store worker information as a tuple
    worker_infos.append((f"{first_name} {last_name}", position, home_address, birthday, phone_number, e_mail))
    print("\nWorker information added successfully!")

#function to show the worker list with a header
def show_worker_list(worker_list):
    if not worker_list:
        print("\nNo worker information available.")
    else:
        #print the header with proper spacing
        header = f"{'First & Last Name':<25} {'Position':20} {'Address':<30} {'Birthday':<15} {'Phone Number':<15} {'Email':<30}"
        print("\n" + header + "\n")

        #print each worker's info with matching column widths
        for worker in worker_list:
            print(f"{worker[0]:<25} {worker[1]:<20} {worker[2]:<30} {worker[3]:<15} {worker[4]:<15} {worker[5]:<30}")

#filter the worker list and display results
def filter_and_show_worker_list():
    global filtered_infos
    if not worker_infos:
        print("\nNo worker information available to filter.")
        return

    search_term = input("Enter the value to filter by (name, position, address, etc.): ").strip().lower()
    filtered_infos = [worker for worker in worker_infos if any(search_term in str(field).lower() for field in worker)]

    if filtered_infos:
        print("\nFiltered Worker List:")
        show_worker_list(filtered_infos)
    else:
        print("\nNo workers match the given filter.")

#edit a worker's information
def edit_worker():
    if not worker_infos:
        print("\nNo workers to edit.")
        return

    #show workers with an index
    for i, worker in enumerate(worker_infos):
        print(f"{i + 1}. {worker[0]} - {worker[1]}")

    #ask which worker to edit
    try:
        worker_index = int(input("Enter the number of the worker to edit: ")) - 1
        worker = worker_infos[worker_index]
    except (ValueError, IndexError):
        print("Invalid choice. Try again.")
        return

    #ask what to edit
    print("What would you like to edit? (1) Name, (2) Position, (3) Address, (4) Birthday, (5) Phone, (6) Email")
    choice = input("Enter the number: ")

    #update based on the choice
    if choice == '1':
        new_value = input("Enter new name: ")
        worker_infos[worker_index] = (new_value, worker[1], worker[2], worker[3], worker[4], worker[5])
    elif choice == '2':
        new_value = input("Enter new position: ")
        worker_infos[worker_index] = (worker[0], new_value, worker[2], worker[3], worker[4], worker[5])
    elif choice == '3':
        new_value = input("Enter new address: ")
        worker_infos[worker_index] = (worker[0], worker[1], new_value, worker[3], worker[4], worker[5])
    elif choice == '4':
        new_value = input("Enter new birthday: ")
        worker_infos[worker_index] = (worker[0], worker[1], worker[2], new_value, worker[4], worker[5])
    elif choice == '5':
        new_value = input("Enter new phone number: ")
        worker_infos[worker_index] = (worker[0], worker[1], worker[2], worker[3], new_value, worker[5])
    elif choice == '6':
        new_value = input("Enter new email: ")
        worker_infos[worker_index] = (worker[0], worker[1], worker[2], worker[3], worker[4], new_value)
    else:
        print("\nInvalid option.")

    print("\nWorker info updated.")

#menu loop
def main_menu():
    while True:
        print("\nMenu:")
        print("1. Add worker")
        print("2. Show unfiltered worker list")
        print("3. Show filtered worker list")
        print("4. Filter list")
        print("5. Edit worker")
        print("6. Close program.")

        choice = input("Please enter your choice (1/2/3/4/5/6): ").strip()

        if choice == '1':
            collect_worker_info()
        elif choice == '2':
            show_worker_list(worker_infos)  #show the unfiltered list
        elif choice == '3':
            show_worker_list(filtered_infos)  #show the filtered list
        elif choice == '4':
            filter_and_show_worker_list()  #apply filter and display filtered list
        elif choice == '5':
            edit_worker()
        elif choice == '6':
            print("Program closed.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, or 6.")

#run main_menu
main_menu()
