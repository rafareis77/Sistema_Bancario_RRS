# Módulo para execução customizada da aplicação

# Define a execução para saldo insuficiente em saques
class SaldoInsuficienteError(Exception):

    """
    Exceção aparece quando uma operação de saque ultrapassa o saldo dsponível
    """

    def __init__(self, saldo_atual, valor_saque, mensagem="Saldo insuficiente para realizar o saque."):
        self.saldo_atual = saldo_atual
        self.valor_saque = valor_saque
        self.mensagem = f"{mensagem} Saldo atual: R${saldo_atual:.2f},\n" \
                        f"Tentativa de saque: R${valor_saque:.2f}"

        super().__init__(self.mensagem)


# Define a exceção ara operações em contas inexistentes
class ContaInexistenteError(Exception):

    """
    Exceção aparece ao tentar uma operação em uma conta que não existe
    """

    def __init__(self, numero_conta, mensagem="Conta não encontrada."):
        self.numero_conta = numero_conta
        self.mensagem = f"{mensagem} Número da conta: {numero_conta}"

        super().__init__(self.mensagem)