class Pessoa:
    def __init__(self, nome = '', idade = 0, profissao = ''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self) -> str:
        return f'{self.nome}, tenho {self.idade} anos, e minha profissão é {self.profissao}.'
    
    def  aniversario(self):
        self.idade += 1
    
    def  saudacao(self):
        if self.profissao:
            print(f'Seja bem vindo {self.nome}, sua profissão é {self.profissao}!')
        else: 
            print(f'Olá {self.nome}!')
    

one_pessoa = Pessoa('Isaque', 21, 'Desenvolvedor')
one_pessoa.aniversario()
one_pessoa.saudacao()
print(one_pessoa)
