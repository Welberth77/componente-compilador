
#  Classe Escopo: representa UM escopo como um HASH MAP (Hash Table).

# Importando erro
from erros import ErroSemantico


class Escopo:
    def __init__(self, nome="usuario"):
        self.nome = nome
        # HASH MAP (Hash Table): nome da variável -> tipo
        self.tabela = {}