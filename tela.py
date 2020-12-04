'''
Este arquivo é responsável pela exibição de alguns pedaços de código.

Layout para usuário.

'''

class Tela:
    # Exibe tela inicial
    def exibirBemVindo(self):
        print("\n=======================================================================\n")
        print("\t\t\t\t\tBem Vindx ao ReApp!")
        print("\n=======================================================================\n")
        return

    # Exibe tela de login
    def exibirLogin(self):
        user = 0
        while user != '1' or user != '2':
            user = input("\nVoce já possui cadastro?\n(1) Sim, já tenho!\n(2) Não, quero me cadastrar!\n-> ")
            if user == '1':
                return True
            elif user == '2':
                return False

    # Exibe menu principal
    def exibirMenu(self):
        selecao = input("\t\t\t\t\tReApp\n\n"
              "Selecione uma opção.\n\n"
              "[1]Realizar Doação\n[2]Buscar Doações\n[3]Vender item bazar\n[4]Comprar item bazar"
              "\n[5]Descartar item ferro-velho\n[6]Adquirir item ferro-velho"
              "\n[7]Sobre o App\n[8]Sair\n\n-> ")
        return selecao

    # Exibe cabeçalho da função de busca
    def exibirAnuncio(self):
        print("\t\t\t\t\tReApp\n\n")
        print("Estes são os anúncios desta seção disponíveis no momento!")

    # Informa sobre intenções do aplicativo
    def exibirSobre(self):
        print("Essa aplicação é um prótotipo para um aplicativo mobile desenvolvido e idealizado\n"
              "por Gustavo Henrique, João V. Souza  e Rafael de Melo. O intuito desse aplicativo é\n"
              "facilitar a comunicação entre pessoas que precisam de alguma doação e pessoas que\n"
              "podem realizar essas doações. O aplicativo também visa incentivar as pessoas ao\n"
              "invés de efetuarem descartes irregulares de itens que não mais o satisfazem, terem\n"
              "atitudes altruistas com o próximo e sustentável com o meio ambiente.\n\n"
              "O aplicativo também disponibiliza a opção de compra de items, para que usuários tenham\n"
              "a possibilidade de adquirir itens em bom estado por um preço menor do que na loja.\n\n"
              "Há também espaço para itens que estão quebrados e o usuário que descarta este item\n"
              "não vê mais valor, pois para um outro usuário, aquele lixo ainda pode servir de\n"
              "alguma forma!")

    # Exibe formulário
    def exibirFormulario(self, acao):
        print("Informe abaixo os campos necessários para realizar sua venda.\n\n")
        titulo = input("Titulo da doação:   ")
        descricao = input("Descrição :  ")
        tipo = 0
        categoria = ''
        while tipo != '1' and tipo != '2' and tipo != '3' and tipo != '4' and tipo != '5' and tipo != '6':
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
        data = input("Data  :   ")
        if acao == 'venda':
            valor = input("Informe o valor do item: ")
            lista = [acao, titulo, descricao, categoria, data, valor]
            return lista
        lista = [acao,titulo,descricao,categoria,data]
        return lista

    # Exibe mensagem de erro
    def erroMensagem(self):
        print("\n============================================================================")
        print("\t\t\t\t\t\t\tOcorreu um erro, tente novamente!")
        print("============================================================================")

