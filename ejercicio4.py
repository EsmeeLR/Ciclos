'''
Programa que muestra la tabla de multiplicar de los nùmeros 1,2,3,4 y 5.
'''
def mostrar_tablas_multiplicar():
    for i in range(1, 6):
        print(f"Tabla de multiplicar del {i}:")
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
        print()  # Línea en blanco para separar las tablas

# Ejecutar el programa
mostrar_tablas_multiplicar()
