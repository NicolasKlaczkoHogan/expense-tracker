# Expense Tracker

## Descrição do Problema Real

Muitas pessoas têm dificuldade em controlar seus gastos pessoais, levando a endividamento e falta de planejamento financeiro. Este aplicativo ajuda a resolver essa dor ao permitir o registro simples de despesas, visualização de histórico e cálculo de totais, promovendo uma melhor gestão financeira.

## Proposta da Solução

Uma aplicação CLI simples que permite adicionar despesas, listar todas, ver um resumo total e deletar entradas. Armazena dados em um arquivo JSON local, sem necessidade de banco de dados.

## Público-Alvo

Pessoas que desejam controlar gastos pessoais, estudantes, freelancers e famílias que precisam de uma ferramenta básica e gratuita para gestão financeira.

## Funcionalidades Principais

- Adicionar despesa com valor e descrição
- Listar todas as despesas com data
- Ver resumo total dos gastos
- Deletar despesa por ID

## Tecnologias Utilizadas

- Linguagem: Python 3.8+
- Interface: CLI (Command Line Interface)
- Armazenamento: Arquivo JSON
- Testes: pytest
- Linting: flake8
- CI: GitHub Actions

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/expense-tracker.git
   cd expense-tracker
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Execução

Execute o aplicativo com Python:

```bash
python src/expense_tracker.py <comando>
```

### Comandos Disponíveis

- Adicionar despesa: `python src/expense_tracker.py add <valor> <descrição>`
- Listar despesas: `python src/expense_tracker.py list`
- Resumo total: `python src/expense_tracker.py summary`
- Deletar despesa: `python src/expense_tracker.py delete <id>`

Exemplo:
```bash
python src/expense_tracker.py add 15.50 "Café da manhã"
python src/expense_tracker.py list
```

## Rodar os Testes

```bash
pytest
```

## Rodar o Lint

```bash
flake8 src/ tests/
```

## Versão Atual

1.0.0

## Autor

Nicolas

## Link do Repositório Público

[https://github.com/seu-usuario/expense-tracker](https://github.com/seu-usuario/expense-tracker)

## CI Status

![CI](https://github.com/seu-usuario/expense-tracker/workflows/CI/badge.svg)