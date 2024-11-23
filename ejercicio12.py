'''
Realizar un programa para determinar cuánto ahorrará una persona en un año, 
si al final de cada mes deposita cantidades variables de dinero; 
además, se quiere saber cuánto lleva ahorrado cada mes.
'''
def ahorro_anual():
    ahorro_total = 0
    ahorros_mensuales = []

    for mes in range(1, 13):
        deposito = float(input(f"Introduce la cantidad ahorrada en el mes {mes}: "))
        ahorro_total += deposito
        ahorros_mensuales.append(ahorro_total)
        print(f"Total ahorrado hasta el mes {mes}: {ahorro_total}")

    print(f"\nEl total ahorrado en el año es: {ahorro_total}")

# Ejecutar el programa
ahorro_anual()
