class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def insert_produtos(self, produto):
        self.produtos.append(produto)

    def list_produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total

    def remove_produto(self):
        del self.produtos

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor