
#  Classe Escopo: representa UM escopo como um HASH MAP (Hash Table).

# Importando erro
from erros import ErroSemantico


class Escopo:
    def __init__(self, nome="usuario"):
        self.nome = nome
        # HASH MAP (Hash Table): nome da variável -> tipo
        self.tabela = {}

    def contem(self, variavel):
        # Retorna True se a variável existe NESTE escopo.
        return variavel in self.tabela

    def declarar_local(self, variavel, tipo):
        # Insere a variável no Hash Map deste escopo (sem subir níveis).
        if self.contem(variavel):
            raise ErroSemantico(
                f"Variável '{variavel}' já declarada no escopo atual "
                f"'{self.nome}'.")
        self.tabela[variavel] = tipo
        return True

    def buscar_local(self, variavel):
        # Retorna o tipo da variável NESTE escopo, ou None se não houver.
        return self.tabela.get(variavel)