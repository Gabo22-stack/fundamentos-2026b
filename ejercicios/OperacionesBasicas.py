# Calculadora básica
print("Welcome to basic calculator by Angel")
print("1: add")
print("2: subtract")
print("3: multiplication")
print("4: division")

operation = input("Select an operation: ")
numero1 = float(input("Enter number 1: "))
numero2 = float(input("Enter number 2: "))

if operation == "1":
    result = numero1 + numero2
elif operation == "2":
    result = numero1 - numero2
elif operation == "3":
    result = numero1 * numero2
elif operation == "4":
    if numero2 == 0:
        print("Error: cannot divide by zero")
    else:
        result = numero1 / numero2
else:
    print("Invalid option")

if operation in ("1", "2", "3", "4") and numero2 != 0:
    print(f"Result: {result}")