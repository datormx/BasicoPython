def run():
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)

    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break     
        
    # texto = input('Escribe un texto: ')
    # for letra in texto:
    #     if letra == 'o':
    #         break
    #     print(letra)

    print('Adivina la letra secreta.\nTienes 5 intentos.')
    intentos = 0
    
    while intentos < 5: 
        letra = input('¿Cuál es la letra secreta?: ')
        intentos+=1
        if letra == 'k':
            print('Le atinaste. La letra secreta es K.')
            break
        if intentos == 5:
            print('Lo siento. Perdiste')



if __name__ == "__main__":
    run()