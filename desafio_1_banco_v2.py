"""
    Código simulando o sistema de um banco com opções de depósito, saque e extrato, adicionando os conhecimentos
    sobre data e hora. Máximo e 10 transações diárias para uma conta. 
    Depósito: apenas valores positivos. Deve ser exibido no extrato.
    Saque: limite máximo de R$500,00 por saque. Deve ser exibido no extrato.
    Extrato: Lista todos os depósitos e saques feitos. No final, exibir o saldo atual da conta. 
             Se nenhuma operação for feita, exibir "Não foram realizadas movimentações." Valores exibidos
             como R$ XXXX.XX. Mostrar data e hora de todas as transações.
"""

from datetime import datetime

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
numero_operacoes = 0
limite_operacoes = 10
limite_por_saque = 500

while True:
    operacao = input(menu)

    if operacao == "1":
        deposito = float(input("Informe o valor do depósito: R$ "))
        data_hora_operacao = datetime.now()
        mascara_data = "%d/%m/%Y %H:%M"

        if numero_operacoes >= limite_operacoes:
            print("""Operação falhou. O limite de 10 operações por dia já foi atingido.\nPor favor, volte amanhã.""")

        elif deposito > 0:
            saldo += deposito
            extrato += f"{data_hora_operacao.strftime(mascara_data)} - Depósito R$ {deposito:.2f}\n"
            numero_operacoes += 1

        else:
            print("""Operação falhou. O valor informado é inválido.\nVoltando ao menu principal...""")
            
    elif operacao == "2":
        saque = float(input("Informe o valor a ser sacado: R$ "))
        data_hora_operacao = datetime.now()
        mascara_data = "%d/%m/%Y %H:%M"

        if saque > limite_por_saque:
            print("""Operação falhou. O valor máximo por saque é de R$ 500,00.\nVoltando ao menu principal...""")
        
        elif saque > saldo:
            print("""Operação falhou. O saldo não é suficiente.\nVoltando ao menu principal...""")
        
        elif numero_operacoes >= limite_operacoes:
            print("""Operação falhou. O limite de 10 operações por dia já foi atingido.\nPor favor, tente novamente amanhã.""")
            
        elif saque > 0:
            saldo -= saque
            extrato += f"{data_hora_operacao.strftime(mascara_data)} - Saque: R$ {saque:.2f}\n"
            numero_operacoes += 1

        else:
            print(f"""Operação falhou. O valor R${saque:.2f} é inválido.\nVoltando ao menu principal...""")
        
    elif operacao == "3":
        data_hora_operacao = datetime.now()
        mascara_data = "%d/%m/%Y %H:%M"
        print("\n--------- EXTRATO ---------")
        print(f"\n{data_hora_operacao.strftime(mascara_data)}")
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
