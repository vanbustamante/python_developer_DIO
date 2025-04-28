"""
    Código simulando o sistema de um banco com opções de depósito, saque e extrato. 
    Depósito: apenas valores positivos. Deve ser exibido no extrato.
    Saque: 3 saques diários com limite máximo de R$500,00 por saque. Deve ser exibido no extrato.
    Extrato: Lista todos os depósitos e saques feitos. No final, exibir o saldo atual da conta. 
             Se nenhuma operação for feita, exibir "Não foram realizadas movimentações." Valores exibidos
             como R$ XXXX.XX
"""

menu = """
---------------------------
Digite qual operação deseja fazer:

[1] Depósito
[2] Saque
[3] Extrato

[0] Sair

---------------------------
=> """

saldo = 0
extrato = ""
numero_saques = 0
limite_saques = 3
limite_por_saque = 500

while True:
    operacao = input(menu)

    if operacao == "1":
        deposito = float(input("Informe o valor do depósito: R$ "))

        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito R$ {deposito:.2f}\n"
        
        else:
            print("""Operação falhou. O valor informado é inválido.\nVoltando ao menu principal...""")
            
    elif operacao == "2":
        saque = float(input("Informe o valor a ser sacado: R$ "))

        if saque > limite_por_saque:
            print("""Operação falhou. O valor máximo por saque é de R$ 500,00.\nVoltando ao menu principal...""")
        
        elif saque > saldo:
            print("""Operação falhou. O saldo não é suficiente.\nVoltando ao menu principal...""")
        
        elif numero_saques >= limite_saques:
            print("""Operação falhou. O limite de 3 saques por dia já foi atingido.\nVoltando ao menu principal...""")
            
        elif saque > 0:
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            numero_saques += 1

        else:
            print(f"""Operação falhou. O valor {saque:.2f} é inválido.\nVoltando ao menu principal...""")
        
    elif operacao == "3":
        print("\n--------- EXTRATO ---------")
        if extrato == "":
            print("\nNão foram realizadas movimentações.\n\n---------------------------")
        else:
            print(f"\n{extrato}")
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("\n---------------------------")
        
    elif operacao == "0":
        break

    else:
        print("""Operação inválida. Por favor, selecione novamente.\nVoltando ao menu principal...""")
