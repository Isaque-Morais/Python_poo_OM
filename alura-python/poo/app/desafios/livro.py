class Livro: 

    def __init__(self, titulo, autor, ano_publicacao) -> None:
        self.titulo = titulo
        self.autor = autor 
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
    
    def __str__(self) -> str:
        status = "Disponível" if self.disponivel else "Indisponível"
        return f'Olá, esse livro tem o titulo de {self.titulo}, e foi criado pelo autor:{self.autor} e teve seu ano de publicação em {self.ano_publicacao}. O status do livre é de {status}'
    
    def emprestar_livro(self):
        self.disponivel = not self.disponivel

    @staticmethod
    def verificar_disponibilidade(ano): 
        livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]
        return livros_disponiveis

livro_um = Livro('A fera', 'Machado de Assis', 1998)
livro_dois = Livro('Eterno', 'Mack', 2019)
livro_tres = Livro('Cobol', 'Fernando', 2024)

Livro.livros = [livro_um, livro_dois, livro_tres]  # Adicionando os livros à lista de livros


