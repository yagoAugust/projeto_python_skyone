# projeto_python_skyone
Projeto de Python oferecido pela Sky.One Solutions.

------------------Cadastro de Squads-------------



Esse é um simples projeto onde você pode cadastrar
Squads (Seu time dev), assim como o seu líder e o telefone 
do mesmo.
Também é possível cadastrar os desenvolvedores
de cada Squad. O interessante é o fato do usuário
ter total liberdade para adicionar quantos Squads
 e/ou desenvolvedores quiserem.

Modificações:
    Tomei liberdade para fazer algumas modificações
no código original, mantendo a sua função e o deixando
com uma formatação melhor e mais prática

Modificação 1:

    Original:option = input('Deseja adicionar mais um dev [S/N]')
        if option in 'Nn':
            break
----
    Modificado:option = input('Deseja adicionar mais um dev [S/N]')
        if option.lower() == 'n':
            break
Fiz essa modificação pois acredito ser mais prático
formatar o valor "option" para minúsculo e depois
fazer a comparação

Modificação 2:
           
                
    Original:print(f'TechLead: {squad.techlead.nome} - {squad.techlead.fone}')
    
    def exibir(self):
        print(f'-> {self.nome} - {self.fone}')
--------
    Modificado:print(f'TechLead: {squad.techlead.nome.title()} \ntelefone: {squad.techlead.telefone}') 

    def exibir(self):
       print(f'nome:{self.nome.title()} \ntelefone:{self.telefone}')

Na segunda modificação, adicionei a função "title"
para deixar uma formatação mais "correta", assim,
independente de como o nome for escrito, ele aparecerá
com a primeira letra maiscúla e o resto minúscula