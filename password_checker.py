# ==========================================
# Password Strength Checker
# Created by Snehal
# Language: Python
# ==========================================

password = input("Enter your password :")

has_upper = False
has_lower = False
has_number = False
has_special = False


# Password score
score = 0

# Special characters
special_characters = "~@#$%^&*()_+[]{};:'\",.<>/?\\|"


# Check password length
if len(password) >=8:
    score += 1


# Check each character
for letter in password:

    if letter.isupper():
        has_upper = True
    
    if letter.islower():
        has_lower = True

    if letter.isdigit():
        has_number = True

    if letter in special_characters:
        has_special = True


# Increase score based on checks
if has_upper:
    score += 1

if has_lower:
    score += 1

if has_number:
    score += 1

if has_special:
    score += 1

# Display results
print("\n---------- Password Analysis -------------")

# Length
if len(password) >= 8:
    print("Length : Good")
else:
    print("Password is too short.")

# Uppercase
if has_upper:
    print("Uppercase Letter: Found")
else:
    print("Uppercase Letter: Not Found.")

# Lowercase
if has_lower:
    print("Lowercase Letter: Found")
else:
    print("Lowercase Letter: Not Found")

# Number
if has_number:
    print("Number: Found")
else:
    print("Number: Not Found")

# Special Character
if has_special:
    print("Special Character: Found")
else:
    print("Special Character: Not Found")

# Final Score
print("\nPassword Scrore:", score, "/5")

# Password Strength
if score <= 2:
    print("Password Strength: Weak")
elif score <= 4:
    print("Password Strength: Medium")
else:
    print("Password Strength: Strong")
