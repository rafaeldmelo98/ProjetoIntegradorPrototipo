class Tela:
    def exibirBemVindo(self):
        print("\n=======================================================================\n")
        print("\t\t\t\t\tBem Vindx ao ReApp!")
        print("\n=======================================================================\n")
        return

    def exibirLogin(self):
        user = 0
        while user != '1' or user != '2':
            user = input("\nVoce já possui cadastro?\n(1) Sim, já tenho!\n(2) Não, quero me cadastrar!\n->")
            if user == '1':
                return True
            elif user == '2':
                return False

    def exibirMenu(self):
        selecao = input("\t\t\t\t\tReApp\n\n"
              "Selecione uma opção.\n\n"
              "[1]Realizar Doação\n[2]Buscar Doações\n[3]Sobre o App\n[4]Sair\n\n-> ")
        return selecao


    def erroMensagem(self):
        print("\n============================================================================")
        print("\t\t\t\t\t\t\tOcorreu um erro, tente novamente!")
        print("============================================================================")


    def exibirDoacoes(self):
        print("\t\t\t\t\tReApp\n\n")
        print("Essas são as doações disponíveis no momento!")


    def exibirSobre(self):
        print("Essa aplicação é um prótotipo para um aplicativo mobile desenvolvido e idealizado\n"
              "por Gustavo Henrique, João V. Souza  e Rafael de Melo. O intuito desse aplicativo é\n"
              "facilitar a comunicação entre pessoas que precisam de alguma doação e pessoas que\n"
              "podem realizar essas doações. O aplicativo também visa incentivar as pessoas ao\n"
              "invés de efetuarem descartes irregulares de itens que não mais o satisfazem, terem\n"
              "atitudes altruistas com o próximo e sustentável com o meio ambiente.")