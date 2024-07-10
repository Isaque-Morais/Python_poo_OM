class Conta:

    def  __init__(self, titular = '', saldo = 0) -> None:
        self.titular = titular
        self.saldo = saldo
        self.ativo = False

    def __str__(self) -> str:
            estado_conta = 'ativada' if self.ativo else 'inativa'
            return f'O titular da conta é {self.titular}, e seu saldo é {self.saldo} é sua conta está {estado_conta}'
    
    def ativa_conta(self):
        self.ativo = not self.ativo


one_conta = Conta('Isaque', saldo=200)
one_conta.ativa_conta()

two_conta = Conta('Amanda', saldo=500)
two_conta.ativa_conta()

print(one_conta)
print(two_conta)