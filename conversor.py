def conversor(tipo_pesos, valor_dolar):
    pesos = float(input('Escribe el valor de pesos' + tipo_pesos + ': '))
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + " dólares.")

menu = """
Bienvenido al conversor de monedas 💲😃

1 - Pesos Colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opcion: """

opcion = input(menu)

if opcion == '1':
    conversor('colombianos', 3875)
elif opcion == '2':
    conversor('argentinos', 65)
elif opcion == '3':
    conversor('mexicanos', 24)
else:
    print('Ingresa una opción correcta.')


# dolares = float(input('Escribe el valor de dólares: '))

# valor_mxn = 0.044
# mxn = dolares / valor_mxn
# mxn = round(mxn, 2)
# mxn = str(mxn)
# print('Tienes $' + mxn + " pesos mexicanos.")

