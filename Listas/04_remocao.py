
#################
# Remoção
#################

# Removendo elementos da cauda
# Caso a lista esteja vazia -> IndexError:
lista = [1, '1', 1.0, True]
cauda = lista.pop()
print(cauda)
print(lista.pop())
print(lista.pop())
print(lista.pop())

# Removendo elementos de determinada posição - del
# DESTROI O ELEMENTO!!!
lista = [1, '1', 1.0, True]
print(lista)
del(lista[2])
print(lista)

# Removendo Cauda - pop
# NÃO DESTROI O ELEMENTO!!!
# Caso a lista esteja vazia -> IndexError:
lista = [1, '1', 1.0, True]
print(lista)
x = lista.pop()
print(lista)
print(x)

# Removendo elementos de determinada posição - pop
# NÃO DESTROI O ELEMENTO!!!
# Caso esteja fora de alcance -> IndexError:
lista = [1, '1', 1.0, True]
print(lista)
x = lista.pop(2)
print(lista)
print(x)

# Removendo determinado elemento - remove
# Busca e remove o primeiro elemento igual ao buscado
# Caso não encontre -> ValueError
lista = [1, '1', 1.0, True]
print(lista)
lista.remove('1')
print(lista)

# Limpando a lista
lista = [1, '1', 1.0, True]
print(lista)
lista.clear()
print(lista)
