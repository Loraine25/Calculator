# Anonuevo, Loraine N.
# BSCpE 1-4
# Simple Calculator

#Header
print("\033[;33;1;3m\033[10m" * 65)
print("\033[;33;1;3mHi! It's a pleasure to have you here!\033[0m".center(81))
print("\033[;33;1;3mಠ\033[10m" * 65)

#Request about the user's name.
print("")
print("\033[1;3mMy name is \033[;45;1;3mLoraine\033[0m")
your_name = input("\033[1;3mWhat is your name?\033[0m")
print("\033[;1;3mI'm glad that you're here!\033[;34;1;3m" + your_name + "\033[0m \033[;1;3m, sit back and learn with me!\033[0m")

def calculator():
    print("\n")

    # Choosing Operation
    operation = input(
        '"+" for addition\n'
        '"-" for subtraction\n'
        '"*" for multiplication\n'
        '"/" for division\n'
        'Select an operation: '
    )

    # Ask to enter first and second number
    firstnumber = float(input("\033[;33m" "Enter the 1st number : "))
    secondnumber = float(input("\033[;33m" "Enter the 2nd number : "))

    # If the user wants addition
    if operation == "+":
        print(firstnumber, "+", secondnumber)
        sum = firstnumber + secondnumber
        print("The result is:", "\033[;3m" + str(sum) + "\033[;m")

    # If the user wants subtraction
    elif operation == "-":
        print(firstnumber, "-", secondnumber)
        difference = firstnumber - secondnumber
        print("The difference:", "\033[;3m" + str(difference) + "\033[;m")

    # If the user wants multiplication
    elif operation == "*":
        print(firstnumber, "*", secondnumber)
        product = firstnumber * secondnumber
        print("The product:", "\033[;3m" + str(product) + "\033[;m")

    # If the user wants division
    elif operation == "/":
        # Exception for division, if the user entered zero(0) as a divisor(2nd number)
        try:
            print(firstnumber, "/", secondnumber)
            quotient = firstnumber / secondnumber
            print("The quotient:", "\033[;3m" + str(quotient) + "\033[;m")

        except ZeroDivisionError as ERROR:
            print("\033[1;31m" "Invalid equation\n")
            print(ERROR)
            print("\nTry again, please insert a non-zero number")



calculator()

