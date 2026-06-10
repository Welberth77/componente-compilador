from tabela_de_simbolos import TabelaDeSimbolos
from erros import ErroSemantico


def demonstracao():
    print("=" * 60)
    print(" SIMULAÇÃO DE GERENCIADOR DE TABELA DE SÍMBOLOS")
    print("=" * 60)

    tabela = TabelaDeSimbolos()

    print("\n--- CASO 1: Declarações no escopo global ---")
    tabela.declarar("x", "int")
    tabela.declarar("nome", "string")
    tabela.buscar("x")
    tabela.buscar("nome")

    print("\n--- CASO 2: Escopo aninhado (função) e acesso ao externo ---")
    tabela.entrar_escopo(nome="funcao_soma")
    tabela.declarar("a", "float")
    tabela.declarar("b", "float")
    tabela.buscar("a")        # local
    tabela.buscar("x")        # vem do escopo global (acessível)

    print("\n--- CASO 3: Shadowing (sombreamento de variável) ---")
    tabela.declarar("x", "double")  # mesmo nome de 'x' global, escopo interno
    tabela.buscar("x")              # deve achar o 'double' interno, não o int

    print("\n--- CASO 4: Saída de escopo e perda das variáveis locais ---")
    tabela.sair_escopo()
    tabela.buscar("a")        # 'a' era local de funcao_soma -> some
    tabela.buscar("x")        # volta a ser o 'int' global

    print("\n--- CASO 5: Erro de redeclaração no mesmo escopo ---")
    try:
        tabela.declarar("x", "char")  # já existe 'x' no global
    except ErroSemantico as e:
        print(f"[ERRO   ] {e}")

    print("\n--- CASO 6: Variável inexistente ---")
    resultado = tabela.buscar("inexistente")
    print(f"Resultado da busca por 'inexistente': {resultado}")

    print("\n" + "=" * 60)
    print(" FIM DA SIMULAÇÃO")
    print("=" * 60)


if __name__ == "__main__":
    demonstracao()
