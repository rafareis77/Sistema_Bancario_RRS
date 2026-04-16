# 🏦 Sistema Bancário Digital — Python com POO

Aplicação Full-Stack de sistema bancário desenvolvida em Python com Programação Orientada a Objetos (POO).  
O projeto conta com duas interfaces: uma via **terminal (CLI)** e outra via **interface web com Streamlit**.

---

## 📁 Estrutura do Projeto

```
Sistema_Bancario_Python_POO/
├── entidades/
│   ├── __init__.py
│   ├── cliente.py
│   └── conta.py
├── operacoes/
│   ├── __init__.py
│   └── banco.py
├── utilitarios/
│   ├── __init__.py
│   └── exceptions.py
├── app.py
├── projeto_banco.py
└── requirements.txt
```

### Descrição dos arquivos

- `entidades/` — Classes que representam as entidades do sistema (`Cliente`, `Conta`, `ContaCorrente`, `ContaPoupanca`)
- `operacoes/` — Lógica de negócio e operações principais (classe `Banco`)
- `utilitarios/` — Utilitários e exceções customizadas (`SaldoInsuficienteError`, `ContaInexistenteError`)
- `app.py` — Interface web construída com **Streamlit** (versão visual do sistema)
- `projeto_banco.py` — Interface via terminal **CLI** (ponto de entrada da aplicação em linha de comando)

---

## ⚙️ Funcionalidades

- Cadastro de clientes (nome e CPF)
- Criação de contas **corrente** e **poupança**
- Operações de **depósito**, **saque** e **transferência**
- Visualização de **extrato** com histórico de movimentações
- Tratamento de erros com exceções customizadas
- Interface web responsiva com Streamlit

---

## 🚀 Como executar

### Pré-requisitos

Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

### Versão terminal (CLI)

```bash
python projeto_banco.py
```

### Versão web (Streamlit)

```bash
streamlit run app.py
```

---

## 🛠️ Tecnologias utilizadas

- Python 3
- Streamlit
- Programação Orientada a Objetos (POO)
