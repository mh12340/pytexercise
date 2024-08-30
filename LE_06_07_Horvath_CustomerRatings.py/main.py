#loop until valid input
while True:
    try:
        customers = int(input("How many customers tested the product? "))
        if customers > 0:
            break
        else:
            print("Please enter number greater than 0.")
    except ValueError:
        print("Invalid Input. Please enter valid number.")

#initialise ratings list
ratings = []

#asks for ratings for each customer
for i in range(1, customers + 1):
    while True:
        try:
            rating = int(input(f"Customer #{i}, how would you rate the product? (1 = bad, 2 = OK, 3 = would recommend) "))
            if rating in [1, 2, 3]:         #if rating is in 1, 2 or 3 it breaks out of loop and asks next customer
                ratings.append(rating)
                break
            else:
                print("Please enter valid rating (1, 2, 3).")        #if not in 1,2,3 it asks for valid rating again
        except ValueError:
            print("Please enter valid rating (1, 2, 3).")           #if something else than numbers is entered it raises value error

#counts the ratings separately
count1 = ratings.count(1)
count2 = ratings.count(2)
count3 = ratings.count(3)

#calculates the ratings %
percentage1 = count1 / customers * 100
percentage2 = count2 / customers * 100
percentage3 = count3 / customers * 100

#prints the results
print(f"{customers} customers rated the product. {count1} rated it bad ({percentage1:.0f}%), {count2} rated it OK ({percentage2:.0f}%) and {count3} rated it great ({percentage3:.0f}%).")
