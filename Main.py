class Main:
    pass

print("Testando Projeto")

from Cliente import Cliente
from Conta import Conta

c1 = Cliente("Jão", "8888-8888")
conta=Conta(c1.,4545,0)

print(c1)
print(c1.nome, " e ", c1.telefone)
print(conta.titular," Numero: ", conta.numero, "Seu saldo: ", conta.saldo)

