# Gerenciador de Tabela de Símbolos

Análise Semântica e Escopos Aninhados | Projeto Prático

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)

Projeto desenvolvido para a disciplina de **Construção de Compiladores (Opção 2)**. 

O sistema implementa uma **Tabela de Símbolos** eficiente para gerenciar **escopos aninhados** (*nested scopes*) utilizando uma estrutura de **Pilha (Stack)** preenchida por **Hash Maps** (dicionários do Python). Cada escopo ativo funciona como um mapa local isolado, permitindo a resolução de nomes de variáveis da maneira exata que um compilador real faz.

---

##  Métodos Implementados

De acordo com as especificações do enunciado, o núcleo do sistema expõe:
* `declarar(variavel, tipo)`: Registra uma nova variável com seu tipo correspondente no escopo atual (topo da pilha).
* `buscar(variavel)`: Procura por uma variável realizando uma busca linear de cima para baixo na pilha (do escopo mais interno/recente até o escopo global).

---

##  Estrutura do Projeto

O desenvolvimento foi feito de forma modular e distribuído entre a equipe:

```text
gerenciador-tabela-simbolos/
├── erros.py                # Exceções personalizadas para erros semânticos
├── escopo.py               # Classe Escopo (Encapsula 1 Hash Map)
├── tabela_de_simbolos.py   # Gerenciamento da Pilha de escopos e métodos de busca
├── main.py                 # Rotina de disposição e cenários de teste
└── README.md               # Documentação principal do projeto
```

### Divisão de Responsabilidades

| Módulo | Responsabilidade | Estrutura de Dados | Integrante |
| :--- | :--- | :--- | :--- |
| `erros.py` / `escopo.py` | Definição de exceções e escopo individual | **Hash Map** (Dicionário) | Welbert Costa |
| `tabela_de_simbolos.py` | Empilhamento/desempilhamento e resolução | **Pilha (Stack)** de escopos | Igor Rafael |
| `main.py` / Docs | Criação dos cenários de teste e relatórios | — | Danilo Lima |

---

##  Como Executar

### Pré-requisitos
Certifique-se de possuir o **Python 3.8 ou superior** instalado na sua máquina. O projeto foi construído utilizando exclusivamente a biblioteca padrão do ecossistema Python (zero dependências externas).

```bash
python3 --version
```

### Inicializando a Demonstração
A partir do diretório raiz do projeto, execute o arquivo principal:

```bash
python3 main.py
```

*Caso esteja utilizando ambiente Windows e ocorra algum problema com o comando acima, tente:*

```bash
python main.py
```

---

##  Casos de Teste Cobertos

Ao rodar o arquivo `main.py`, a aplicação simula uma rotina real de compilação passando por 6 cenários críticos:
* **Declarações Globais**: Inserção e busca de variáveis no escopo raiz do programa.
* **Escopos Aninhados**: Criação de um novo escopo (simulando uma função) com busca retroativa de variáveis globais.
* **Shadowing**: Verificação do sombreamento de variáveis, onde uma variável local temporariamente oculta uma global de mesmo nome.
* **Saída de Escopo**: Destruição do escopo local após a saída de um bloco e validação de que as variáveis internas tornaram-se inacessíveis.
* **Erro Semântico (Redeclaração)**: Tratamento de erro disparado ao tentar declarar duas variáveis idênticas no mesmo nível de escopo.
* **Variável Inexistente**: Resposta padrão do sistema ao tentar buscar um identificador que nunca foi definido.

---

##  Exemplo Prático de Uso

Caso queira utilizar o gerenciador como um módulo em outros arquivos do seu projeto:

```python
from tabela_de_simbolos import TabelaDeSimbolos

# Inicializa a tabela (o escopo global é aberto automaticamente)
tabela = TabelaDeSimbolos()
tabela.declarar("contador", "int")

# Entra em um bloco/escopo aninhado
tabela.entrar_escopo("loop_for")
tabela.declarar("i", "int")

# Acessa variável do escopo pai (Global) normalmente
print(tabela.buscar("contador"))  # Saída: "int"

# Finaliza o bloco atual e desempilha o escopo
tabela.sair_escopo()

# Tentar acessar a variável local do bloco agora retornará None
print(tabela.buscar("i"))  # Saída: None
```

---

## 👥 Autores

* **Welbert de Oliveira Costa** — Desenvolvimento das estruturas base (`escopo.py` e `erros.py`).
* **Igor Rafael Basilio de Lima** — Desenvolvimento do motor da tabela (`tabela_de_simbolos.py`).
* **Danilo Vitor Firmino Lima** — Casos de teste, validação e documentação (`main.py` e relatórios).
