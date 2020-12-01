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
while user != '4':
    os.system('cls')
    user = Tela().exibirMenu()
    if user == '1':
        os.system('cls')
        sistema.realizar_doacao()
        input("[Enter]")
        os.system('cls')
    elif user == '2':
        os.system('cls')
        tela.exibirDoacoes()
        sistema.listar_doacoes()
        sistema.receber_doacao()
        input("[Enter]")
        os.system('cls')
    elif user == '3':
        os.system('cls')
        tela.exibirSobre()
        input("[Enter]")
        os.system('cls')
    elif user == '4':
        os.system('cls')
        print("Volte sempre!")
        input()
    else:
        Tela().erroMensagem()