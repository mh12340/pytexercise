from datetime import datetime

while True:
    try:        #asks for input
        start_date = input("Enter the start date (DD.MM.YYYY) or 0 to close the program: ")
        if start_date == "0":
            print("Program closed.")
            break

        end_date = input("Enter the end date (DD.MM.YYYY): ")

        # convert input to datetime objects
        date1 = datetime.strptime(start_date, "%d.%m.%Y")
        date2 = datetime.strptime(end_date, "%d.%m.%Y")

        # make sure date1 is before date2
        if date1 > date2:
            date1, date2 = date2, date1

        # calculate number of days between two dates
        diff = date2 - date1
        total_days = diff.days

        # count leap years and print february days
        leap_years = 0
        for year in range(date1.year, date2.year + 1):
            if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
                leap_years += 1
                feb_days = 29
                print(f"Year {year} is a leap year. February has {feb_days} days.")
            else:
                feb_days = 28
                print(f"Year {year} is not a leap year. February has {feb_days} days.")

        print(f"\nTotal days between {date1.date()} and {date2.date()} is: {total_days} days")
        print(f"Number of leap years in this range: {leap_years}\n")

    except ValueError:
        print("Invalid input. Please enter the date in the correct format (DD.MM.YYYY).")
