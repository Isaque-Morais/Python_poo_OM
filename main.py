class Pessoa():

    ano_atual = 2019

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def get_ano_nascimeto(self):
        print(self.ano_atual - self.idade)
    
    @classmethod
    #cls passado por parametro na função indica que pode usar atributos da classe
    def por_ano_nascimeto(cls, nome, ano_nascimeto):
        idade = cls.ano_atual - ano_nascimeto
        return cls(nome, idade)

#Criando a intancia
pessoa_1 = Pessoa.por_ano_nascimeto('Isaque', 1999)
print(pessoa_1)
print(pessoa_1.nome, pessoa_1.idade)
pessoa_1.get_ano_nascimeto()