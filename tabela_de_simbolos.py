from escopo import Escopo
from erros import ErroSemantico


class TabelaDeSimbolos:

    def __init__(self):
        # A PILHA (Stack) de escopos. append() = push, pop() = pop.
        self.pilha_de_escopos = []
        # Toda tabela começa com um escopo global aberto.
        self.entrar_escopo(nome="global")

    # Operações de PILHA (gerência de escopos)
    def entrar_escopo(self, nome="anonimo"):
        """PUSH: empilha um novo Escopo (Hash Map) no topo da pilha."""
        self.pilha_de_escopos.append(Escopo(nome))
        print(f"[ESCOPO] Entrou no escopo '{nome}' "
              f"(profundidade = {self.profundidade()})")

    def sair_escopo(self):
        """POP: desempilha o escopo do topo, descartando suas variáveis."""
        if self.profundidade() <= 1:
            raise ErroSemantico("Não é possível sair do escopo global.")
        escopo = self.pilha_de_escopos.pop()
        print(f"[ESCOPO] Saiu do escopo '{escopo.nome}' "
              f"(profundidade = {self.profundidade()})")
        return escopo

    def profundidade(self):
        """Número de escopos atualmente empilhados."""
        return len(self.pilha_de_escopos)

    # Métodos obrigatórios do enunciado
    def declarar(self, variavel, tipo):
        """Declara a variável no escopo do TOPO da pilha (escopo atual)."""
        escopo_atual = self.pilha_de_escopos[-1]
        escopo_atual.declarar_local(variavel, tipo)
        print(f"[DECLARAR] '{variavel} : {tipo}' adicionada ao escopo "
              f"'{escopo_atual.nome}'.")
        return True

    def buscar(self, variavel):
        """Busca a variável percorrendo a PILHA do TOPO para a BASE."""
        for escopo in reversed(self.pilha_de_escopos):
            if escopo.contem(variavel):
                tipo = escopo.buscar_local(variavel)
                print(f"[BUSCAR ] '{variavel}' ENCONTRADA no escopo "
                      f"'{escopo.nome}' -> tipo = {tipo}")
                return tipo
        print(f"[BUSCAR ] '{variavel}' NÃO ENCONTRADA (erro: não declarada)")
        return None
