print("Conversion de unidades")
print("1. Celsius, kelvin, Fahrenheit")
print("2. Km a millas")
print("3. kg a libras")
print("4.  dolares a pesos")
print("5. Salir")

while True:
    opcion = int(input("\nElige una opción (1-5): "))

    if opcion == 5:
        print("Adiós")
        break

    if opcion == 1:
        celsius = float(input("Ingresa la temperatura en Celsius: "))
        kelvin = celsius + 273.15
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C = {kelvin} K")
        print(f"{celsius}°C = {fahrenheit}°F")

    elif opcion == 2:
        km = float(input("Ingresa la distancia en kilómetros: "))
        millas = km * 0.621371
        print(f"{km} km = {millas} millas")

    elif opcion == 3:
        kg = float(input("Ingresa el peso en kilogramos: "))
        libras = kg * 2.20462
        print(f"{kg} kg = {libras} libras")

    elif opcion == 4:
        dolares = float(input("Ingresa la cantidad en dólares: "))
        pesos = dolares * 20.0  # Suponiendo un tipo de cambio de 1 USD = 20 MXN
        print(f"{dolares} USD = {pesos} MXN")

    else:
        print("Opción inválida. Intenta nuevamente.")