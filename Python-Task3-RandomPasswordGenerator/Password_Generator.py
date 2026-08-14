import random
import string

while True:
    print("\n--- Random Password Generator ---")

    # Password length
    try:
        length = int(input("Enter password length (minimum 8): "))

        if length < 8:
            print("Password length must be at least 8 characters.")
            continue

    except ValueError:
        print("Please enter a valid number.")
        continue

    # Character type selection
    print("\nChoose character types:")
    print("1. Uppercase letters")
    print("2. Lowercase letters")
    print("3. Numbers")
    print("4. Symbols")

    choices = input("Enter your choices (example: 123): ")

    selected_types = set(choices)

    # At least 2 valid character types
    valid_types = {"1", "2", "3", "4"}

    if len(selected_types.intersection(valid_types)) < 2:
        print("Please select at least 2 valid character types.")
        continue

    # Create character pool
    characters = ""

    if "1" in selected_types:
        characters += string.ascii_uppercase

    if "2" in selected_types:
        characters += string.ascii_lowercase

    if "3" in selected_types:
        characters += string.digits

    if "4" in selected_types:
        characters += string.punctuation

    # Guarantee at least one character from each selected type
    password_chars = []

    if "1" in selected_types:
        password_chars.append(random.choice(string.ascii_uppercase))

    if "2" in selected_types:
        password_chars.append(random.choice(string.ascii_lowercase))

    if "3" in selected_types:
        password_chars.append(random.choice(string.digits))

    if "4" in selected_types:
        password_chars.append(random.choice(string.punctuation))

    # Add remaining random characters
    remaining = length - len(password_chars)

    for _ in range(remaining):
        password_chars.append(random.choice(characters))

    # Shuffle characters
    random.shuffle(password_chars)

    # Convert list into password
    password = ''.join(password_chars)

    print("\nGenerated Password:", password)

    # Generate another password
    again = input("\nGenerate another password? (yes/no): ").lower()

    if again != "yes":
        print("Thank you for using the Password Generator!")
        break