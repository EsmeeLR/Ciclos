'''
Mostrar en pantalla los N primero números primos. Se pide por teclado la cantidad 
de números primos que queremos mostrar.
'''
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def primeros_n_primos(n):
    primos = []
    numero = 2
    while len(primos) < n:
        if es_primo(numero):
            primos.append(numero)
        numero += 1
    return primos

# Solicitar la cantidad de números primos al usuario
n = int(input("Introduce la cantidad de números primos que deseas mostrar: "))

# Obtener y mostrar los primeros N números primos
primos = primeros_n_primos(n)
print(f"Los primeros {n} números primos son: {primos}")
