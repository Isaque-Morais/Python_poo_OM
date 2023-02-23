from classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()
p1 = Produto('Camiseta', 50)
p2 = Produto('Sapato', 100)
p3 = Produto('Caneca', 20)


carrinho.insert_produtos(p1)
carrinho.insert_produtos(p2)
carrinho.insert_produtos(p3)
carrinho.insert_produtos(p1)
carrinho.insert_produtos(p2)
carrinho.insert_produtos(p3)

carrinho.list_produtos()

print(carrinho.soma_total())