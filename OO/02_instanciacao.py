
class Animal():

    def __init__(self, nome, idade=0, som=''):
        self.nome = nome
        self.idade = idade
        self.som = som

        print(self.nome + ' nasceu.')

    def __del__(self):
        print(self.nome + ' morreu.')

    def envelhecer(self, anos=1):
        self.idade += anos

    def emitir_som(self):
        print(self.som)


# Instânciando objetos
bicho_01 = Animal('bicho')
bicho_02 = Animal('miau', idade=2)
bicho_03 = Animal('rex', som='grrr')
bicho_04 = Animal('canárinho', som='piu', idade=3)

# Excluindo objetos
del(bicho_02)

# O coletor de lixo se encarrega de excluir os restantes

# Não confira nos destrutores!
# Sobre o destrutor em python ver:
# -https://stackoverflow.com/questions/1641219/does-python-have-private-variables-in-classes
