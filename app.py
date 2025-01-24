import os

restaurantes = [{'nome':'Sabor da Itália', 'categoria':'Italiana', 'ativo': False},
                {'nome':'Temaki', 'categoria':'Japonesa', 'ativo': True},
                {'nome':'Estrela do Nordeste', 'categoria':'Brasileira', 'ativo': False}]

def exibir_nome_do_programa():
    print('''
        █▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
        ▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
    '''
    )

    
def exibir_opcoes():
    '''
    Essa função exibe o menu da Aplicação
    
    '''

    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def voltar_ao_menu_principal():
    input('Digite uma tecla para voltar ao menu principal')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)

def finalizar_app():
    os.system('cls')
    print('Finalizando app\n')

def opcao_invalida():
    print('Opção inválida\n')
    voltar_ao_menu_principal()
 
def cadastrar_novo_restaurante():

    '''Essa função é responsável por cadastrar um novo restaurante
    - Nome do restaurante
    - Categoria

    Output:
    - Adiciona um novo restaurante à lista de restaurantes

    '''
    exibir_subtitulo('Cadastre um novo restaurante')
    novo_restaurante = input('Digite o nome do restaurante: ')
    categoria = input(f'Digite o nome da categoria do restaurante {novo_restaurante}: ')
    dados_do_restaurante = {'nome':novo_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {novo_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
   
   '''Essa função é responsável por listar um restaurante cadastrado
    - Nome do restaurante
    - Categoria
    - Status

    Output:
    - Lista um restaurante cadastrado

    '''

   exibir_subtitulo('Listando os restaurantes')
   print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')
   for restaurante in restaurantes:
        nome = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome.ljust(20)} | {categoria.ljust(20)} | {ativo}')
   voltar_ao_menu_principal()

def alterar_estado_do_restaurante():
    '''Essa função é responsável por alterar o Status de um restaurante
    - Status

    Output:
    - Altera o Status de um restaurantes

    '''
    exibir_subtitulo('Alterando o estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi modificado com sucesso.'
            print(mensagem)
        if not restaurante_encontrado:
            print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
           listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_estado_do_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
