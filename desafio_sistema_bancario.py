print(
    " CAIXA ELETRONICO ".center(38, "=")
)
print(
    " SISTEMA BANCARIO ".center(38, "=")
)

menu = """
        [1] Depositar
        [2] Sacar
        [3] Extrato
        [s] Sair

Digite: """

saldo = 0
limite = 1000
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: R$ "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

            print("".center(38, "="))
        else:
            print("Operação falhou! O valor informado é inválido.")
            print("".center(38, "="))
    elif opcao == "2":
        valor = float(input("Informe o valor desejado saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou: Você não tem saldo suficiente.")
            print("".center(38, "="))

        elif excedeu_limite:
            print("Operação falhou: Saque excede o limite diario.")
            print("".center(38, "="))

        elif excedeu_saques:
            print("Operação falhou: Número máximo de saques excedido.")
            print("".center(38, "="))

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Operação com Sucesso".center(38, " "))
            print("".center(38, "="))

        else:
            print("Operação falhou: O valor informado é inválido.")
            print("".center(38, "="))

    elif opcao == "3":
        print(" ESTRATO ".center(38, "="))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("".center(38, "="))

    elif opcao == "s":
        break

    else:
        print("Opção inválida: Por favor selecione novamente a operação desejada.")
        print("".center(38, "="))

print("".center(38, "="))