'''
Realizar un programa que pida al usuario un número entero y muestre el mismo número en binario
'''
def convertir_a_binario():
    numero = int(input("Introduce un número entero: "))
    binario = bin(numero)[2:]  # Convertir a binario y eliminar el prefijo '0b'
    print(f"El número {numero} en binario es: {binario}")

# Ejecutar el programa
convertir_a_binario()
