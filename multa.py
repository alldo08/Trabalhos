minima = 80

while True:
    try:
        valor = int(input('Qual é a sua velocidade? '))
        break
    except ValueError:
        print('Apenas números.')

amais = valor - minima

if valor <= minima:
    print('Sem multa.')
else:
    multa = amais * 7
    print('Sua velocidade está {} km/h acima do limite máximo de 80 km/h.'.format(amais))
    print('Sua multa é de R${},00'.format(multa))
