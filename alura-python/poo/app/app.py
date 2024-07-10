from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praca', 'Doces')

restaurante_praca.receber_avaliacao('Tobias', 9.5)
restaurante_praca.receber_avaliacao('Isais', 7)
restaurante_praca.receber_avaliacao('Lu', 5.8)
restaurante_praca.receber_avaliacao('Luiza', 3)


restaurante_praca.alterar_status()


def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()