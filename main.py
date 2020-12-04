'''
Esse arquivo é responsável por chamar as funções de acordo com o input dos usuários.
'''

# Importando bibliotecas necessárias para funcionamento do aplicativo
from tela import Tela           #Importando arquivo para exibição
from sistema import Sistema     #Importando arquivo que roda sistema
import os

# Instanciando classes
sistema = Sistema()
tela = Tela()

# Exibe tela inicial
sistema.carregar_conteudo()
tela.exibirBemVindo()
input("[Enter]")
os.system('cls')
acesso = False

# Exibe tela de login
while acesso == False:
    login = tela.exibirLogin()
    if login:
        acesso = Sistema().autenticacao()
        input("\n[Enter]")
    else:
        acesso = Sistema().cadastro()
        input("\n[Enter]")

# Exibe menu inicial
user = 0
while user != '8':
    os.system('cls')
    user = Tela().exibirMenu()
    if user == '1':
        # Exibi formulário de doação
        os.system('cls')
        lista = tela.exibirFormulario('doacao')
        sistema.realizar_acao(lista, sistema.doacoes)
        os.system('cls')
    elif user == '2':
        # Exibe lista de itens doados
        os.system('cls')
        tela.exibirAnuncio()
        sistema.listar_anuncios(sistema.doacoes)
        sistema.receber_anuncio('doacao',sistema.doacoes)
        os.system('cls')
    elif user == '3':
        # Exibe formulário de venda
        os.system('cls')
        lista = tela.exibirFormulario('venda')
        sistema.realizar_acao(lista, sistema.bazar)
        os.system('cls')
    elif user == '4':
        # Exibe lista de produtos a venda
        os.system('cls')
        tela.exibirAnuncio()
        sistema.listar_anuncios(sistema.bazar)
        sistema.receber_anuncio('venda', sistema.bazar)
        os.system('cls')
    elif user == '5':
        # Exibe formulário de descarte
        os.system('cls')
        lista = tela.exibirFormulario('ferrovelho')
        sistema.realizar_acao(lista, sistema.ferrovelho)
        os.system('cls')
    elif user == '6':
        # Exibe lista de itens para descarte
        os.system('cls')
        tela.exibirAnuncio()
        sistema.listar_anuncios(sistema.ferrovelho)
        sistema.receber_anuncio('ferrovelho', sistema.ferrovelho)
        os.system('cls')
    elif user == '7':
        # Exibe informações adicionais sobre aplicativo
        os.system('cls')
        tela.exibirSobre()
        input("[Enter]")
        os.system('cls')
    elif user == '8':
        # Fecha execução da aplicação
        os.system('cls')
        print("Volte sempre!")
        input()
    else:
        tela.erroMensagem()