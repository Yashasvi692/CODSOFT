import random
import string
def generate_password(length):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    all_characters = lowercase + uppercase + digits + special_characters
    for i in range(1,length):
        password =random.choice(all_characters)
    return password
def password_generator():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Password length must be a positive number.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return
    password = generate_password(length)
    print(f"\nYour generated password is: {password}")
if __name__ == "__main__":
    password_generator()
