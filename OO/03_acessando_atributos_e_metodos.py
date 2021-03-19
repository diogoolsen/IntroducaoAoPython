
class Animal():

    def __init__(self, nome, idade=0, som=''):
        # Público
        self.nome = nome
        # Privado
        self.__idade = idade
        # Protegido - Apenas estilo de codificação!
        self._som = som

        print(self.nome + ' nasceu.')

    def __del__(self):
        print(self.nome + ' morreu com ' + str(self.__idade) + ' anos.')

    def envelhecer(self, anos=1):
        self.__idade += anos

    def emitir_som(self):
        print(self._som)


bicho = Animal('canárinho', som='piu', idade=3)
bicho.nome = 'Amarelinho'
bicho._som = 'piu, piu, piu'

# adiciona um novo atributo à classe, porém não altera o privado
bicho.__idade = 50

print(bicho.__idade)

bicho.envelhecer()
bicho.emitir_som()
