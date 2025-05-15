from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime
import textwrap


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("""|xxx| Operação falhou. O saldo não é suficiente.\n""")
        
        elif valor > 0:
            self._saldo -= valor
            print("\n|===| Saque realizado com suscesso.\n")
            return True
        
        else:
            print(f"""|xxx| Operação falhou. O valor {valor:.2f} é inválido.\n""")

        return False
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n|===| Depósito realizado com suscesso.\n")
        
        else:
            print("""|xxx| Operação falhou. O valor informado é inválido.\n""")
            return False
        
        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico._transacoes if transacao["tipo"] == Saque.__name__]
            )
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("""|xxx| Operação falhou. O valor máximo por saque é de R$ 500,00.\n""")

        elif excedeu_saques:
            print("""|xxx| Operação falhou. O limite de 3 saques por dia já foi atingido.\n""")

        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""\
            Agência:\t{self._agencia}
            Conta Corrente:\t{self._numero}
            Titular:\t{self._cliente.nome}
            """


class Historico():
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__, 
                "valor": transacao.valor, 
                "data": datetime.now().strftime("%d/%m/%Y %H:%M:%s"),
            }
        )

    
class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

def menu():
    menu = """
    -------------- MENU --------------
    Digite qual operação deseja:

    [1]\tDepósito
    [2]\tSaque
    [3]\tExtrato
    [4]\tNovo Cliente
    [5]\tNova Conta
    [6]\tListar Contas

    [0] Sair

    ----------------------------------
    => """
    
    return input(textwrap.dedent(menu))


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n|xxx| Cliente não possui conta! |xxx|\n")
        return

    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]


def validar_cliente_conta(cpf, clientes):
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\n|xxx| Cliente não encontrado! |xxx|\n")
        return None, None
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return cliente, None 
    
    return cliente, conta


def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente, conta = validar_cliente_conta(cpf, clientes)
    
    if not conta:
        return  

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)
    cliente.realizar_transacao(conta, transacao)


def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente, conta = validar_cliente_conta(cpf, clientes)
    
    if not conta:
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)
    cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente, conta = validar_cliente_conta(cpf, clientes)
    
    if not conta:
        return

    print("\n|================ EXTRATO ================|")
    transacoes = conta.historico.transacoes
    
    if not transacoes:
        print("Não foram realizadas movimentações.")
    else:
        print("\n|Operação|" + " " * 26 + "|Valor|")
        print("-" * 43)
        
        for transacao in transacoes:
            tipo = transacao['tipo']
            valor = f"R$ {transacao['valor']:>10.2f}"
            linha = f"|{tipo.ljust(10)}{'.' * 18}{valor}|"
            print(linha)
    
    # Saldo
    saldo_str = f"R$ {conta.saldo:>10.2f}"
    print(f"\n|Saldo{'.' * 23}{saldo_str}|")
    print("|===================-=====================|")


def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n|xxx| Já existe cliente com esse CPF! |xxx|\n")
        return

    nome = input("Nome Completo: ")
    data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ")
    logradouro = input("Logradouro: ")
    nro_end = input("Número: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Estado (Sigla): ")
    endereco = f"{logradouro}, {nro_end} - {bairro} - {cidade}/{estado}."
    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print("\n|===| Cliente criado com sucesso! |===|\n")


def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n|xxx| Cliente não encontrado, fluxo de criação de conta encerrado! |xxx|\n")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n|===| Conta criada com sucesso! |===|\n")


def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))


def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            depositar(clientes)

        elif opcao == "2":
            sacar(clientes)

        elif opcao == "3":
            exibir_extrato(clientes)

        elif opcao == "4":
            criar_cliente(clientes)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            break

        else:
            print("\n|xxx| Operação inválida, por favor selecione novamente a operação desejada. |xxx|\n")


main()
