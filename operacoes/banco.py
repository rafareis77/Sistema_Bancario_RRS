from entidades.cliente import Cliente
from entidades.conta import Conta, ContaCorrente, ContaPoupanca
from utilitarios.exceptions import ContaInexistenteError


class Banco:
    """
    Classe que gerencia as operações bacárias
    """

    def __init__(self, nome: str):
        self.nome = nome
        self._clientes = {}
        self._contas = {}

    # Método para adicionar um novo cliente
    def adicionar_cliente(self, nome: str, cpf: str) -> Cliente:

        """
        Cria e adiciona um novo cliente ao banco
        """

        # Verifica se o cpf já foi cadastrado
        if cpf in self._clientes:
            raise ValueError(f"O CPF {cpf} já foi cadastrado.")

        # Cria objeto Cliente e adiciona ao dicionario
        novo_cliente = Cliente(nome, cpf)
        self._clientes[cpf] = novo_cliente

        print(f"Cliente {nome} adcionado com sucesso!")

        return novo_cliente

    # Método para criar uma conta
    def criar_conta(self, cliente: Cliente, tipo: str) -> Conta:
        """
        Cria uma nova conta para um cliente já existente.
        """

        # Número da conta será baseado no total de contas + 1
        numero_conta = Conta.get_total_contas() + 1

        # Cria conta corrente se o tipo for informado "corrente"
        if tipo.lower() == "corrente":
            nova_conta = ContaCorrente(numero_conta, cliente)
            nova_conta.tipo = "Corrente"

        elif tipo.lower() == "poupanca":
            nova_conta = ContaPoupanca(numero_conta, cliente)
            nova_conta.tipo = "Poupança"

        else:
            print("Tipo de Conta inválido. Escolha entre 'corrente' ou 'poupanca'.")
            return None

        # Adiciona a conta ao dicionario de contas
        self._contas[numero_conta] = nova_conta

        # Associa a conta ao cliente
        cliente.adicionar_conta(nova_conta)
        print(f"Conta {tipo} nº {numero_conta} criada para o cliente {cliente.nome}.")

        return nova_conta

    # Método para buscar uma conta pelo número
    def buscar_conta(self, numero_conta: int) -> Conta:

        """Busca uma conta pelo seu número
        """

        # Tenta recuperar a conta do dicionário
        conta = self._contas.get(numero_conta)

        # senao encontrar, lança esse erro
        if not conta:
            raise ContaInexistenteError(numero_conta)

        return conta

    # Método para realizar transernecias
    def transferencia(self, num_origem: int, num_destino: int, valor: float):
        if num_origem == num_destino:
            raise ValueError("Não é possível transferir para a mesma conta.")

        conta_origem = self.buscar_conta(num_origem)
        conta_destino = self.buscar_conta(num_destino)

        conta_origem.sacar(valor)
        conta_destino.depositar(valor)

        return True
