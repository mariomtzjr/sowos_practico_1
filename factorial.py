import sys
# Factorial
# n*(n-1)

numero = sys.argv[1]

def factorial(numero):
    if len(sys.argsv) > 2:
        print("Solo debes ingresar un número")
    else:
        if numero == 0 or numero == 1:
            return 1
        else:
            return (numero*factorial(numero - 1))
