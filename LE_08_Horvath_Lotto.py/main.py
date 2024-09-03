import random

#generate random numbers
main_numbers = random.sample(range(1, 46), 6)
#gets random number which isnt in main numbers already 1-45
additional_number = random.choice([n for n in range(1, 46) if n not in main_numbers])
#sorts the main numbers list
main_numbers.sort()

#get user input
user_input = input("Please enter 6 numbers (1-45) to play lotto: ")
#splits the usernumbers in list
user_numbers = user_input.split()

#check for 6 numbers
if len(user_numbers) != 6:
    print("Invalid input. You must enter exactly 6 numbers.")
    exit()

#convert user input to integers
try:
    user_numbers = list(map(int, user_numbers))
except ValueError:
    print("Invalid input. Please enter valid numbers.")
    exit()

#check for unique numbers
if len(set(user_numbers)) != 6:
    print("All 6 numbers must be unique.")
    exit()

#check if each number is between 1 and 45
valid = True
for number in user_numbers:
    if number < 1 or number > 45:
        valid = False
        break

if not valid:
    print("Invalid input. All numbers must be between 1 and 45.")
    exit()

#checks for matches
matches = [num for num in user_numbers if num in main_numbers]
#counts the matches
num_matches = len(matches)
#checks for additional number in usernumbers
has_additional_number = additional_number in user_numbers

#if valid input, checks for win
if num_matches == 6:
    print("\nCongratulations, you won the jackpot!")
elif num_matches == 5 and has_additional_number:
    print("\nYou guessed 5 numbers plus the additional number.")
elif num_matches == 5:
    print("\nYou guessed 5 numbers.")
elif num_matches == 4 and has_additional_number:
    print("\nYou guessed 4 numbers plus the additional number.")
elif num_matches == 4:
    print("\nYou guessed 4 numbers.")
elif num_matches == 3 and has_additional_number:
    print("\nYou guessed 3 numbers plus the additional number.")
elif num_matches == 3:
    print("\nYou guessed 3 numbers.")
elif has_additional_number:
    print("\nYou guessed the additional number.")
else:
    print("\nNo significant matches.")

print(f"You matched {num_matches}.")
print(f"\nMain Numbers: {main_numbers}")
print(f"Additional Number: {additional_number}")
