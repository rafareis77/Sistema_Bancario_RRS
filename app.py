<<<<<<< HEAD
import streamlit as st
import sys
import os

from entidades.cliente import Cliente
from entidades.conta import Conta, ContaCorrente, ContaPoupanca
from operacoes.banco import Banco
from utilitarios.exceptions import ContaInexistenteError, SaldoInsuficienteError

# Adciona o diretorio pai ao path para importar os modulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Configuração da página
st.set_page_config(page_title="RRS Bank", page_icon="🏦", layout="wide")

# Iniciando a sessão no streamlit
if 'banco' not in st.session_state:
    st.session_state.banco = Banco("Banco Digital RRS")
    st.session_state.conta_atual = None


def main():
    st.markdown("""
        <style>
        /* Camada da Imagem de fundo */
        [data-testid="stAppViewContainer"] {
            content: "";
            background-image:url("https://fia.com.br/wp-content/uploads/2024/01/2024_01_08_Financas-Capa.png");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            
        /* Filtro transparente */ 
        [data-testid="stAppViewContainer"]::before {
            position: absolute;
            top: 0;
            left: 0;
            width: 95%;
            height: 95%;
            background-color: rgba(255, 255, 255, 0.99);
            z-index: 0;
        }
        
        /* Garantindo que o conteúdo fique por cima do filtro */
        [data-tesid="stVerticalBlock"], [data-testid="stHeader"] {
            z-index: 1;
        }
        
        /* Removendo os fundos brancos */
        [data-testid="stMainViewContainer"], .main, .stApp {
            background-color: transparent !important;
        }
        
        /* Estilização do sidebar*/
        [data-testid="stSidebar"] {
            background-color: rgba(255, 255, 255, 0.4);
            background-filter: blur(40px);
            border-right: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        /* Estilização dos Cards */
        div[data-testid="stVerticalBlock"] > div.stBock {
            background-color: rgba(255, 255, 255, 0.95) !important;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.1);
            color: #1e1e1e !important;
            border: 1px solid #ddd;
        }
        
        /* Botões com hover brilhante */
        .stButton>button {
            background: linear-gradient(45deg, #00c6ff, #0072ff);
            border: none;
            color: white;
            font-weight: bold;
            border-radius: 12px;
            transition: all 0.3s ease;
        }
        .stButton>button: hover{
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0, 198, 255, 0.4);
        }
        
        /* Muda a cor dos textos (p, span, labels) */
        html, body, [class*="st-"] {
            color: #f0f2f6 !important;
        }
        
        /* Muda a cor dos títulos e subtitulos */
        h1, h2, h3, h4, h5, h6 {
            color: #ffffff !important;
        }
        
        /* Muda a cor dos labels (campos de input)
        .stWidgetLabel {
            color: #ffffff !important;
            font-weight: bold !important;
        }
        
        /* 4. Muda a cor das legendas e textos pequenos */
        .stMarkdown p, .stCaption {
            color: #e0e0e0 !important;
    }
    
    /* Garante que labels dentro de blocos brancos fiquem escuros se necessário */
        div[data-testid="stVerticalBlock"] > div.stBlock .stWidgetLabel {
            color: #1e1e1e !important;
    }
        </style>
    """, unsafe_allow_html=True)

    # Menu lateral
    with st.sidebar:
        #st.image("https://cdn-icons-png.flaticon.com/512/2830/2830284.png", width=100)
        st.title("RRS Bank")
        st.caption("Soluções Digitais Inteligentes")
        st.divider()

        # Senão houver conta ativa, mostra o menu geral
        if st.session_state.conta_atual is None:
            opcao = st.radio(
                "Navegação",
                ["Página Inicial", "Adicionar Cliente", "Criar Conta", "Acessar Conta", "Sair"]
            )
        else:
            # Se houver conta ativa, mostra as opções da conta
            opcao = "Operações da Conta"
            if st.button("⬅️ Sair da Conta / Voltar"):
                st.session_state.conta_atual = None
                st.rerun()

    if opcao == "Página Inicial":
        # Criando um cabeçalho centralizado
        col_logo, col_titulo = st.columns([1, 4])
        with col_logo:
            st.image("https://cdn-icons-png.flaticon.com/512/2830/2830284.png", width=80)
        with col_titulo:
            st.title("Seja Bem-vindo ao RRS Bank")
            st.info("Selecione uma opção no menu lateral para começar.")

        st.write("---")
        st.markdown("### O futuro das suas finanças começa aqui.")

    elif opcao == "Adicionar Cliente":
        st.header("👤 Cadastrar novo Cliente")

        with st.form("form_cliente", clear_on_submit=True):
            nome = st.text_input("Nome do Cliente")
            cpf = st.text_input("CPF do Cliente")
            submit = st.form_submit_button("Cadastrar Cliente")

            if submit:
                if nome and cpf:
                    try:
                        st.session_state.banco.adicionar_cliente(nome, cpf)
                        st.success(f"Cliente {nome} adicionado com sucesso!")

                        # Mostrar clientes cadastrados
                        if st.session_state.banco._clientes:
                            st.subheader("Clientes cadastrados")
                            for cpf_clientes, cliente_obj in st.session_state.banco._clientes.items():
                                st.write(f"- {cliente_obj.nome} (CPF: {cpf_clientes})")

                    except Exception as e:
                        st.error(f"Erro: {e}")

            else:
                st.warning("Preencha todos os campos.")

    elif opcao == "Criar Conta":
        st.header("💳 Abertura de Conta")

        with st.form("form_conta"):
            cpf_busca = st.text_input("Digite o CPF para criar a conta")
            tipo_conta = st.selectbox("Tipo", ["corrente", "poupanca"])
            submit_conta = st.form_submit_button("Criar Conta")

            if submit_conta:
                cliente = st.session_state.banco._clientes.get(cpf_busca)

                if cliente:
                    try:
                        conta_nova = st.session_state.banco.criar_conta(cliente, tipo_conta)
                        st.success(f"Conta {tipo_conta} Nº {conta_nova._numero} criada!")
                    except Exception as e:
                        st.error(f"Erro: {e}")
                else:
                    st.error("Cliente não encontrado.")

    elif opcao == "Acessar Conta":
        st.header("🔑 Acessar Conta")
        with st.form("form_login"):
            num_c = st.text_input("Número da conta")
            btn_login = st.form_submit_button("Entrar")

            if btn_login:
                try:
                    conta_encontrada = st.session_state.banco.buscar_conta(int(num_c))
                    st.session_state.conta_atual = conta_encontrada
                    st.rerun()

                except ContaInexistenteError as e:
                    st.error(f"Conta não encontrada: {e}")

    elif opcao == "Operações da Conta":
        conta = st.session_state.conta_atual

        # Informações
        st.subheader(f"📱 Conta {conta.tipo}: {conta._numero}")
        col_info1, col_info2 = st.columns(2)
        col_info1.write(f"Titular {conta._cliente.nome}")
        col_info2.metric("Saldo Atual", f"R${conta.saldo:.2f}")

        tab1, tab2, tab3, tab4 = st.tabs(["💵 Depósito/Saque", "📊 Extrato", "💸 Transferência", "Sair da Conta"])

        with tab1:
            with st.form("operacoes_caixa"):
                op = st.radio("Ação", ["Depositar", "Sacar"], horizontal=True)
                v = st.number_input("Valor: ", min_value=0.01, step=50.0)

                if st.form_submit_button("Confirmar"):
                    try:
                        if op == "Depositar":
                            conta.depositar(v)
                        else:
                            conta.sacar(v)
                        st.success("Operação realizada com sucesso!")
                        st.rerun()

                    except SaldoInsuficienteError as e:
                        st.error(f"Erro: {e}")

        with tab2:
            with st.form("### Historico Recente"):
                historico = getattr(conta, "historico", []) or getattr(conta, "_historico", [])
                if not historico:
                    st.info("Sem movimentações")
                else:
                    if st.form_submit_button("Confirmar"):
                        for data, msg in reversed(historico):  # mostra o mais recente primeiro
                            c_data, c_msg = st.columns([1, 4])
                            c_data.caption(data.strftime("%d/%m/%Y %H:%M"))
                            emoji = "🟢" if "Depósito" in msg else "🔴"
                            c_msg.write(f"{emoji} {msg}")
                            st.divider()

        with tab3:
            st.write("### 💸 Transferência")
            with st.form("form_transferencia", clear_on_submit=True):
                c_dest = st.number_input("Número da Conta Destino", min_value=1, step=1)
                v_transf = st.number_input("Valor da transferência", min_value=0.01, step=10.0)

                if st.form_submit_button("Confirmar Transferência"):
                    try:
                        st.session_state.banco.transferencia(conta._numero, int(c_dest), v_transf)
                        st.success(f"Trasnferência de R${v_transf:.2f} realizada com sucesso!")
                        st.rerun()

                    except SaldoInsuficienteError as e:
                        st.error(f"Erro: {e}")

        with tab4:
            if st.button("Sair da Conta"):
                st.session_state.conta_atual = None
                st.success("Conta desconectada!")
                st.rerun()

    elif opcao == "Sair":
        st.info("Obrigado por usar nosso sistema! Até logo!")
        st.stop()


