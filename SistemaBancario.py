class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso!")
            else:
                print("Saldo insuficiente para saque.")
        else:
            print("Valor inválido para saque.")

    def consultar_saldo(self):
        print(f"Saldo de {self.titular}: R${self.saldo:.2f}")

def exibir_menu():
    print("\nSistema Bancário")
    print("1. Criar conta")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Consultar saldo")
    print("5. Sair")

def main():
    conta = None  

    while True:
        exibir_menu()

        opcao = input("Escolha uma opção (1/2/3/4/5): ")

        if opcao == "1":
            if conta:
                print("Conta já criada!")
            else:
                nome = input("Digite o nome do titular da conta: ")
                saldo_inicial = float(input("Digite o valor do depósito inicial (R$): "))
                conta = ContaBancaria(nome, saldo_inicial)
                print(f"Conta criada com sucesso para {nome} com saldo inicial de R${saldo_inicial:.2f}.")

        elif opcao == "2":
            if conta:
                valor_deposito = float(input("Digite o valor a ser depositado: R$"))
                conta.depositar(valor_deposito)
            else:
                print("Você precisa criar uma conta primeiro!")

        elif opcao == "3":
            if conta:
                valor_saque = float(input("Digite o valor a ser sacado: R$"))
                conta.sacar(valor_saque)
            else:
                print("Você precisa criar uma conta primeiro!")

        elif opcao == "4":
            if conta:
                conta.consultar_saldo()
            else:
                print("Você precisa criar uma conta primeiro!")

        elif opcao == "5":
            print("Saindo... Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

main()
