import re
from datetime import datetime
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

#show worker list
def show_worker_list(worker_list):
    if not worker_list:
        print("\nNo worker information available.")
    else:
        header = f"{'First & Last Name':<25} {'Position':20} {'Address':<30} {'Birthday':<15} {'Phone Number':<15} {'Email':<30}"
        print("\n" + header + "\n")

        for worker in worker_list:
            print(f"{worker[0]:<25} {worker[1]:<20} {worker[2]:<30} {worker[3]:<15} {worker[4]:<15} {worker[5]:<30}")

def show_filtered_workers():
    try:
        with open('txt2.txt', 'r') as file:
            content = file.read()
            if content:
                print("\nFiltered workers from txt2.txt:")
                print(content)
            else:
                print("\ntxt2.txt is empty. No filtered workers to display.")
    except FileNotFoundError:
        print("\ntxt2.txt not found. Please filter workers first.")

#filter and show worker list
def filter_and_show_worker_list():
    global filtered_infos
    if not worker_infos:
        print("\nNo worker information available to filter.")
        return

    search_term = input("Enter the value to filter by (name, position, address, etc.): ").strip().lower()
    filtered_infos = [worker for worker in worker_infos if any(search_term in str(field).lower() for field in worker)]

    if filtered_infos:
        print("\nFiltered Worker List:")
        show_filtered_workers()

        #export filtered workers to txt2.txt
        with open('txt2.txt', 'w') as file:
            for worker in filtered_infos:
                file.write(', '.join(worker) + '\n')
        print("\nFiltered workers exported to txt2.txt")
    else:
        print("\nNo workers match the given filter.")

#edit worker info
def edit_worker():
    if not worker_infos:
        print("\nNo workers to edit.")
        return

    for i, worker in enumerate(worker_infos):
        print(f"{i + 1}. {worker[0]} - {worker[1]}")

    try:
        worker_index = int(input("Enter the number of the worker to edit: ")) - 1
        worker = worker_infos[worker_index]
    except (ValueError, IndexError):
        print("Invalid choice. Try again.")
        return

    print("What would you like to edit? (1) Name, (2) Position, (3) Address, (4) Birthday, (5) Phone, (6) Email")
    choice = input("Enter the number: ")

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

#calculate days since last birthday and until next birthday
def calculate_days(birthday_str):
    try:
        birthday = datetime.strptime(birthday_str, "%d.%m.%Y")
        today = datetime.now()

        #create a date object for this year's birthday
        this_year_birthday = birthday.replace(year=today.year)

        if this_year_birthday > today:
            #if this year's birthday hasn't happened yet
            last_birthday = this_year_birthday.replace(year=today.year - 1)
            next_birthday = this_year_birthday
        else:
            #if this year's birthday has already passed
            last_birthday = this_year_birthday
            next_birthday = this_year_birthday.replace(year=today.year + 1)

        #calculate days passed since last birthday and days left until next birthday
        days_passed = (today - last_birthday).days
        days_left = (next_birthday - today).days

        return days_passed, days_left
    except ValueError:
        return None, None  #return None if the birthday format is invalid

#filter workers by birth month and export
def filter_and_export(month):
    filtered_workers = []

    for worker in worker_infos:
        try:
            birthday_day, birthday_month, birthday_year = worker[3].split('.')
            #check if the birthday month matches the input month
            if birthday_month == month:
                #calculate days since last birthday and days until next birthday
                days_passed, days_left = calculate_days(worker[3])  #make sure you use the correct function name here

                if days_passed is not None and days_left is not None:
                    #create a new tuple with additional days information
                    worker_with_days = worker + (str(days_passed), str(days_left))
                    filtered_workers.append(worker_with_days)
        except ValueError:
            print(f"Error processing worker: {worker}")  #handle unexpected format
        except IndexError:
            print(f"Error processing worker: {worker}")  #handle unexpected format

    #write filtered workers to the output file
    if filtered_workers:
        with open('filtered_bday.txt', 'w') as file:
            for worker in filtered_workers:
                file.write(', '.join(worker) + '\n')
    else:
        print("No workers found for the specified month.")

    return filtered_workers  #return the filtered list of workers


#export the entire worker list to a file
def export_to_file(filename):
    with open(filename, 'a') as file:  # use 'a' mode to append
        for worker in worker_infos:
            file.write(', '.join(worker) + '\n')
    print(f"\nWorker list exported to {filename}.")