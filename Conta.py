class Conta:
    def __init__(self, titular, numero, saldo):
        self.titular = titular
        self.numero = numero
        self._saldo = saldo


    def get_saldo(self):
        return self._saldo


    def set_saldo(self, saldo):
        if saldo < 0:
            print("O saldo nao pode ser negativo")
        else:
            self._saldo = saldo


    def saque(self, valor):
        if self._saldo>=valor:
            self._saldo-=valor
            print("Saque Realizado com sucesso!")
        else:
            print("Saldo insuficiente")


    def deposita(self, valor):
        self._saldo+=valor


    def extrato(self):
        print("Cliente: ", self.titular, " Saldo Atual: ", self._saldo)