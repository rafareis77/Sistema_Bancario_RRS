<<<<<<< HEAD
from operacoes.banco import Banco
from utilitarios.exceptions import SaldoInsuficienteError, ContaInexistenteError


# Exibindo o menu principal
def menu_principal():
    print("\n--- Sistema Bancário Digital ---\n")
    print("1. Adicionar cliente")
    print("2. Criar conta")
    print("3. Acessar conta")
    print("4. Sair\n")

    return input("Escolha uma opção: ")


# Exibe o menu de operações de uma conta específica
def menu_conta(banco):
    try:
        num_conta = int(input("Digite o número da conta: "))
        conta = banco.buscar_conta(num_conta)

        # Loop das operações dentro da conta
        while True:
            print(f"\n--- Operações para Conta Nº {conta._numero} ---")
            print(f"Cliente: {conta._cliente.nome} | Saldo: R${conta.saldo:.2f}")
            print("1. Depositar")
            print("2. Sacar")
            print("3. Ver Extrato")
            print("4. Voltar ao Menu Principal")

            # Lê a opção do usuario
            opcao = input("Escolha uma opção: ")

            if opcao == '1':

                # Deposita valor na conta
                valor = float(input("Digite o valor para depósito: "))
                conta.depositar(valor)

            elif opcao == '2':

                # Tenta realizar um saque
                try:
                    valor = float(input("Digite o valor para saque: "))
                    conta.sacar(valor)

                except SaldoInsuficienteError as e:
                    print(f"Erro na operação: {e}")

            elif opcao == '3':

                # Exibe o extrato
                conta.extrato()

            elif opcao == '4':

                # Sai do menu da conta e retona para o menu principal
                break

            else:
                print("Opção inválida. Tente novamente.")

    # Exceção caso a conta não exista
    except ContaInexistenteError as e:
        print(f"Erro: {e}")

    # Exceção para entradas inválidas
    except ValueError:
        print("Erro: Entrada inválida. Digite apenas números por favor.")


# Função principal que controla o fluxo do sistema
def main():
    banco = Banco("Banco Digital RRS")

    # Loop principal do sistema
    while True:

        opcao = menu_principal()

        if opcao == '1':

            # Adiciona um novo cliente
            nome = input("Digite o nome do cliente: ")
            cpf = input("Digite o CPF do cliente: ")
            banco.adicionar_cliente(nome, cpf)

        elif opcao == '2':

            # Cria uma nova conta vinculada a um cliente existente
            cpf = input("Digite o CPF para cadastrar a conta: ")
            cliente = banco._clientes.get(cpf)

            if cliente:
                tipo = input("Digite o tipo da conta (corrente / poupanca)")
                banco.criar_conta(cliente, tipo)

            else:
                print("Cliente não encontrado. É preciso cadastrar primeiro.")

        elif opcao == '3':

            # Abre o menu de operações de uma conta
            menu_conta(banco)

        elif opcao == '4':

            # Encerra o programa
            print("\nObrigado por usar nosso sistema. Até logo!\n")
            break


if __name__ == "__main__":
    main()
=======
from operacoes.banco import Banco
from utilitarios.exceptions import SaldoInsuficienteError, ContaInexistenteError


# Exibindo o menu principal
def menu_principal():
    print("\n--- Sistema Bancário Digital ---\n")
    print("1. Adicionar cliente")
    print("2. Criar conta")
    print("3. Acessar conta")
    print("4. Sair\n")

    return input("Escolha uma opção: ")


# Exibe o menu de operações de uma conta específica
def menu_conta(banco):
    try:
        num_conta = int(input("Digite o número da conta: "))
        conta = banco.buscar_conta(num_conta)

        # Loop das operações dentro da conta
        while True:
            print(f"\n--- Operações para Conta Nº {conta._numero} ---")
            print(f"Cliente: {conta._cliente.nome} | Saldo: R${conta.saldo:.2f}")
            print("1. Depositar")
            print("2. Sacar")
            print("3. Ver Extrato")
            print("4. Voltar ao Menu Principal")

            # Lê a opção do usuario
            opcao = input("Escolha uma opção: ")

            if opcao == '1':

                # Deposita valor na conta
                valor = float(input("Digite o valor para depósito: "))
                conta.depositar(valor)

            elif opcao == '2':

                # Tenta realizar um saque
                try:
                    valor = float(input("Digite o valor para saque: "))
                    conta.sacar(valor)

                except SaldoInsuficienteError as e:
                    print(f"Erro na operação: {e}")

            elif opcao == '3':

                # Exibe o extrato
                conta.extrato()

            elif opcao == '4':

                # Sai do menu da conta e retona para o menu principal
                break

            else:
                print("Opção inválida. Tente novamente.")

    # Exceção caso a conta não exista
    except ContaInexistenteError as e:
        print(f"Erro: {e}")

    # Exceção para entradas inválidas
    except ValueError:
        print("Erro: Entrada inválida. Digite apenas números por favor.")


# Função principal que controla o fluxo do sistema
def main():
    banco = Banco("Banco Digital RRS")

    # Loop principal do sistema
    while True:

        opcao = menu_principal()

        if opcao == '1':

            # Adiciona um novo cliente
            nome = input("Digite o nome do cliente: ")
            cpf = input("Digite o CPF do cliente: ")
            banco.adicionar_cliente(nome, cpf)

        elif opcao == '2':

            # Cria uma nova conta vinculada a um cliente existente
            cpf = input("Digite o CPF para cadastrar a conta: ")
            cliente = banco._clientes.get(cpf)

            if cliente:
                tipo = input("Digite o tipo da conta (corrente / poupanca)")
                banco.criar_conta(cliente, tipo)

            else:
                print("Cliente não encontrado. É preciso cadastrar primeiro.")

        elif opcao == '3':

            # Abre o menu de operações de uma conta
            menu_conta(banco)

        elif opcao == '4':

            # Encerra o programa
            print("\nObrigado por usar nosso sistema. Até logo!\n")
            break


if __name__ == "__main__":
    main()
>>>>>>> 6ce586c146c80863dbd26afe47d2e882204a8e49
