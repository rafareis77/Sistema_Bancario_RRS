<<<<<<< HEAD
# Módulo da Entidade Cliente

# Define a classe Cliente
class Cliente:
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf
        self.contas = []

    # Método para adcionar uma conta a lista de contas do cliente
    def adcionar_conta(self, conta):
        self.contas.append(conta)

    # Método especial que define o objeto em string
    def __str__(self):
        return f"Cliente: {self.nome} (CPF: {self.cpf})"

    def adicionar_conta(self, nova_conta):
=======
# Módulo da Entidade Cliente

# Define a classe Cliente
class Cliente:
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf
        self.contas = []

    # Método para adcionar uma conta a lista de contas do cliente
    def adcionar_conta(self, conta):
        self.contas.append(conta)

    # Método especial que define o objeto em string
    def __str__(self):
        return f"Cliente: {self.nome} (CPF: {self.cpf})"

    def adicionar_conta(self, nova_conta):
>>>>>>> 6ce586c146c80863dbd26afe47d2e882204a8e49
        pass