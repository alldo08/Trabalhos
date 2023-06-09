while True:
    try:
        sem_desconto = float(input('Valor Km em viagens menores que 200km.'))
        break
    except ValueError:
        print('Apenas numeros')

while True:
    try:
        desconto = float(input("Valor Km em viagens maiores que 200 KM."))
        break
    except ValueError:
        print('Apenas numeros.')
while True:
    try:
        distancia = float(input('Quantos Km de distancia? '))
        break
    except ValueError:
        print('Apenas numeros')
sdesconto = distancia * sem_desconto
cdesconto = distancia * desconto
if  distancia <= 200:
    print('Distância menor que 200km, Você pagara R${} por KM'.format(sem_desconto))
    print('{}Km'.format(distancia))
    print('Pagará:R${:.2f} por {:.2f}KM'.format(sdesconto, distancia))
else:
    print('Distância maior que 200km, Você pagara R${} por KM'.format(desconto))
    print('{}Km'.format(distancia))
    print('Pagará:R${:.2f} por {:.2f}KM'.format(cdesconto, distancia))