if __name__ == "__main__":
    main()
=======
import streamlit as st
import sys
import os

from entidades.cliente import Cliente
from entidades.conta import Conta, ContaCorrente, ContaPoupanca
from operacoes.banco import Banco
from utilitarios.exceptions import ContaInexistenteError, SaldoInsuficienteError

# Adciona o diretorio pai ao path para importar os modulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Configuração da página
st.set_page_config(page_title="RRS Bank", page_icon="🏦", layout="wide")

# Iniciando a sessão no streamlit
if 'banco' not in st.session_state:
    st.session_state.banco = Banco("Banco Digital RRS")
    st.session_state.conta_atual = None


def main():
    st.markdown("""
        <style>
        /* Camada da Imagem de fundo */
        [data-testid="stAppViewContainer"] {
            content: "";
            background-image:url("https://fia.com.br/wp-content/uploads/2024/01/2024_01_08_Financas-Capa.png");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            
        /* Filtro transparente */ 
        [data-testid="stAppViewContainer"]::before {
            position: absolute;
            top: 0;
            left: 0;
            width: 95%;
            height: 95%;
            background-color: rgba(255, 255, 255, 0.99);
            z-index: 0;
        }
        
        /* Garantindo que o conteúdo fique por cima do filtro */
        [data-tesid="stVerticalBlock"], [data-testid="stHeader"] {
            z-index: 1;
        }
        
        /* Removendo os fundos brancos */
        [data-testid="stMainViewContainer"], .main, .stApp {
            background-color: transparent !important;
        }
        
        /* Estilização do sidebar*/
        [data-testid="stSidebar"] {
            background-color: rgba(255, 255, 255, 0.4);
            background-filter: blur(40px);
            border-right: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        /* Estilização dos Cards */
        div[data-testid="stVerticalBlock"] > div.stBock {
            background-color: rgba(255, 255, 255, 0.95) !important;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.1);
            color: #1e1e1e !important;
            border: 1px solid #ddd;
        }
        
        /* Botões com hover brilhante */
        .stButton>button {
            background: linear-gradient(45deg, #00c6ff, #0072ff);
            border: none;
            color: white;
            font-weight: bold;
            border-radius: 12px;
            transition: all 0.3s ease;
        }
        .stButton>button: hover{
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0, 198, 255, 0.4);
        }
        
        /* Muda a cor dos textos (p, span, labels) */
        html, body, [class*="st-"] {
            color: #f0f2f6 !important;
        }
        
        /* Muda a cor dos títulos e subtitulos */
        h1, h2, h3, h4, h5, h6 {
            color: #ffffff !important;
        }
        
        /* Muda a cor dos labels (campos de input)
        .stWidgetLabel {
            color: #ffffff !important;
            font-weight: bold !important;
        }
        
        /* 4. Muda a cor das legendas e textos pequenos */
        .stMarkdown p, .stCaption {
            color: #e0e0e0 !important;
    }
    
    /* Garante que labels dentro de blocos brancos fiquem escuros se necessário */
        div[data-testid="stVerticalBlock"] > div.stBlock .stWidgetLabel {
            color: #1e1e1e !important;
    }
        </style>
    """, unsafe_allow_html=True)

    # Menu lateral
    with st.sidebar:
        #st.image("https://cdn-icons-png.flaticon.com/512/2830/2830284.png", width=100)
        st.title("RRS Bank")
        st.caption("Soluções Digitais Inteligentes")
        st.divider()

        # Senão houver conta ativa, mostra o menu geral
        if st.session_state.conta_atual is None:
            opcao = st.radio(
                "Navegação",
                ["Página Inicial", "Adicionar Cliente", "Criar Conta", "Acessar Conta", "Sair"]
            )
        else:
            # Se houver conta ativa, mostra as opções da conta
            opcao = "Operações da Conta"
            if st.button("⬅️ Sair da Conta / Voltar"):
                st.session_state.conta_atual = None
                st.rerun()

    if opcao == "Página Inicial":
        # Criando um cabeçalho centralizado
        col_logo, col_titulo = st.columns([1, 4])
        with col_logo:
            st.image("https://cdn-icons-png.flaticon.com/512/2830/2830284.png", width=80)
        with col_titulo:
            st.title("Seja Bem-vindo ao RRS Bank")
            st.info("Selecione uma opção no menu lateral para começar.")

        st.write("---")
        st.markdown("### O futuro das suas finanças começa aqui.")

    elif opcao == "Adicionar Cliente":
        st.header("👤 Cadastrar novo Cliente")

        with st.form("form_cliente", clear_on_submit=True):
            nome = st.text_input("Nome do Cliente")
            cpf = st.text_input("CPF do Cliente")
            submit = st.form_submit_button("Cadastrar Cliente")

            if submit:
                if nome and cpf:
                    try:
                        st.session_state.banco.adicionar_cliente(nome, cpf)
                        st.success(f"Cliente {nome} adicionado com sucesso!")

                        # Mostrar clientes cadastrados
                        if st.session_state.banco._clientes:
                            st.subheader("Clientes cadastrados")
                            for cpf_clientes, cliente_obj in st.session_state.banco._clientes.items():
                                st.write(f"- {cliente_obj.nome} (CPF: {cpf_clientes})")

                    except Exception as e:
                        st.error(f"Erro: {e}")

            else:
                st.warning("Preencha todos os campos.")

    elif opcao == "Criar Conta":
        st.header("💳 Abertura de Conta")

        with st.form("form_conta"):
            cpf_busca = st.text_input("Digite o CPF para criar a conta")
            tipo_conta = st.selectbox("Tipo", ["corrente", "poupanca"])
            submit_conta = st.form_submit_button("Criar Conta")

            if submit_conta:
                cliente = st.session_state.banco._clientes.get(cpf_busca)

                if cliente:
                    try:
                        conta_nova = st.session_state.banco.criar_conta(cliente, tipo_conta)
                        st.success(f"Conta {tipo_conta} Nº {conta_nova._numero} criada!")
                    except Exception as e:
                        st.error(f"Erro: {e}")
                else:
                    st.error("Cliente não encontrado.")

    elif opcao == "Acessar Conta":
        st.header("🔑 Acessar Conta")
        with st.form("form_login"):
            num_c = st.text_input("Número da conta")
            btn_login = st.form_submit_button("Entrar")

            if btn_login:
                try:
                    conta_encontrada = st.session_state.banco.buscar_conta(int(num_c))
                    st.session_state.conta_atual = conta_encontrada
                    st.rerun()

                except ContaInexistenteError as e:
                    st.error(f"Conta não encontrada: {e}")

    elif opcao == "Operações da Conta":
        conta = st.session_state.conta_atual

        # Informações
        st.subheader(f"📱 Conta {conta.tipo}: {conta._numero}")
        col_info1, col_info2 = st.columns(2)
        col_info1.write(f"Titular {conta._cliente.nome}")
        col_info2.metric("Saldo Atual", f"R${conta.saldo:.2f}")

        tab1, tab2, tab3, tab4 = st.tabs(["💵 Depósito/Saque", "📊 Extrato", "💸 Transferência", "Sair da Conta"])

        with tab1:
            with st.form("operacoes_caixa"):
                op = st.radio("Ação", ["Depositar", "Sacar"], horizontal=True)
                v = st.number_input("Valor: ", min_value=0.01, step=50.0)

                if st.form_submit_button("Confirmar"):
                    try:
                        if op == "Depositar":
                            conta.depositar(v)
                        else:
                            conta.sacar(v)
                        st.success("Operação realizada com sucesso!")
                        st.rerun()

                    except SaldoInsuficienteError as e:
                        st.error(f"Erro: {e}")

        with tab2:
            with st.form("### Historico Recente"):
                historico = getattr(conta, "historico", []) or getattr(conta, "_historico", [])
                if not historico:
                    st.info("Sem movimentações")
                else:
                    if st.form_submit_button("Confirmar"):
                        for data, msg in reversed(historico):  # mostra o mais recente primeiro
                            c_data, c_msg = st.columns([1, 4])
                            c_data.caption(data.strftime("%d/%m/%Y %H:%M"))
                            emoji = "🟢" if "Depósito" in msg else "🔴"
                            c_msg.write(f"{emoji} {msg}")
                            st.divider()

        with tab3:
            st.write("### 💸 Transferência")
            with st.form("form_transferencia", clear_on_submit=True):
                c_dest = st.number_input("Número da Conta Destino", min_value=1, step=1)
                v_transf = st.number_input("Valor da transferência", min_value=0.01, step=10.0)

                if st.form_submit_button("Confirmar Transferência"):
                    try:
                        st.session_state.banco.transferencia(conta._numero, int(c_dest), v_transf)
                        st.success(f"Trasnferência de R${v_transf:.2f} realizada com sucesso!")
                        st.rerun()

                    except SaldoInsuficienteError as e:
                        st.error(f"Erro: {e}")

        with tab4:
            if st.button("Sair da Conta"):
                st.session_state.conta_atual = None
                st.success("Conta desconectada!")
                st.rerun()

    elif opcao == "Sair":
        st.info("Obrigado por usar nosso sistema! Até logo!")
        st.stop()


if __name__ == "__main__":
    main()
>>>>>>> 6ce586c146c80863dbd26afe47d2e882204a8e49
