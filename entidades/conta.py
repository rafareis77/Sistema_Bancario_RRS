<<<<<<< HEAD
from abc import ABC, abstractmethod
from datetime import datetime
from utilitarios.exceptions import SaldoInsuficienteError


# Define a classe abstrata conta, que serve como base para os outros tipos de conta
class Conta(ABC):
    """
    Classe abstrata para contas bancárias
    """

    # Atributo de classe que calcula quantas contas foram criadas
    _total_contas = 0

    def __init__(self, numero: int, cliente):
        self._numero = numero
        self._saldo = 0.0
        self._cliente = cliente
        self._historico = []

        # Incrementa o total de contas criadas
        Conta._total_contas += 1

    # Propriedade para acessar o saldo de forma controlada
    @property
    def saldo(self):
        """
        Getter para o saldo, permitindo acesso controlado
        :return: valor do saldo
        """

        return self._saldo

    # Método da classe para consultar o numero total de contas
    @classmethod
    def get_total_contas(cls):
        """
        Metodo de classe para obter o número total de contas criadas
        :return: Número total das contas criadas
        """

        return cls._total_contas

    # Método para realizar depositos
    def depositar(self, valor: float):

        # Adciona um valor ao saldo da conta e incrementa ao saldo
        if valor > 0:
            self._saldo += valor

            # Registra a transação ao histórico com data e hora
            self._historico.append((datetime.now(), f"Depósito de R${valor:.2f}"))
            print(f"Depósito realizado com sucesso.")

        else:
            print("Valor de deposito inválido")

    # Método abstrato que deve ser implementado pelas subclasses
    @abstractmethod
    def sacar(self, valor: float):

        """
        Método para sacar um valor que será implementado pelas subclasses
        """
        pass

    # Método para exibir o extrato bancário
    def extrato(self):
        """
        Exibe o extrato da conta
        """
        print(f"\n--- Extrato da Conta Nº {self._numero} ---")
        print(f"Cliente: {self._cliente.nome}")
        print(f"Saldo atual: R${self._saldo:.2f}")
        print("Histórico de transações:")

        # Caso não haja transações na conta
        if not self._historico:
            print("Nenhuma transação registrada.")

        # Percorre o histórico e exibe cada transação
        for data, transacao in self._historico:
            print(f"- {data.strftime('%d/%m/%Y %H:%M:%S')}: {transacao}")
        print("-----------------------------------------\n")


# Define a subclasse ContaCorrente
class ContaCorrente(Conta):
    """
    Subclasse que representa a conta corrente
    """

    def __init__(self, numero: int, cliente, limite: float = 500.0):
        super().__init__(numero, cliente)

        # Define o limite de cheque especial
        self.limite = limite

    def sacar(self, valor: float):
        """
        Permite o saque utilizando o valor da conta mais o limite de cheque especial
        """

        if valor <= 0:
            print("Valor de saque inválido")
            return

        # Calcula o saldo disponivel (saldo + limite)
        saldo_disponivel = self._saldo + self.limite

        # Caso o saque ultrapasse o saldo disponível
        if valor > saldo_disponivel:
            raise SaldoInsuficienteError(saldo_disponivel, valor, "Saldo e limite insuficientes.")

        # Deduz o valor do saque do saldo
        self._saldo -= valor

        # Registra a transação no histórico
        self._historico.append((datetime.now(), f"Saque de R${valor:.2f}"))


# Define a subclasse ContaPoupanca
class ContaPoupanca(Conta):
    """
    Representa a poupança
    """

    def __init__(self, numero: int, cliente):
        super().__init__(numero, cliente)

    # Implementação do saque apenas com saldo disponivel
    def sacar(self, valor: float):

        # Permite saque apenas se houver saldo suficiente na conta
        if valor <= 0:
            print("Valor de saque inválido.")
            return

        # Verifica se há saldo suficiente
        if valor > self._saldo:
            raise SaldoInsuficienteError(self._saldo, valor)

        self._saldo -= valor

        self._historico.append((datetime.now(), f"Saque de R${valor:.2f}"))
        print("Saldo realizado com sucesso")
