from Cliente import Cliente
from Conta import Conta

def criar_cliente():
    nome = input("Insira o nome do cliente: ")
    telefone = input("Insira o telefone do cliente: ")
    return Cliente(nome, telefone)

def criar_conta(cliente):
    numero = input("Insira o número da conta: ")
    saldo_inicial = float(input("Insira o saldo inicial da conta: "))
    return Conta(cliente.get_nome(), numero, saldo_inicial)

def menu():
    print("\nOpções:")
    print("1: Depósito")
    print("2: Saque")
    print("3: Exibir Extrato")
    print("4: Sair")
    return input("Escolha uma opção: ")

def main():
    print("Bem-vindo ao sistema bancário!")

    cliente = criar_cliente()
    conta = criar_conta(cliente)

    while True:
        opcao = menu()

        if opcao == "1":
            try:
                valor = float(input("Insira o valor do depósito: "))
                conta.deposita(valor)
            except ValueError:
                print("Valor inválido para depósito!")

        elif opcao == "2":
            try:
                valor = float(input("Insira o valor do saque: "))
                conta.saque(valor)
            except ValueError:
                print("Valor inválido para saque!")

        elif opcao == "3":
            conta.extrato()

        elif opcao == "4":
            print("Saindo do sistema. Até mais!")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
