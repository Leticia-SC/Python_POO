class Main:
    pass

from Cliente import Cliente
from Conta import Conta

c1 = Cliente("Letícia", "13997972103")
conta = Conta(c1.get_nome(),6565,0)

conta.deposita(100)
conta.saque(40)
conta.extrato()
