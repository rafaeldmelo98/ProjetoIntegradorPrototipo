import random
from usuario import Usuario
from doacao import Doacao
from doacao import Venda
import os

class Sistema:
    usuarios = []
    doacoes = []
    bazar = []
    ferrovelho = []


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
        documentos = ['usuarios.txt', 'doacoes.txt', 'bazar.txt', 'ferrovelho.txt']
        for documento in documentos:
            db_documentos = open(documento, "r", encoding="utf-8")
            registros = [registro.replace("\n", "") for registro in db_documentos]
            if documento == 'usuarios.txt':
                for usuario in registros:
                    info = usuario.split(";")
                    login = info[0]
                    senha = info[1]
                    user = Usuario(login,senha)
                    self.usuarios.append(user)
            else:
                for item in registros:
                    info = item.split(";")
                    if len(info) > 1:
                        id = info[0]
                        titulo = info[1]
                        descricao = info[2]
                        categoria = info[3]
                        data = info[4]
                        if documento == 'bazar.txt':
                            valor = info[5]
                            venda = Venda(id,titulo,descricao,categoria,data,valor)
                            self.bazar.append(venda)
                        elif documento == 'doacoes.txt':
                            donate = Doacao(id, titulo, descricao, categoria, data)
                            self.doacoes.append(donate)
                        elif documento == 'ferrovelho.txt':
                            ferrovelho = Doacao(id, titulo, descricao, categoria, data)
                            self.ferrovelho.append(ferrovelho)


    def cadastrar_usuario(self, login, senha):
        user = Usuario(login, senha)
        self.usuarios.append(user)
        db_usuarios = open('usuarios.txt', "a", encoding="utf-8")
        db_usuarios.write(f"\n{user.login};{user.senha}")
        db_usuarios.close()


    def listar_anuncios(self, anuncios):
        exibir_todos = False
        escolha = 0
        for anuncio in anuncios:
            print(anuncio)
            if exibir_todos == False:
                escolha = input("Gostaria de exibir o próximo anúncio?\n[1]Sim\n[2]Não\n[3]Exibir Todos\n-> ")
            if escolha == '2':
                return
            elif escolha == '3':
                exibir_todos = True
        if exibir_todos == True:
            input("[Enter]")
        else:
            input("Não há mais anúncios para exibir!\n\n[Enter]")


    def cadastrar_doacao(self, id, titulo, descricao, categoria, data, anuncios, tipo):
        doacao = Doacao(id, titulo, descricao, categoria, data)
        anuncios.append(doacao)
        if tipo == 'doacao':
            db_usuarios = open('doacoes.txt', "a", encoding="utf-8")
            db_usuarios.write(f"\n{doacao.id};{doacao.titulo};{doacao.descricao};{doacao.categoria};{doacao.data}")
            db_usuarios.close()
        elif tipo == 'ferrovelho':
            db_usuarios = open('ferrovelho.txt', "a", encoding="utf-8")
            db_usuarios.write(f"\n{doacao.id};{doacao.titulo};{doacao.descricao};{doacao.categoria};{doacao.data}")
            db_usuarios.close()


    def cadastrar_venda(self, id, titulo, descricao, categoria, valor, data):
        venda = Venda(id, titulo, descricao, categoria, valor, data)
        self.bazar.append(venda)
        db_usuarios = open('doacoes.txt', "a", encoding="utf-8")
        db_usuarios.write(f"\n{venda.id};{venda.titulo};{venda.descricao};{venda.categoria};{venda.valor};{venda.data}")
        db_usuarios.close()


    def receber_anuncio(self, tipo, anuncios):
        escolha = 0
        documento = ''
        while escolha != '1' and escolha != '2':
            if tipo == 'doacao':
                escolha = input("Você gostaria de receber alguma dessas doações?\n[1]Sim\n[2]Não\n\n-> ")
                documento = 'doacoes.txt'
            elif tipo == 'venda':
                escolha = input("Você gostaria de comprar algum desses produtos?\n[1]Sim\n[2]Não\n\n-> ")
                documento = 'bazar.txt'
            elif tipo == 'ferrovelho':
                escolha = input("Você gostaria de adquirir algum desses itens?\n[1]Sim\n[2]Não\n\n-> ")
                documento = 'ferrovelho.txt'
            if escolha == '1':
                doado = True
                while doado:
                    id = input("Informe o ID do produto: ")
                    for doacao in anuncios:
                        if doacao.id == id:
                            anuncios.remove(doacao)
                            input("\nEste produto foi separado para você!\n[Enter]")
                            doado = False
                    if doado == True:
                        resposta = input("Informe um número de ID válido ou digite [1] para CANCELAR.\n[Enter] -> ")
                        if resposta == '1':
                            return
            elif escolha != '1' and escolha != '2':
                input("Por favor, selecione uma opção válida!")
        if os.path.exists(documento):
            os.remove(documento)
            open(documento, "x")
            for anuncio in anuncios:
                if tipo != 'venda':
                    db_documento = open(documento, "a", encoding="utf-8")
                    db_documento.write(f"{anuncio.id};{anuncio.titulo};{anuncio.descricao};{anuncio.categoria};{anuncio.data}\n")
                    db_documento.close()
                else:
                    db_documento = open(documento, "a", encoding="utf-8")
                    db_documento.write(
                        f"{anuncio.id};{anuncio.titulo};{anuncio.descricao};{anuncio.categoria};{anuncio.data};{anuncio.valor}\n")
                    db_documento.close()


    def checa_usuario(self, login, senha):
        for indice in range(len(self.usuarios)):
            if self.usuarios[indice].login == login and self.usuarios[indice].senha == senha:
                return True
        return False


    def realizar_acao(self, lista, anuncios):
        id = 0
        id_correto = True
        while id_correto:
            id = str(random.randrange(0,1000))
            for anuncio in anuncios:
                if anuncio.id != id:
                    id_correto = False
                else:
                    id_correto = True
        if lista[0] == 'doacao':
            self.cadastrar_doacao(id, lista[1], lista[2], lista[3], lista[4], anuncios, 'doacao')
            input("Sua doação foi realizada com sucesso!\n[Enter]")
        elif lista[0] == 'ferrovelho':
            self.cadastrar_doacao(id, lista[1], lista[2], lista[3], lista[4], anuncios, 'ferrovelho')
            input("Seu descarte ao ferro-velho foi realizado com sucesso!\n[Enter]")
        elif lista[0] == 'venda':
            self.cadastrar_venda(id, lista[1], lista[2], lista[3], lista[4], lista[5])
            input("Seu produto foi adicionado ao bazar com sucesso!\n[Enter]")