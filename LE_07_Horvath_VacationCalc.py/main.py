from datetime import datetime, timedelta

while True:
    try:        #asks for input
        start_date = input("Enter the start date (DD.MM.YYYY) or 0 to close the program: ")
        if start_date == "0":
            print("Program closed.")
            break

        end_date = input("Enter the end date (DD.MM.YYYY): ")
        vac_days_poss = input("Please enter how many vacation days you got left: ")

        # convert input to datetime objects
        date1 = datetime.strptime(start_date, "%d.%m.%Y")
        date2 = datetime.strptime(end_date, "%d.%m.%Y")

        # make sure date1 is before date2
        if date1 > date2:
            date1, date2 = date2, date1

        # calculate number of days between two dates
        diff = date2 - date1
        total_days = diff.days

        #initialise days minus weekend days
        actual_vac_days = 0

        #loops through each day to check for weekdays
        for i in range(total_days + 1):  # +1 to ensure end date is correct
            current_day = date1 + timedelta(days=i) #adds a day to current day
            if current_day.weekday() < 5:  # 0-4 = monday-friday
                actual_vac_days += 1    #adds 1 to actual days if its weekday


        # check for leap year and print february days
        for year in range(date1.year, date2.year + 1):
            if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
                feb_days = 29
                print(f"\nYear {year} is a leap year. February has {feb_days} days.")
            else:
                feb_days = 28
                print(f"\nYear {year} is not a leap year. February has {feb_days} days.")

        #initialises days left for vacation variable
        vac_left = int(vac_days_poss) - int(actual_vac_days)

        print(f"\nTotal vacation days between {date1.strftime('%d.%m.%Y')} and {date2.strftime('%d.%m.%Y')} is: {actual_vac_days} actual vacation days.\n")

        #checks if vacation is valid or recommends suitable date if not
        if int(vac_days_poss) >= int(actual_vac_days):
            print(f"The vacation you planned is valid.\n")
            print(f"You got {vac_left} vacation days left.")
        else:
            print(f"The vacation you planned exceeds your available vacation days.\n")

            # start from the first day and count vacation days until you run out
            days_used = 0
            current_day = date1

            #while days used < possible days add 1 day for every weekday
            while days_used < int(vac_days_poss):
                if current_day.weekday() < 5:  # 0-4 = monday to friday
                    days_used += 1

                #if enough vac days available
                if days_used < int(vac_days_poss):
                    current_day += timedelta(days=1)  # move to the next day

            recommended_end_date = current_day  # recommended end date = last day you could take off

            print(f"With {vac_days_poss} vacation days, you could take a vacation from {date1.strftime('%d.%m.%Y')} to {recommended_end_date.strftime('%d.%m.%Y')}.")

    except ValueError:
        print("Invalid input. Please enter the date in the correct format (DD.MM.YYYY).")
