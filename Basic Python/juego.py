import random



def run():
    numero_aleatorio = random.randint(1,100)
    numero_elegido = int(input("Ingrese el numero del 1 al 100: "))

    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("Error, escoge un numero más grande.")
        else:
            print("Error, escoge un numero más pequeño.")
        
        numero_elegido = int(input("Ingrese otro numero: "))
        
    print ("Felicidades, ganaste el numero era" ,str(numero_aleatorio))
            
if __name__ == '__main__':
    run()