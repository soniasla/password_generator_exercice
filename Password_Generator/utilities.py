def user_input(message):
    while True :
        value_input = input(message).strip()
        if not value_input:
            print("Error")
            continue
        break

    return value_input

