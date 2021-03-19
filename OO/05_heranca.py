
class Animal():

    def __init__(self, nome, idade=0, som=''):
        self.nome = nome
        self.__idade = idade
        self._som = som

        print(self.nome + ' nasceu')

    def __del__(self):
        print(self.nome + ' morreu com ' + str(self.__idade) + ' anos.')

    def envelhecer(self, anos=1):
        self.__idade += anos

    def emitir_som(self):
        print(self._som)


class Passaro(Animal):

    def voar(self):
        print('voando ...')


class Mamifero(Animal):
    # Acessando o construtor da classe pai
    def __init__(self, nome, idade=0, som=''):
        # Indica qual das superclasses deve ser usada
        # Envia uam referência do próprio objeto (self)

        # Python oferece herança múltipla
        Animal.__init__(self, nome, idade, som)

    def emitir_som(self):
        print('grr')

    def andar(self):
        print('andando ...')


p = Passaro('Canário', som='piu')
m = Mamifero('Rex')

# Acessando Método da Superclasse
p.envelhecer()
m.envelhecer()

# Acessando método sobrescrito
p.emitir_som()
m.emitir_som()

# Acessando método das classes filhas
p.voar()
# m.voar()  # - Erro
# p.andar()  # - Erro
m.andar()
