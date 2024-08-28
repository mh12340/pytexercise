while True:
    try:
        year = int(input("Please enter the year to check if it's a leap year(or 0 to close program): "))

        #leap year = divisible by 4. if divisible by 100 it's not a leap year, except if it's divisible by 400

        if year == 0:
            print("Program closed.")
            break

        if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
            print("It's a leap year.")
        else:
            print("It's not a leap year.")
    except ValueError:
        print("Invalid Input.")