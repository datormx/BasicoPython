import random

def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input('Elige un número del 1 al 100: '))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('Busca un número mayor.')
        else:
            print('Busca un número más pequeño.')            
        numero_elegido = int(input('Elige otro número: '))
    print('\n¡Ganaste!. El número era ' + str(numero_aleatorio))


if __name__ == "__main__":
    run()