=======
from abc import ABC, abstractmethod
from datetime import datetime
from utilitarios.exceptions import SaldoInsuficienteError


# Define a classe abstrata conta, que serve como base para os outros tipos de conta
class Conta(ABC):
    """
    Classe abstrata para contas bancárias
    """

    # Atributo de classe que calcula quantas contas foram criadas
    _total_contas = 0

    def __init__(self, numero: int, cliente):
        self._numero = numero
        self._saldo = 0.0
        self._cliente = cliente
        self._historico = []

        # Incrementa o total de contas criadas
        Conta._total_contas += 1

    # Propriedade para acessar o saldo de forma controlada
    @property
    def saldo(self):
        """
        Getter para o saldo, permitindo acesso controlado
        :return: valor do saldo
        """

        return self._saldo

    # Método da classe para consultar o numero total de contas
    @classmethod
    def get_total_contas(cls):
        """
        Metodo de classe para obter o número total de contas criadas
        :return: Número total das contas criadas
        """

        return cls._total_contas

    # Método para realizar depositos
    def depositar(self, valor: float):

        # Adciona um valor ao saldo da conta e incrementa ao saldo
        if valor > 0:
            self._saldo += valor

            # Registra a transação ao histórico com data e hora
            self._historico.append((datetime.now(), f"Depósito de R${valor:.2f}"))
            print(f"Depósito realizado com sucesso.")

        else:
            print("Valor de deposito inválido")

    # Método abstrato que deve ser implementado pelas subclasses
    @abstractmethod
    def sacar(self, valor: float):

        """
        Método para sacar um valor que será implementado pelas subclasses
        """
        pass

    # Método para exibir o extrato bancário
    def extrato(self):
        """
        Exibe o extrato da conta
        """
        print(f"\n--- Extrato da Conta Nº {self._numero} ---")
        print(f"Cliente: {self._cliente.nome}")
        print(f"Saldo atual: R${self._saldo:.2f}")
        print("Histórico de transações:")

        # Caso não haja transações na conta
        if not self._historico:
            print("Nenhuma transação registrada.")

        # Percorre o histórico e exibe cada transação
        for data, transacao in self._historico:
            print(f"- {data.strftime('%d/%m/%Y %H:%M:%S')}: {transacao}")
        print("-----------------------------------------\n")


# Define a subclasse ContaCorrente
class ContaCorrente(Conta):
    """
    Subclasse que representa a conta corrente
    """

    def __init__(self, numero: int, cliente, limite: float = 500.0):
        super().__init__(numero, cliente)

        # Define o limite de cheque especial
        self.limite = limite

    def sacar(self, valor: float):
        """
        Permite o saque utilizando o valor da conta mais o limite de cheque especial
        """

        if valor <= 0:
            print("Valor de saque inválido")
            return

        # Calcula o saldo disponivel (saldo + limite)
        saldo_disponivel = self._saldo + self.limite

        # Caso o saque ultrapasse o saldo disponível
        if valor > saldo_disponivel:
            raise SaldoInsuficienteError(saldo_disponivel, valor, "Saldo e limite insuficientes.")

        # Deduz o valor do saque do saldo
        self._saldo -= valor

        # Registra a transação no histórico
        self._historico.append((datetime.now(), f"Saque de R${valor:.2f}"))


# Define a subclasse ContaPoupanca
class ContaPoupanca(Conta):
    """
    Representa a poupança
    """

    def __init__(self, numero: int, cliente):
        super().__init__(numero, cliente)

    # Implementação do saque apenas com saldo disponivel
    def sacar(self, valor: float):

        # Permite saque apenas se houver saldo suficiente na conta
        if valor <= 0:
            print("Valor de saque inválido.")
            return

        # Verifica se há saldo suficiente
        if valor > self._saldo:
            raise SaldoInsuficienteError(self._saldo, valor)

        self._saldo -= valor

        self._historico.append((datetime.now(), f"Saque de R${valor:.2f}"))
        print("Saldo realizado com sucesso")
>>>>>>> 6ce586c146c80863dbd26afe47d2e882204a8e49
