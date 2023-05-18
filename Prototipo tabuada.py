import math

n1 = int(input('Qual número você quer saber a tabuada? '))
n2 = int(input('Até quanto você quer saber a tabuada? '))

print('A tabuada de {} é:'.format(n1))
for i in range(1, n2 + 1):
    resultado = n1 * i
    print('\n{} x {} = {}'.format(n1, i, resultado), end=' ')

print('Obrigado por usar a máquina de tabuada.')
