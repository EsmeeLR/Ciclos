"""
CICLO FOR
Permite realizar una serie de instrucciones 
una cantidad determinada de veces

Estructura:
for i in [1...n]:
    intrucciones

range(fin) 
    range(3)    [0, 1, 2]
range(inicio, fin)
    range(4,7)  [4,5,6]
range(inicio, fin, pasos)
    range(2,9,2)    [2, 4, 6, 8]
"""
# Ejemplo: Imprimir los números del 1 al 10
for i in range(10): 
    print(f"Num: { i + 1}, vuelta { i }")
# Ejemplo: Imprimir los números del 10 al 20
for i in range(10,20): 
    print(f"Num: { i + 1}")