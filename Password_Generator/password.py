import string
import secrets

def password(length, upper=True, lower=True, number=True, symbols=False, weird_character=False):
    password_pool = ""
    if lower:
        password_pool += string.ascii_lowercase
    if upper:
        password_pool += string.ascii_uppercase
    if number:
        password_pool += string.digits
    if symbols:
        password_pool += string.punctuation

    if weird_character:
        character = "lI1O0"
        new_password_pool = ""
        for i in password_pool:
            if i not in character:
                new_password_pool += i
        password_pool = new_password_pool

    if not password_pool:
        raise ValueError("Error.")

    user_password = ""
    for i in range(length):
        y = secrets.choice(password_pool)
        user_password  += y
    return user_password






