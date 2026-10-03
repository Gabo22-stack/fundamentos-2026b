import math

print("Calculadora de áreas y perímetros")
print("1. Cuadrado")
print("2. Rectángulo")
print("3. Triángulo")
print("4. Circunferencia")
print("5. Salir")

while True:
    opcion = int(input("\nElige una figura (1-5): "))

    if opcion == 5:
        print("Adiós")
        break

    if opcion == 1:
        lado = float(input("Ingresa el lado del cuadrado: "))
        area = lado ** 2
        perimetro = 4 * lado
        print(f"Área: {area}")
        print(f"Perímetro: {perimetro}")

    elif opcion == 2:
        base = float(input("Ingresa la base del rectángulo: "))
        altura = float(input("Ingresa la altura del rectángulo: "))
        area = base * altura
        perimetro = 2 * (base + altura)
        print(f"Área: {area}")
        print(f"Perímetro: {perimetro}")

    elif opcion == 3:
        base = float(input("Ingresa la base del triángulo: "))
        altura = float(input("Ingresa la altura del triángulo: "))
        lado1 = float(input("Ingresa el primer lado del triángulo: "))
        lado2 = float(input("Ingresa el segundo lado del triángulo: "))
        lado3 = float(input("Ingresa el tercer lado del triángulo: "))
        area = (base * altura) / 2
        perimetro = lado1 + lado2 + lado3
        print(f"Área: {area}")
        print(f"Perímetro: {perimetro}")

    elif opcion == 4:
        radio = float(input("Ingresa el radio de la circunferencia: "))
        area = math.pi * radio ** 2
        perimetro = 2 * math.pi * radio
        print(f"Área: {area}")
        print(f"Perímetro (circunferencia): {perimetro}")

    else:
        print("Opción inválida. Intenta nuevamente.")
