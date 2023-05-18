while True:
    try:
        n1 = float(input('Valor de salario: '))
        break
    except ValueError:
        print('Apenas números')

while True:
    try:
        n2 = float(input('Procentagem de aumento: '))
        break
    except ValueError:
        print('Apenas números')

print('Com o salário de R$ {:.2f} e com {}% de aumento, seu salário será: R$ {:.2f}'.format(n1, n2, n1 + (n1 * (n2 / 100))))
