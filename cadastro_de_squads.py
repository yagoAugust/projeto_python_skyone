"""
Neste bloco, crio uma classe chamada "Pessoa" e dou os atributos "nome" e "telefone"
"""
from pessoa import Pessoa
from colaborador import Colaborador
from dev import Dev
from squad import Squad

print('\n-=-=-=-=-=-=-=-=-=-=-Sky.One Solutions=-=-=-=-=-=-=-=-=-')
print('Bem vindo ao sistema de cadastro de squads!\n')

while True:

    squads = []
    nome_squad = input('\nNome da squad: ')
    while nome_squad.isnumeric():
        nome_squad = input('Por gentileza, informe apenas letras.\nNome da squad: ')

    nome_techlead = input('Nome do techlead da squad: ')
    while nome_techlead.isnumeric():
        nome_techlead = input('Por gentileza, informe apenas letras.\n techlead: ')

    telefone_techlead = input('Telefone do techlead: ')
    while telefone_techlead.isalpha():
        telefone_techlead = input('Por gentileza, informe apenas números\nTelefone do techlead: ')

    squad = Squad(nome_squad)
    techlead = Colaborador(nome_techlead, telefone_techlead)
    squad.incluir_techlead(techlead)
    techlead.incluir_squad(squad)

    squads.append(squad)

    while True:

        nome_dev = input('\nNome do desenvolvedor: ')
        while nome_dev.isnumeric():
            nome_dev = input('Por gentileza, informe apenas letras.\nNome do desenvolvedor: ')

        telefone_dev = input('Telefone do desenvolvedor: ')
        while telefone_dev.isalpha():
            telefone_dev = input('Por gentileza, informe apenas números\nTelefone do desenvolvedor: ')

        cargo_dev = input('Cargo do desenvolvedor: ')

        dev = Dev(nome_dev, telefone_dev, cargo_dev)
        dev.incluir_squad(squad)
        squad.incluir_dev(dev)

        option = input('Deseja adicionar mais um dev [S/N]')
        if option.lower() == 'n':
            break

    option = input('\nDeseja adicionar mais uma squad [S/N]')
    if option.lower() == 'n':
        break

"""Laço para informar todo o elemento "squad" dentro da lista "squads" """
for squad in squads:
    print(f'\n-=-=-=-=-=-=-=-=-Cadastro Sky.One-=-=-=-=-=-=-=-=-')
    print('Squads criadas:')
    print(f'\n------------------------------{squad.nome.title()}------------------------------')
    print(f'TechLead: {squad.techlead.nome.title()} \ntelefone: {squad.techlead.telefone}')

    print('\n-----Devs do squad-----')

    """Laço para informar todo o elemento "dev" dentro da lista "devs" """

    for dev in squad.devs:
        dev.exibir()
    print(f'--------------------------------{squad.nome.title()}------------------------------')

print('\n-==-=-=-=-=-=-=-=-=-=-=Sky.One Solutions=-=-=-=-=-=-=-=-=-=-')
