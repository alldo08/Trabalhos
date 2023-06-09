while True:
    try:
        ano = int(input('Insira ano:'))
        break
    except ValueError:
        print('Apenas numeros.')

if ano % 4 == 0:
    print('Ano bissexto')
else:
    print('Nao bissexto.')