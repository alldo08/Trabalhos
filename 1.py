import random

class ChuteNumero:

    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 0
        self.valor_maximo = 0
        self.tentar_novamente = True

    def Iniciar(self):
        self.PedirMinimo()
        self.PedirMaximo()
        self.GerarAleatorio()
        self.PedirValor()
        try:
            while self.tentar_novamente:
                if int(self.valor_do_chute) > self.valor_aleatorio:
                    print('Chute valor mais baixo')
                    self.PedirValor()
                elif int(self.valor_do_chute) < self.valor_aleatorio:
                    print('Chute Valor mais alto')
                    self.PedirValor()
                if int(self.valor_do_chute) == self.valor_aleatorio:
                    self.tentar_novamente = False
                    print('Acertou')
        except ValueError:
            print('Entrada inválida. Digite um número inteiro válido.')
            self.Iniciar()

    def PedirMinimo(self):
        while True:
            try:
                self.valor_minimo = int(input('Valor mínimo: '))
                break
            except ValueError:
                print('Entrada inválida. Digite um número inteiro válido.')

    def PedirMaximo(self):
        while True:
            try:
                self.valor_maximo = int(input('Valor máximo: '))
                break
            except ValueError:
                print('Entrada inválida. Digite um número inteiro válido.')

    def PedirValor(self):
        while True:
            try:
                self.valor_do_chute = int(input('Chute um número: '))
                break
            except ValueError:
                print('Entrada inválida. Digite um número inteiro válido.')

    def GerarAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)


chute = ChuteNumero()
chute.Iniciar()
