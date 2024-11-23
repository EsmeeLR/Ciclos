'''
Algoritmo que pida caracteres e imprima 'VOCAL' si son vocales y 'NO VOCAL' 
en caso contrario, el programa termina cuando se introduce un espacio.
'''
def verificar_vocal():
    while True:
        caracter = input("Introduce un carácter: ").lower()
        if caracter == ' ':
            break
        elif caracter in 'aeiou':
            print("VOCAL")
        else:
            print("NO VOCAL")

# Ejecutar el programa
verificar_vocal()
