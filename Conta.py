class Conta:
    def __init__(self, titular, numero, saldo=0.0):
        self._saldo = saldo
        self._numero = numero
        self._titular = titular

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            print("O saldo não pode ser negativo!")
        else:
            self._saldo = saldo

    def saque(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente!")

    def deposita(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Depósito realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo!")

    def extrato(self):
        print(f"Cliente: {self._titular} | Conta Número: {self._numero} | Saldo Atual: {self._saldo:.2f}")
