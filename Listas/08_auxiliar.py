
#################
# Funções Auxiliares
#################

#################
# Cópia de listas
#################

# Referência
# É referência e não cópia
lista1 = [1, '1', 1.0, True]

lista2 = lista1
lista2.pop()

print(lista1)
print(lista2)

# Intervalo
lista1 = [1, '1', 1.0, True]

lista2 = lista1[::]
lista2.pop()

print(lista1)
print(lista2)

# Comprehension
lista1 = [1, '1', 1.0, True]

lista2 = [item for item in lista1]
lista2.pop()

print(lista1)
print(lista2)

# Iterador
lista1 = [1, '1', 1.0, True]

lista2 = []

for item in lista1:
    lista2.append(item)

lista2.pop()

print(lista1)
print(lista2)

# Operador +=
lista1 = [1, '1', 1.0, True]

lista2 = []

lista2 += lista1

lista2.pop()

print(lista1)
print(lista2)


#################
# Range
#################

lista = range(30)  # GERADOR
print(lista)

lista = list(range(30))  # Gera a lista
print(lista)


#################
# Sort
#################

lista = [3, 9, 1, 5, 2, 0]
print(lista)

lista.sort()
print(lista)

lista = ['professor', 'aluno', 'estudante', 'diretor', 'pedagogo', 'técnico']
print(lista)

lista.sort()
print(lista)
