""""
public, protected, private
_  Protected / Public
__ Private (Pode acessar o atributo com _NOMECLASSE_nomeatributo)

"""

class BaseDeDados:
    def __init__(self):
        self._dados = {}
    
    @property
    def dados(self):
        return self.__dados
    
    def insert_client(self, id, name):
        if 'client' not in self._dados:
            self._dados['client'] = {id: name}
        else:
            self._dados['client'].update({id: name})
    
    def list_clients(self):
        for id, name in self._dados['client'].items():
            print(id, name)

    def delete_client(self, id):
        del self._dados['client'][id]

bd = BaseDeDados()

bd.insert_client(1 , 'Isaque')
bd.insert_client(2 , 'Morais')
bd.insert_client(3 , 'Maria')
bd.insert_client(4 , 'Bene')
# bd.delete_client(2)
bd.list_clients()

# print(bd.dados)