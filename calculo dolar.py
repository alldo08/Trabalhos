class Dollar:
    def __init__(self):
        self.n1 = '0'
        self.n2 = '0'

    def iniciar(self):
        while True:
            try:
                self.n1 = float(input('Quantos R$ você tem? '))
                break
            except ValueError:
                print('Apenas números com . (ponto)')

        while True:
            try:
                self.n2 = float(input('Valor do Dólar U$? '))
                break
            except ValueError:
                print('Apenas números com . (ponto)')

        print('Com R$:{:.2f} reais você pode comprar: U$:{:.2f} dólares'.format(self.n1, self.n1 / self.n2), end=' ')
        print('Obrigado')


inicio = Dollar()
inicio.iniciar()
