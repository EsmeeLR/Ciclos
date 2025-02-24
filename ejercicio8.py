'''
Escribir un programa que imprima todos los números pares entre dos números que 
se le pidan al usuario.
'''
def imprimir_pares():
    inicio = int(input("Introduce el primer número: "))
    fin = int(input("Introduce el segundo número: "))

    if inicio > fin:
        inicio, fin = fin, inicio  # Intercambiar si el inicio es mayor que el fin

    print(f"Números pares entre {inicio} y {fin}:")
    for numero in range(inicio, fin + 1):
        if numero % 2 == 0:
            print(numero)

# Ejecutar el programa
imprimir_pares()
