#importing both modules to have all the string constants and also the random module for generating random numbers and choice
import string
import random

#function generates a random password with specified length
def generate_password(length):  #function name and argument length
    #docstring, special type comment describe work of function
    """ 
    Generates a random password of specified length.
    The password includes uppercase, lowercase, digits, and special characters.
    """
    #checks length of password
    if length < 4:
        raise ValueError("Password length should be at least 4 or more to include all character types.")

    #define character sets for different complexities
    lowercase_letters = string.ascii_lowercase  #assigns lowercase letters to variable "lowercase_letters"
    uppercase_letters = string.ascii_uppercase  #assigns uppercase letters to variable "uppercase_letters"
    digits = string.digits   #assigns all 0-9 digits to the variable "digits"
    special_chars = string.punctuation #assigns special characters to the variable "special_chars"

    #ensures password includes one from each set
    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(special_chars)
    ]

    # Fill the rest of the password length with random characters
    all_characters = lowercase_letters + uppercase_letters + digits + special_chars
    password += [random.choice(all_characters) for _ in range(length - 4)]

    # Shuffle the list to ensure randomness and convert to a string
    random.shuffle(password)
    return ''.join(password)

def main():
    try:
        # Prompt the user for desired password length
        length = int(input("Enter the desired length of the password:"))

        # Generate and display the password
        password = generate_password(length)
        print("Generated Password:", password)
    except ValueError as e:
        # Handle invalid input
        print(e)

# Check if the script is being run directly
if __name__ == "__main__":
    main()
