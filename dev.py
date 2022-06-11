from colaborador import Colaborador

class Dev(Colaborador):
    def __init__(self, nome, telefone, cargo, squad=None):
        super().__init__(nome, telefone, squad)
        self.cargo = cargo

    def exibir(self):
        super().exibir()
        print(f'Cargo:{self.cargo}\nsquad:{self.squad.nome.title()}\n')
