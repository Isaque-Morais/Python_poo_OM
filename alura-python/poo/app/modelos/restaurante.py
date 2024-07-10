from modelos.avaliacao import Avaliacao

class Restaurante: 

    restaurantes = []


    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avalicao = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self) -> str:
        return f'Nome: {self._nome} | Categoria: {self._categoria} | Ativo: {self._ativo}'
    

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









