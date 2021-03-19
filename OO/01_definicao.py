
class Animal():

    # Construtor
    def __init__(self, nome, idade=0, som=''):
        # Atributo
        self.nome = nome
        self.idade = idade
        self.som = som

    # Destrutor
    def __del__(self):
        print('fim')

    # Método 01
    def envelhecer(self, anos=1):
        self.idade += anos

    # Método 02
    def emitir_som(self):
        print(self.som)
