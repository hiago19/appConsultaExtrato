class Main:
    pass

print("Testando Projeto")

from Cliente import Cliente
from Conta import Conta

c1 = Cliente("Jão", "8888-8888")
conta=Conta(c1.get_nome(), 4545, 0)

'''
print(c1)
print(c1.nome, " e ", c1.telefone)
print(conta.titular," Numero: ", conta.numero, "Seu saldo: ", conta.saldo)
'''
conta.deposita(int(input("Insira o valor depositado: ")))
conta.saque(int(input("Insira o valor do saque: ")))
conta.extrato()
