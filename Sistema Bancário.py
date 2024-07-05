
#criando um sistema bancário com python


menu = """

    [d] Depositar
    [s] sacar
    [e] extrato
    [q] sair


"""

saldo = 0
limite = 500
extrato = " "
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("informe quanto quer depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Despósito: R$ {valor: .2f}\n"
        else:
            print("Operação cancelada. Valor inválido.")
        
    elif opcao == "s":
        valor = float(input("digite o quanto quer sacar: "))

        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite        
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação cancelada. Você não possui saldo suficiente.")
        
        elif excedeu_limite:
            print("Operação cancelada. Você não possui limite suficiente.")

        elif excedeu_saques:
            print("Operação cancelada. Você excedeu o número de saques permitidos.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1 # incrementa um valo ao saque para verificar se já foram 3.
        
        else:
            print("Operação falhou. Valor inválido")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas nenhuma movimentação." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===========================================")
    
    elif opcao == "q":
        print("Obrigado por usar nossos serviços.")
        break

    else:
        ("operação inválida. Tente novamente.")