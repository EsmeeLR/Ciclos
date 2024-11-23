'''
Escribe un programa que dados dos números, uno real (base) y un entero positivo 
(exponente), saque por pantalla el resultado de la potencia. No se puede 
utilizar el operador de potencia.
'''
def calcular_potencia(base, exponente):
    resultado = 1
    for _ in range(exponente):
        resultado *= base
    return resultado

# Solicitar la base y el exponente al usuario
base = float(input("Introduce la base (número real): "))
exponente = int(input("Introduce el exponente (entero positivo): "))

# Asegurarse de que el exponente es positivo
if exponente < 0:
    print("El exponente debe ser un entero positivo.")
else:
    resultado = calcular_potencia(base, exponente)
    print(f"El resultado de {base} elevado a {exponente} es: {resultado}")
