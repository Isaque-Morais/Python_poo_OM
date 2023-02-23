from classes import Cliente, Endereco

cliente_1 = Cliente('Isaque', 30)
cliente_1.insere_endereco('São Paulo', 'SP')
print(cliente_1.nome)
cliente_1.lista_enderecos()
print()

cliente_2 = Cliente('Ana', 30)
cliente_2.insere_endereco('Salvador', 'BA')
cliente_2.insere_endereco('Amapá', 'AM')
print(cliente_2.nome)
cliente_2.lista_enderecos()
print()


cliente_3 = Cliente('Julia', 30)
cliente_3.insere_endereco('Minas Gerais', 'MG')
cliente_3.insere_endereco('Amapá', 'AM')
print(cliente_3.nome)
cliente_3.lista_enderecos()
print()
