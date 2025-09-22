from utilities import user_input
#preparation

def addition (x, y):
    return x + y

def subtraction (x, y):
    return x - y

def multiplication (x, y):
    return x * y

def division (x, y):
    if y == 0:
        print("Error, can't divide by zero.")
    else:
        return x / y

def modulo(x, y):
    if y == 0:
        return "Error: modulo by zero"
    return x % y

#main part

def calculator():
    try:
        x_value = float(user_input("Enter the first value: "))
        y_value = float(user_input("Enter the second value: "))
    except ValueError:
        print("Enter valid numbers.")
        return

    operation_value = user_input("Choose an operator (+, -, *, /, %) : ")

    if operation_value == "+" :
        result = addition(x_value,y_value)
    elif operation_value == "-":
        result = subtraction(x_value,y_value)
    elif operation_value == "*":
        result = multiplication(x_value,y_value)
    elif operation_value == "/":
        result = division(x_value,y_value)
    elif operation_value == "%":
        result = modulo(x_value,y_value)
    else:
        print("Invalid operation.")
        return

    print(result)




