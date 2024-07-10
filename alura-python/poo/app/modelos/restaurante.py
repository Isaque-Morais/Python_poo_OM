from modelos.avaliacao import Avaliacao

class Restaurante: 

    restaurantes = []

    #Metados especiais no PYTHON (__init__, __str__)
    # Esse init é o contrutor do metodo 
    # self serve para intanciar os metodos dentro do contrutor

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        #atributo privado, por convencao usamos _ 
        self._ativo = False
        #Aqui ele cria um lista de restaurantes toda vez que for criado um restaurante 
        self._avalicao = []
        Restaurante.restaurantes.append(self)
    
    #Esse metodo serve para retornar em string o objeto criado
    def __str__(self) -> str:
        return f'Nome: {self._nome} | Categoria: {self._categoria} | Ativo: {self._ativo}'
    
    # Meu metédo 

    def  listar_restaurantes():
        print(f'{"Nome do Restaurante".ljust(25)} | {"Categoria". ljust(25)} | {"Status"}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante._ativo}')

    @property
    def ativo(self):
         return 'verdadeiro' if self._ativo else 'false'

    def alterar_status(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao()

         

# restaurante_praca = Restaurante('Fazenda', 'Italiana') #crio meu objeto
# restaurante_praca.alterar_status()

# restaurante_pizza = Restaurante('Pizzaria do Zé', 'Brasileira')#crio meu objeto
# restaurante_pizza.alterar_status()

# a funcao vars() serve para imprimir meu objeto criado

# Restaurante.listar_restaurantes()

# if restaurante_praca.ativo:
#     print(f'Restaurante: {restaurante_praca.nome} está ativo!!\n')
# else: 
#     print(f'Restaurante:  {restaurante_praca.nome} está inativo!!')

# if restaurante_pizza.ativo: 
#     print(f'Restaurante: {restaurante_pizza.nome} está ativo!!\n')
# else: 
#         print(f'Restaurante:  {restaurante_pizza.nome} está inativo!!')

