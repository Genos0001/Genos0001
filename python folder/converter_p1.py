#A project name 'converter_p1.py' to just check how to convert decimal to octal, octal to decimal, decimal to hexadecimal, and hexadecimal to decimal.
#import turtle
#import time
#wn = turtle.Screen()   `!`

def decimal_to_octal(decimal):
    return oct(decimal).replace("0o", "")

def octal_to_decimal(octal):
    return int(octal, 8)

def decimal_to_hexadecimal(decimal):
    return hex(decimal).replace("0x", "")

def hexadecimal_to_decimal(hexadecimal):
    return int(hexadecimal, 16)

def binary_converter():
    print("Binary Converter")
    print("1. Decimal to Octal")
    print("2. Octal to Decimal")
    print("3. Decimal to Hexadecimal")
    print("4. Hexadecimal to Decimal")
    print("5. Exit")

    while True:
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            decimal = int(input("Enter a decimal number: "))
            octal = decimal_to_octal(decimal)
            print(f"Octal: {octal}")

        elif choice == "2":
            octal = input("Enter an octal number: ")
            decimal = octal_to_decimal(octal)
            print(f"Decimal: {decimal}")

        elif choice == "3":
            decimal = int(input("Enter a decimal number: "))
            hexadecimal = decimal_to_hexadecimal(decimal)
            print(f"Hexadecimal: {hexadecimal}")

        elif choice == "4":
            hexadecimal = input("Enter a hexadecimal number: ")
            decimal = hexadecimal_to_decimal(hexadecimal)
            print(f"Decimal: {decimal}")

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

binary_converter()

#new test lines