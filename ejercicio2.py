#Pedir a la computadora que genere un numero ramdom entre 1 a 100
aleatorio = random.randint(1,100)
intentos_res = 10
for intento in range(1,11):
    num_ingresado = int(input("Ingrese cualquier número entero entre 1 y 100 para adivinar el número generado:"))
    intento=-1
    if (num_ingresado>=1) and (num_ingresado <=100):
        if num_ingresado == aleatorio:
            print(f"Has adivinado el nùmero en",(10-intento),"intentos")
        elif num_ingresado > aleatorio:
            print("El nùmero", num_ingresado, "es mayor al aleatorio, intenta de nuevo")
        elif num_ingresado < aleatorio:
            print("El nùmero", num_ingresado, "es menor al aleatorio, intenta de nuevo")
    else:
        print("Ingrese un nùmero vàlido entre 1 y 100")
if intento == 10:
    print("Lo siento, intentos agotados")
print("FIN")