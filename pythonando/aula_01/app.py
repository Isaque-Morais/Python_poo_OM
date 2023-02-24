class Usuario: 

    # cargo = 'cargo'

    def __init__(self, name, idade, altura):
        self.name = name
        self.idade = idade
        self.altura = altura
    
    def retorna_altura(self):
        print(self.altura)

    def retorna_name(self):
        print(self.name)

    # def exibe_cargo(cls):
    #     print(cls.cargo)


user_1 = Usuario('Isaque', 20, 1.75)
print(f'O seu nome é {user_1.name}, tem idade de {user_1.idade} e tem a altura de {user_1.altura}.\n')


user_2 = Usuario('Maria', 30, 1.51)
print(f'O seu nome é {user_2.name}, tem idade de {user_2.idade} e tem a altura de {user_2.altura} \n')

# user_1.retorna_name()
# user_1.retorna_altura()
# print(user_1.idade)

# print()

# user_2.retorna_name()
# user_2.retorna_altura()
# print(user_2.idade)

