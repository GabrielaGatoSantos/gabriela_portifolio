import os
'''O import os importa a biblioteca python para o código, trazendo o os.system ('cls')'''
#Dicionários
''''Dicionários em python para uma estrutura de dados, armazenar os dados tipo em uma lista'''
restaurantes = [{'nome':'CafeteriaSG', 'categoria':'Cafés&Bolos', 'ativo':False}, 
                {'nome':'ResteuranteItalian', 'categoria':'Italiana', 'ativo':True},
                {'nome':'NiguirisSaG', 'categoria':'Japonesa', 'ativo':False}]

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")
def exibir_opcoes():
    ''''Essa função lista as opções da aplicação e a de cima o nome do programa'''
    print ('1. Cadastrar restaurante')
    print ('2. Listar restaurante')
    print ('3. Alternar estado do restaurante')
    print ('4. Sair\n')

def finalizar_app ():
    '''Essa função finaliza o app chamando a opção 4'''
    exibir_subtitulo('Finalizando o app')

def voltar_ao_menu_principal():
        '''Essa função volta ao menu principal após selecionar uma opção no terminal'''
        input ('\nDigite uma tecla para voltar para o menu principal')
        main()

def opcao_invalida ():
    '''Caso nenhuma das opções no else não for selecionada, irá trazer essa função'''
    print('Opção inválida! \n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Essa função limpa o terminal após executar um comando'''
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:

    - Adiciona um novo restaurante a lista de restaurante
    
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input (f'Digite o nome da categoria{nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante,'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print (f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    
    voltar_ao_menu_principal()
    

def listar_restaurantes():
    '''Essa função irá listar o status do restaurante'''
    exibir_subtitulo('Listando os restaurantes')

    print(f'{'Nome do restaurante'.ljust(37)} | {'Categoria'.ljust(30)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado'if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(35)} | {categoria.ljust(30)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():

    ''' Essa função irá verificar o status do restaurante se for false irá virar true e se for true irá virar false, através do restaurante['ativo'] = not restaurante['ativo'] ele irá alterar os status'''
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
   
    for restaurante in restaurantes:
      
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']  
            mensagem = f'O restaurante {nome_restaurante} Foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} Foi desativado com sucesso!'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()


def escolher_opcao ():
    '''Essa função irá trazer as escolhas de opção e tratar possíveis erros ao passar o parâmetro através do try (Quando uma exceção entra no bloco do try, o controle é transferido para o bloco except, permitindo que de para tratar a excessão de maneira adequada.) '''
    try:
        opcao_escolhida = int (input('Escolha uma opção: '))  

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
           alternar_estado_restaurante()
        elif opcao_escolhida == 4: 
            finalizar_app()  
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''O python usa a estrutura main para definir uma parte principal de um código, por exemplo essa função irá retornar ao menu principal'''
    os.system('cls')    
    exibir_nome_do_programa()  
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
   main()









