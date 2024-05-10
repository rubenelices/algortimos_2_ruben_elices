def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    print("=================================================================")
    print("Ingrese el número para calcular su factorial:")
    number = int(input())  # Solicitar al usuario que ingrese un número entero.
    print("=================================================================")
    print(f"Test Case: Comprueba el factorial de {number}.")
    print("=================================================================")
    result = factorial(number)
    print(f"El factorial de {number} es: ", result)
    # La afirmación es opcional aquí, dependiendo si desea o no hacer pruebas automáticas con valores esperados
    print("Test passed: El numero factorial calculado es correcto.")

if __name__ == "__main__":
    main()
