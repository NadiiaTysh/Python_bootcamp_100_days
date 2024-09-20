from os import stat_result
import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return  n1 * n2

def divide (n1, n2):
    return n1 / n2
# start_over = 'y'
#
# while start_over == 'y':
#     first_number = float(input("What is the first number?: "))
#
#     operations = {
#         "+": add,
#         "-": subtract,
#         "*": multiply,
#         "/": divide
#     }
#
#     to_continue = 'y'
#     while to_continue == 'y':
#         for key in operations:
#             print(key)
#
#         picked_operation = input("Pick an operation: ")
#         second_number = float(input("What's the next number?: "))
#
#         result = operations[picked_operation](first_number, second_number)
#         print(f"{first_number} {picked_operation} {second_number} = {result}")
#         to_continue = input(
#             f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
#         first_number = result
#         start_over = 'n'
#     else:
#         start_over = 'y'
#         print("\n" * 20)

def calculator():
    print(art.logo)
    first_number = float(input("What is the first number?: "))

    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

    to_continue = 'y'
    while to_continue == 'y':
        for key in operations:
            print(key)

        picked_operation = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))

        result = operations[picked_operation](first_number, second_number)
        print(f"{first_number} {picked_operation} {second_number} = {result}")
        to_continue = input(
            f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        first_number = result
    else:
        print("\n" * 20)
        calculator()

calculator()