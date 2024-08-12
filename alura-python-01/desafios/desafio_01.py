print("Python na Escola de Programação da Alura")

nome = input("Digite seu nome: ")

idade = input("Digite sua idade:")


print(f'Meu nome é {nome} e tenho {idade} anos!!')


print("""
A
L
U
R
A
""")

termos = float(input("Informe um valor para calcular pi:"))

pi = 3.14
i = 0
while i < termos:
    pi += ((-1) ** i) / (2 * i + 1)
    i += 1
pi *= 4
print(pi)