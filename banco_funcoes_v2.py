"""
    Código simulando o sistema de um banco com opções de depósito, saque e extrato, agora como funções.
    Adicionar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancária.
    Depósito: Apenas valores positivos. Deve ser exibido no extrato.
              A função deve receber argumentos apenas por posição (positional only). Sugestão de argumentos:
              saldo, valor, extrato. Sugestão de retorno: saldo e extrato.
    Saque: Limite de 3 saques diários com limite máximo de R$500,00 por saque. Deve ser exibido no extrato.
           A função deve receber os argumentos apenas por nome (keyword only). Sugestão de argumentos: saldo, valor,
           extrato, numero_saques, limite_saques. Sugestão de retorno: saldo, extrato.
    Extrato: Lista todos os depósitos e saques feitos. No final, exibir o saldo atual da conta. 
             Se nenhuma operação for feita, exibir "Não foram realizadas movimentações." Valores exibidos
             como R$ XXXX.XX.
             A função deve receber argumentos por posição (saldo) e por nome (extrato).
    Novas funções:
        Criar usuário: Armazena os usuários em uma lista composta por nome, data de nascimento, CPF e endereço (string
                       com: logradouro, nro - bairro - cidade/sigla estado). Deve ser armazenado somente os números 
                       do CPF. Não pode cadastrar 2 usuários com mesmo CPF.
        Criar conta corrente: Armazena as contas em uma lista composta por agência (sempre 0001), número da conta (sequencial,
                              iniciando em 1), e usuário. Um usuário pode ter mais de uma conta, mas uma conta pertence somente
                              a um usuário.
        Listar contas: para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para
                       cada usuário da lista. Liste a conta com nome, CPF, agência e conta.
"""

import textwrap

def menu():
    menu = """
    -------------- MENU --------------
    Digite qual operação deseja:

    [1]\tDepósito
    [2]\tSaque
    [3]\tExtrato
    [4]\tNovo Usuário
    [5]\tNova Conta
    [6]\tListar Contas

    [0] Sair

    ----------------------------------
    => """
    
    return input(textwrap.dedent(menu))

def depositar(saldo, deposito, extrato, /):
    if deposito > 0:
            saldo += deposito
            extrato += f"Depósito:\tR$ {deposito:.2f}\n"
            print("\n|===| Depósito realizado com suscesso.\n|----------Voltando ao menu principal...")
        
    else:
        print("""|xxx| Operação falhou. O valor informado é inválido.\n|----------Voltando ao menu principal...""")
    
    return saldo, extrato

def sacar(*, saldo, saque, extrato, numero_saques):
    limite_por_saque = 500
    limite_saques = 3
    if saque > limite_por_saque:
            print("""|xxx| Operação falhou. O valor máximo por saque é de R$ 500,00.\n|----------Voltando ao menu principal...""")
        
    elif saque > saldo:
        print("""|xxx| Operação falhou. O saldo não é suficiente.\n|----------Voltando ao menu principal...""")
        
    elif numero_saques >= limite_saques:
        print("""|xxx| Operação falhou. O limite de 3 saques por dia já foi atingido.\n|----------Voltando ao menu principal...""")
            
    elif saque > 0:
        saldo -= saque
        extrato += f"Saque:\tR$ {saque:.2f}\n"
        numero_saques += 1
        print("\n|===| Saque realizado com suscesso.\n|----------Voltando ao menu principal...")

    else:
        print(f"""|xxx| Operação falhou. O valor {saque:.2f} é inválido.\n|----------Voltando ao menu principal...""")
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n|---------- EXTRATO ----------|")
    if not extrato:
        print("\n| Não foram realizadas movimentações. |\n\n|---------------------------|")
    else:
        print(f"\n{extrato}")
        print(f"\n| Saldo:\t\tR$ {saldo:.2f} |")
        print("\n|---------------------------|")


def criar_usuario(usuarios):
    cpf = input("CPF (Somente números): ")
    
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
         print("|xxx| CPF já cadastrado.\n|----------Voltando ao menu principal...")
         return
         

    nome = input("Nome Completo: ")
    data_nascimento = input("Data de Nascimento (dd/mm/AAAA): ")
    logradouro = input("Logradouro: ")
    nro_end = input("Número: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Estado (Sigla): ")
    endereço = f"{logradouro}, {nro_end} - {bairro} - {cidade}/{estado}."
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereço})

    print("\n|===| Usuário cadastrado com suscesso.\n|----------Voltando ao menu principal...")

def filtrar_usuario(cpf, usuarios):
     usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
     return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(numero_conta, usuarios):
    agencia = "0001"
    cpf = input("CPF (Somente Números): ")
     
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        numero_conta += 1
        print("\n|===| Conta criada com suscesso.\n|----------Voltando ao menu principal...")
        return {"agencia":agencia, "numero_conta": numero_conta, "usuario": usuario}
    else:
        print("|xxx| Usuário não encontrado.\n|----------Voltando ao menu principal...")

    
def listar_contas(contas):
     for conta in contas:
          linha = f"""\
            Agência:\t{conta["agencia"]}
            Conta Corrente:\t{conta["numero_conta"]}
            Usuário:\t{conta["usuario"]["nome"]}
            """
          print("=" *100)
          print(textwrap.dedent(linha))


def main():

    numero_conta = 0
    saldo = 0
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        operacao = menu()

        if operacao == "1":
            deposito = float(input("Informe o valor do depósito: R$ "))
            saldo, extrato = depositar(saldo, deposito, extrato)

        elif operacao == "2":
            saque = float(input("Informe o valor a ser sacado: R$ "))
            saldo, extrato = sacar(saldo=saldo, saque=saque, extrato=extrato, numero_saques=numero_saques)
       
        elif operacao == "3":
            exibir_extrato(saldo,extrato=extrato)

        elif operacao == "4":
             criar_usuario(usuarios)

        elif operacao == "5":
             conta = criar_conta(numero_conta, usuarios)
             if conta:
                 contas.append(conta)
            
        elif operacao == "6":
             listar_contas(contas)

        elif operacao == "0":
            break

        else:
            print("""|xxx| Operação inválida. Por favor, selecione novamente.\n|----------Voltando ao menu principal...""")

main()
