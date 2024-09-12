from datetime import datetime
import re
from email_validator import validate_email, EmailNotValidError

#initialize list
worker_infos = []

#first name validation
def first_name_check(first_name):
    if len(first_name) < 2 or len(first_name) > 20: #checks for length
        return "Invalid name. Name must be between 2 and 20 letters."
    elif not re.match("^[A-Za-z]+$", first_name): #checks for lower and uppercase letters A-z
        return "Invalid name. Only alphabetic letters allowed."
    return None  # If valid, return None

#last name validation
def last_name_check(last_name):
    if len(last_name) < 2 or len(last_name) > 20:   #checks for length
        return "Invalid name. Name must be between 2 and 20 letters."
    elif not re.match("^[A-Za-z]+$", last_name): #checks for lower and uppercase letters A-z
        return "Invalid name. Only alphabetic letters allowed."
    return None  #if valid, return None

#birthday validation
def birthday_check(birthday):
    try:
        birth_date = datetime.strptime(birthday, "%d.%m.%Y")    #formats to datetime object
        today = datetime.now()
        if birth_date > today:
            return "Invalid: Birthday cannot be in the future."
        return None  #if valid return None
    except ValueError:
        return "Invalid date format. Please use DD.MM.YYYY."

#phone number validation
def phone_number_check(phone_number):
    if len(phone_number) != 11:
        return "Invalid phone number. Phone number must be 11 digits."
    elif not phone_number.isdigit():
        return "Invalid phone number. Only digits allowed."
    return None  #if valid, return None

#email validation
def email_check(e_mail):
    try:
        validate_email(e_mail)
        return None  #if valid, return None
    except EmailNotValidError as e:
        return f"Invalid email: {str(e)}"  #if invalid return the error

#main function to collect and validate worker info
def collect_worker_info():

    while True:
        first_name = input("Please enter first name: ")
        error = first_name_check(first_name)
        if error: #checks for error in first_name_check function
            print(error) #if error prints it
        else:
            break #if valid breaks out of loop

    while True:
        last_name = input("Please enter last name: ")
        error = last_name_check(last_name)
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
    worker_infos.append((f"{first_name} {last_name}", home_address, birthday, phone_number, e_mail))

    print("Worker information added successfully!")

#function to show the worker list with a header
def show_worker_list():
    if not worker_infos:
        print("No worker information available.")
    else:
        #print the header with proper spacing
        header = f"{'First & Last Name':<25} {'Address':<30} {'Birthday':<15} {'Phone Number':<15} {'Email':<30}"
        print("\n" + header + "\n")

        #print each worker's info with matching column widths
        for worker in worker_infos:
            print(f"{worker[0]:<25} {worker[1]:<30} {worker[2]:<15} {worker[3]:<15} {worker[4]:<30}")

#menu loop
def main_menu():
    while True:
        print("\nMenu:")
        print("1. Add Worker")
        print("2. Show Worker List")
        print("3. Close Program")

        choice = input("Please enter your choice (1/2/3): ").strip()

        if choice == '1':
            collect_worker_info()
        elif choice == '2':
            show_worker_list()
        elif choice == '3':
            print("Program closed")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

#run program
main_menu()
