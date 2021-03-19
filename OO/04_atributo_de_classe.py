
class Animal():

    # Definição de atributo de classe
    # Em C++ similar à static member
    planeta = 'Terra'

    def __init__(self, nome, idade=0, som=''):
        self.nome = nome
        self.__idade = idade
        self._som = som

        print(self.nome + ' nasceu com ' + str(self.__idade) + ' anos.')

    def __del__(self):
        print(self.nome + ' morreu.')

    def envelhecer(self, anos=1):
        self.__idade += anos

    def emitir_som(self):
        print(self._som)

    def em_qual_planeta(self):
        # Acesso à atributo de classe
        print(self.__class__.planeta)


bicho_01 = Animal('Canárinho', som='piu')
bicho_02 = Animal('Amarelinho', som='piu')

bicho_01.em_qual_planeta()
bicho_02.em_qual_planeta()

# Acesso à atributo de classe
bicho_01.__class__.planeta = 'Universo'

bicho_01.em_qual_planeta()
bicho_02.em_qual_planeta()
