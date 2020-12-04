'''
Esse arquivo é responsável pelas classes Doacao e Venda
'''

class Doacao:
    def __init__(self, id, titulo, descricao, categoria, data):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.categoria = categoria
        self.data = data

    def __str__(self):
        return f"ID: {self.id}\n" \
               f"Titulo: {self.titulo}\n" \
               f"Descrição: {self.descricao}\n" \
               f"Categoria: {self.categoria}\n" \
               f"Data: {self.data}\n"


class Venda:
    def __init__(self, id, titulo, descricao, categoria, data, valor):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.categoria = categoria
        self.data = data
        self.valor = valor

    def __str__(self):
        return f"ID: {self.id}\n" \
               f"Titulo: {self.titulo}\n" \
               f"Descrição: {self.descricao}\n" \
               f"Categoria: {self.categoria}\n" \
               f"Data: {self.data}\n" \
               f"Valor: R$ {self.valor}\n"
