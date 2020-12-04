'''
Esse arquivo é responsável pela classe Usuário
'''

class Usuario:
    def __init__(self, login, senha):
        self.__login = login
        self.__senha = senha


    def __str__(self):
        return f"-{self.login}-{self.senha}-"


    @property
    def login(self):
        return self.__login


    @property
    def senha(self):
        return self.__senha
