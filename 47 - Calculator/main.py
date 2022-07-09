import art
from art import logo

# Divide
def divide(n1, n2):
    return n1/n2


# Multiply
def multiply(n1, n2):
    return n1*n2


# Add
def add(n1, n2):
    return n1+n2


# Subtract
def subtract(n1, n2):
    return n1-n2


def calculator():
    print(art.logo)
    operations = {"/": divide,
                  "*": multiply,
                  "+": add,
                  "-": subtract,
                  }

    num1 = float(input("What is the first number? "))

    for symbol in operations:
        print(symbol)
    continue_flag = True

    while continue_flag:
        operation_symbol = input("Choose an operation: ")
        num2 = float(input("What is the second number? "))

        calculation_function = operations[operation_symbol]
        output_value = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {output_value}")
        if input("Type 'Y' to continue with current calculation or 'N' to start over: ").upper() == "Y":
            num1 = output_value
        else:
            continue_flag = False
            calculator()


calculator()
