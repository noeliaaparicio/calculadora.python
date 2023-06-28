def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: división por cero"

# Función principal de la calculadora
def calcular():
    print("Calculadora de Python")
    print("----------------------")

    while True:
        print("Operaciones disponibles:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        opcion = input("Selecciona una operación (1-5): ")

        if opcion == "5":
            break

        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if opcion == "1":
            resultado = suma(num1, num2)
            print("El resultado es:", resultado)
        elif opcion == "2":
            resultado = resta(num1, num2)
            print("El resultado es:", resultado)
        elif opcion == "3":
            resultado = multiplicacion(num1, num2)
            print("El resultado es:", resultado)
        elif opcion == "4":
            resultado = division(num1, num2)
            print("El resultado es:", resultado)
        else:
            print("Opción inválida. Inténtalo nuevamente.")

calcular()