"""
Crea una programa que pida un número y calcule su factorial (El factorial de 
un número es el producto de todos los enteros entre 1 y el propio número y se 
representa por el número seguido de un signo de exclamación. 
Por ejemplo 5! = 1x2x3x4x5=120)
"""
#Solicitamos al usuario que ingrese un entero para saber su factorial
a = int(input("Ingresa el entero del que deseas saber su factorial: "))
factorial = 1

# Calcular el factorial usando un ciclo
for i in range(1, a + 1):
    factorial *= i

# Mostrar el resultado
print("El factorial de",a, "es", factorial)
