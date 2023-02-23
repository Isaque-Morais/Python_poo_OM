class Produto:

    def __init__(self, nome, preco):
        self.nome = nome        #Instancia nome
        self.preco = preco      #Instancia preco
        
    def desconto_produto(self, desconto):
        self.preco = self.preco - (self.preco * (desconto / 100))

    #Atende a instancia nome
    #Getter
    @property
    def nome(self):
        return self._nome

    #Setter
    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()


    #Atende a instancia preco
    # Getter
    @property
    def preco(self):
        return self._preco
    
    # Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))

        self._preco = valor

produto_1 = Produto('CAMISETA', 50)
produto_1.desconto_produto(10)
print(produto_1.nome, produto_1.preco)

produto_2 = Produto('CONTROLE', 'R$30')
produto_2.desconto_produto(10)
print(produto_2.nome, produto_2.preco)