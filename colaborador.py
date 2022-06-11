from pessoa import Pessoa

class Colaborador(Pessoa):
    def __init__(self, nome, telefone, squad=None):
        super().__init__(nome, telefone)
        self.squad = squad

    def incluir_squad(self, squad):
        self.squad = squad
