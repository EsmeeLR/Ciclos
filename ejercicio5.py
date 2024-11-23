'''
Programa que pida 10 números e imprima el promedio de estos.

Se utilizan los conceptos del programa anterior de contador y acumulador.
'''
def calcular_promedio():
    suma = 0
    contador = 0

    for _ in range(10):
        numero = float(input("Introduce un número: "))
        suma += numero
        contador += 1

    promedio = suma / contador
    print(f"El promedio de los números introducidos es: {promedio}")

# Ejecutar el programa
calcular_promedio()
