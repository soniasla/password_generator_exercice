from password import password
from utilities import user_input

if __name__ == "__main__":
    try:
        password_input = user_input("How many characters do you want in your password? ")
        password_length = int(password_input)
    except ValueError:
        print("Enter a number.")
    else:
        word = password(password_length)
        print(word)

