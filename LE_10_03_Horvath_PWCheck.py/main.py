import string

#check if password is 8 or more characters long.
def check_length(password):
    return 1 if len(password) >= 8 else 0

#check if the password contains uppercase and lowercase
def check_case(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    return 1 if has_upper and has_lower else 0

#check if password contains more than 6 unique characters
def check_unique_chars(password):
    return 1 if len(set(password)) > 6 else 0

#check if the password contains at least one digit
def check_digit(password):
    return 1 if any(c.isdigit() for c in password) else 0

#check if the password contains at least one special character
def check_special_char(password):
    special_chars = set(string.punctuation)  # Special characters
    return 1 if any(c in special_chars for c in password) else 0

#evaluate the password based on the given criteria
def evaluate_password(password):
    score = 0
    score += check_length(password)
    score += check_case(password)
    score += check_unique_chars(password)
    score += check_digit(password)
    score += check_special_char(password)
    return score

password = input("Enter the password: ")

#evaluate the password using function
score = evaluate_password(password)

print(f"Password Quality Score: {score} / 5")
