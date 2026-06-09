# Gerenciador de Tabela de Símbolos

Projeto da disciplina de **Construção de Compiladores** — Opção 2.

Implementa uma **Tabela de Símbolos** que gerencia **escopos aninhados**
(*nested scopes*) usando uma **Pilha (Stack)** de **Hash Maps**. Cada escopo
é um Hash Map (dicionário) que mapeia o nome de uma variável ao seu tipo, e a
Pilha controla qual é o escopo atual.

Métodos exigidos pelo enunciado:

- `declarar(variavel, tipo)` — registra uma variável no escopo atual.
- `buscar(variavel)` — procura uma variável do escopo mais interno para o mais
  externo (regra de resolução de nomes de um compilador).

## Requisitos

- **Python 3.8 ou superior** (não usa nenhuma biblioteca externa).

```bash
python3 --version
```

## Como executar

A partir da pasta raiz do projeto, rode **exatamente**:

```bash
python3 main.py
```

> No Windows, caso o comando acima não funcione, use:
>
> ```bash
> python main.py
> ```

O programa executa uma demonstração automática com 6 casos de teste e imprime,
passo a passo, cada operação (entrada/saída de escopo, declaração e busca).

## Estrutura do projeto (organização modular)

```
gerenciador-tabela-simbolos/
├── erros.py                # Erro semântico            (Pessoa 1)
├── escopo.py               # Classe Escopo = 1 Hash Map (Pessoa 1)
├── tabela_de_simbolos.py   # Pilha de escopos + métodos (Pessoa 2)
├── main.py                 # Demonstração / casos de teste (Pessoa 3)
├── README.md               # Este arquivo                (Pessoa 3)
└── Relatorio_Tecnico.pdf   # Relatório técnico           (Pessoa 3)
```

| Módulo | Responsabilidade | Estrutura de dados |
|--------|------------------|--------------------|
| `escopo.py` | Um escopo individual | **Hash Map** (dicionário) |
| `tabela_de_simbolos.py` | Empilhar/desempilhar escopos e resolver nomes | **Pilha (Stack)** de escopos |
| `main.py` | Exercitar o sistema com casos de teste | — |

## Como usar como biblioteca

```python
from tabela_de_simbolos import TabelaDeSimbolos

tabela = TabelaDeSimbolos()      # já abre o escopo global
tabela.declarar("contador", "int")

tabela.entrar_escopo("loop")     # abre um escopo aninhado
tabela.declarar("i", "int")
print(tabela.buscar("contador")) # -> "int" (vem do escopo externo)
tabela.sair_escopo()             # fecha o escopo "loop"

print(tabela.buscar("i"))        # -> None (já saiu do escopo)
```

## Autores

- Pesso 1 — _(Welbert de Oliveira Costa / 1231525468)_
- Aluno 2 — _(Igor Rafael Basilio de Lima / 1231527762)_
- Aluno 3 — _(Danilo Vitor Firmino Lima / 1231522159)_
