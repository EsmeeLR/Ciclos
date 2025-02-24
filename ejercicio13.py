'''
Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 
euros, el segundo 20 euros, el tercero 40 euros y así sucesivamente. 
Realizar un programa para determinar cuánto debe pagar mensualmente y el total 
de lo que pagó después de los 20 meses.
'''
def calcular_pagos():
    total_pagado = 0
    pago_mensual = 10

    for mes in range(1, 21):
        print(f"Mes {mes}: {pago_mensual} euros")
        total_pagado += pago_mensual
        pago_mensual *= 2

    print(f"\nTotal pagado después de 20 meses: {total_pagado} euros")

# Ejecutar el programa
calcular_pagos()
