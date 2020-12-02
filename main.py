from tela import Tela
from sistema import Sistema
import os

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

user = 0
while user != '8':
    os.system('cls')
    user = Tela().exibirMenu()
    if user == '1':
        os.system('cls')
        lista = tela.exibirFormulario('doacao')
        sistema.realizar_acao(lista, sistema.doacoes)
        os.system('cls')
    elif user == '2':
        os.system('cls')
        tela.exibirAnuncio()
        sistema.listar_anuncios(sistema.doacoes)
        sistema.receber_anuncio('doacao',sistema.doacoes)
        os.system('cls')
    elif user == '3':
        os.system('cls')
        lista = tela.exibirFormulario('venda')
        sistema.realizar_acao(lista, sistema.bazar)
        os.system('cls')
    elif user == '4':
        os.system('cls')
        tela.exibirAnuncio()
        sistema.listar_anuncios(sistema.bazar)
        sistema.receber_anuncio('venda', sistema.bazar)
        os.system('cls')
    elif user == '5':
        os.system('cls')
        lista = tela.exibirFormulario('ferrovelho')
        sistema.realizar_acao(lista, sistema.ferrovelho)
        os.system('cls')
    elif user == '6':
        os.system('cls')
        tela.exibirAnuncio()
        sistema.listar_anuncios(sistema.ferrovelho)
        sistema.receber_anuncio('ferrovelho', sistema.ferrovelho)
        os.system('cls')
    elif user == '7':
        os.system('cls')
        tela.exibirSobre()
        input("[Enter]")
        os.system('cls')
    elif user == '8':
        os.system('cls')
        print("Volte sempre!")
        input()
    else:
        tela.erroMensagem()