from datetime import datetime

date1 = input("Please enter first date (DD.MM.YYYY): ")
date2 = input("Please enter second date (DD.MM.YYYY): ")

date1_obj = datetime.strptime(date1, "%d.%m.%Y")
date2_obj = datetime.strptime(date2, "%d.%m.%Y")

difference = date2_obj - date1_obj

print("The Difference in days between", date1, "and", date2, "is:", difference.days)

