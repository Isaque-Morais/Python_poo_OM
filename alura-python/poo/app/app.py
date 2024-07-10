from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praca', 'Doces')
restaurante_mexicano = Restaurante('Mexicano', 'Gourmet')
restaurante_italiano = Restaurante('Italiano', 'Massas')

restaurante_mexicano.alterar_status()

def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()