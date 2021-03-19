

print('Início do programa.')

# Usar o depurador!
# Analizar as variáveis!


# Os parâmetros são passados por:
#  - cópia de valor quando imutáveis
#  - referência quando mutáveis

# Listas são mutaveis
# portanto a passagem de parâmetros destas
# variáveis é por referência


def adiciona_a_lista(lista_01):
    print('\nInício da função adiciona_a_lista')

    lista_01.append(3)

    print('Fim da função adiciona_a_lista\n')


lista = [2]

print('Antes da execução da função')
print(lista)

lista_02 = lista

adiciona_a_lista(lista_02)

print('Depois da execução da função')
print(lista)

# A lista foi alterada!
# Passagem por referência

print('Fim do programa.')
