import random
from usuario import Usuario
from doacao import Doacao
import os

class Sistema:
    usuarios = []
    doacoes = []


    def autenticacao(self):
        login_usuario = input("Digite o login   : ")
        senha_usuario = input("Digite sua senha : ")
        logado = self.checa_usuario(login_usuario,senha_usuario)
        if logado:
            print("\nUsuário logado com sucesso!")
            return True
        else:
            print("\nUsuário informado não existe!")
            return False


    def cadastro(self):
        login = input("Digite um login  : ")
        senha = input("Crie uma senha   : ")
        confirmacaoSenha = input("Confirme a senha  : ")
        existe_usuario = self.checa_usuario(login,senha)
        if senha == confirmacaoSenha and not existe_usuario:
            self.cadastrar_usuario(login,senha)
            print("Usuario cadastrado com sucesso!")
            return True
        elif existe_usuario:
            print("Usuario já existe.\nTente logar novamente ou crie um novo usuário.")
            return False
        else:
            print("Senhas não coincidem! Tente novamente, por favor.\n")
            return False


    def carregar_conteudo(self):
        db_usuarios = open('usuarios.txt', "r", encoding="utf-8")
        todos_usuarios = [usuario.replace("\n", "") for usuario in db_usuarios]

        for usuario in todos_usuarios:
            info_usuario = usuario.split(";")
            login = info_usuario[0]
            senha = info_usuario[1]
            user = Usuario(login,senha)
            self.usuarios.append(user)

        db_doacoes = open('doacoes.txt', "r", encoding="utf-8")
        todas_doacoes = [doacao.replace("\n", "") for doacao in db_doacoes]

        for doacao in todas_doacoes:
            info_usuario = doacao.split(";")
            id = info_usuario[0]
            titulo = info_usuario[1]
            descricao = info_usuario[2]
            categoria = info_usuario[3]
            data = info_usuario[4]
            donate = Doacao(id,titulo,descricao,categoria,data)
            self.doacoes.append(donate)


    def cadastrar_usuario(self, login, senha):
        user = Usuario(login, senha)
        self.usuarios.append(user)
        db_usuarios = open('usuarios.txt', "a", encoding="utf-8")
        db_usuarios.write(f"\n{user.login};{user.senha}")
        db_usuarios.close()


    def listar_doacoes(self):
        for doacao in self.doacoes:
            print(doacao)
            escolha = input("Gostaria de exibir próxima doação?\n[1]Sim\n[2]Não\n->")
            if escolha == '2':
                return
        input("[Enter]")

    def cadastrar_doacao(self, id, titulo, descricao, categoria, data):
        doacao = Doacao(id, titulo, descricao, categoria, data)
        self.doacoes.append(doacao)
        db_usuarios = open('doacoes.txt', "a", encoding="utf-8")
        db_usuarios.write(f"\n{doacao.id};{doacao.titulo};{doacao.descricao};{doacao.categoria};{doacao.data}")
        db_usuarios.close()


    def receber_doacao(self):
        escolha = 0
        while escolha != '1' and escolha != '2':
            escolha = input("Você gostaria de receber alguma dessas doações?\n[1]Sim\n[2]Não\n\n-> ")
            if escolha == '1':
                doado = True
                while doado:
                    id = input("Informe o ID da doação: ")
                    for doacao in self.doacoes:
                        if doacao.id == id:
                            doado = False
                            self.doacoes.remove(doacao)
                            input("\nEsta doação foi separada para você!")
                            return
                    input("Informe um número de ID válido.\n[Enter]")
        if os.path.exists("doacoes.txt"):
            os.remove("doacoes.txt")
            db_doacoes = open("doacoes.txt", "x")
            for doacao in self.doacoes:
                db_doacoes = open('doacoes.txt', "a", encoding="utf-8")
                db_doacoes.write(f"{doacao.id};{doacao.titulo};{doacao.descricao};{doacao.categoria};{doacao.data}")
                db_doacoes.close()



    def checa_usuario(self, login, senha):
        for indice in range(len(self.usuarios)):
            if self.usuarios[indice].login == login and self.usuarios[indice].senha == senha:
                return True
        return False

    def realizar_doacao(self):
        print("Informe abaixo os campos necessários para realizar a doação.\n\n")
        titulo = input("Titulo da doação:")
        descricao = input("Descrição :")
        tipo = 0
        categoria = ''
        while tipo != '1' and tipo != '2' and tipo != '3' and tipo != '4' and tipo != '5':
            print("Selecione uma categoria: "
                  "[1]Móvel [2]Automóvel [3]Eletrônica e Eletroeletrônicos [4]Eletrodomesticos [5]Roupa [6]Outros")
            tipo = input("Seleção: ")
            if tipo == '1':
                categoria = "Móvel"
            elif tipo == '2':
                categoria = "Automóvel"
            elif tipo == '3':
                categoria = "Eletrônica e Eletroeletrônicos"
            elif tipo == '4':
                categoria = "Eletrodomesticos"
            elif tipo == '5':
                categoria = "Roupa"
            elif tipo == '6':
                categoria = "Outros"
            else:
                print("\nInforme uma categoria válida!\n")
        data = input("Data  :")
        id = 0
        id_correto = True
        while id_correto:
            id = str(random.randrange(0,1000))
            for doacao in self.doacoes:
                if doacao.id != id:
                    id_correto = False
                else:
                    id_correto = True
        self.cadastrar_doacao(id,titulo,descricao,categoria,data)
        input("Sua doação foi realizada com sucesso!\n[Enter]")
