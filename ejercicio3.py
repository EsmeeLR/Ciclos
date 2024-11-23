'''
Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma
y la media de todos los números introducidos.
'''
print("Ingresa los nùmeros que desee")
print("Ingresa un cero para indicar que has ingresado todos los nùmeros ")
print("Se calcularà la suma y la media de todos los nùmeros ingresados")

def suma_y_media():
    suma = 0
    contador = 0
    numero = int(input("Introduce un número (0 para terminar): "))

    while numero != 0:
        suma += numero
        contador += 1
        numero = int(input("Introduce un número (0 para terminar): "))

    if contador == 0:
        print("No se han introducido números.")
    else:
        media = suma / contador
        print(f"La suma de los números introducidos es: {suma}")
        print(f"La media de los números introducidos es: {media}")

# Ejecutar el programa
suma_y_media()
