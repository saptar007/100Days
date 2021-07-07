from art import logo


def add (a,b):
    """Adds 2 numbers"""
    return (a+b)

def subtract (a,b):
    """Subrtacts 2 numbers"""
    return (a-b)

def multiply (a,b):
    """Multiplies 2 numbers"""
    return (a*b)

def divide (a,b):
    """Divides 2 numbers"""
    return (a/b)

# print (add(5,9))
operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator():
    print(logo)
    num1 = float(input("What is the first number?: "))
    should_continue = True

    # for symbol in operations:
    #     print(symbol)
    # operation_symbol = input("pick an operation from the lines above: ")
    #
    # num2 = int(input("What is the second number?: "))

    # calculation_function = (operations[(operation_symbol)])
    # answer = (calculation_function(num1, num2))
    # print(f"{num1} {operation_symbol} {num2} = {answer}")

    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("pick an operation: ")
        num2 = float(input("What is the second number?: "))
        calculation_function = (operations[(operation_symbol)])
        answer = (calculation_function(num1, num2))
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        operation_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit and start fresh.: ")
        if operation_continue == 'y':
            num1 = answer
        else:
            print(f"The Final answer is {answer}")
            should_continue = False
            calculator()

calculator()