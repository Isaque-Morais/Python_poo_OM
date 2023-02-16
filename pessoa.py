class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self):
        print(f'{self.nome} que tem {self.idade} de idade, está comendo.')
        self.comendo = True

    def falando(self):
        print(f'O {self.nome} está {self.falando}!!!')
        self.falando = True