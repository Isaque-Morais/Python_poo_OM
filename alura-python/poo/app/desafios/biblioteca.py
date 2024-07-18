from livro import Livro

livro_biblioteca = Livro("Django", "Castro", 2018) 

print(livro_biblioteca)

print(f"Antes de emprestar (biblioteca): Livro disponível? {livro_biblioteca.disponivel}")
livro_biblioteca.emprestar_livro()
print(f"Depois de emprestar (biblioteca): Livro disponível? {livro_biblioteca.disponivel}")


ano_especifico = 2018
livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico)
print(f"Livros disponíveis em {ano_especifico}: {livros_disponiveis_ano}")