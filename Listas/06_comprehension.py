
#################
# LIST COMPREHENSION
#################

# Sintaxe
# NOVA_LISTA = [EXPRESSÃO for ITEM in ITERAVEL if CONDIÇÃO]

# Imprimindo
lista = [1, '1', 1.0, True]

[print(item) for item in lista]

# Obtendo os pares
lista = [1, 2, 3, 4, 5, 6]

pares = [item for item in lista if item % 2 == 0]

print(pares)

# Multiplicando por 2
lista = [1, 2, 3, 4, 5, 6]

dobro = [item * 2 for item in lista]

print(dobro)

# Multiplicando apenas os pares por 3
lista = [1, 2, 3, 4, 5, 6]

dobro = [item * 3 if item % 2 == 0 else item for item in lista]

print(dobro)
