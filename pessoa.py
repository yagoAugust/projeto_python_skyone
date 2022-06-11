class Pessoa:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def exibir(self):
        print(f'nome:{self.nome.title()} \ntelefone:{self.telefone}')