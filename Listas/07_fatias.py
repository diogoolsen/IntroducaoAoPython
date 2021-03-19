
#################
# Fatiamento
#################

# Sintaxe
# [ INICIO : FIM : INTERVALO ]

lista = range(30)  # GERADOR
print(lista)

lista = list(range(30))
print(lista)

# do 15 em diante
print(lista[15:])

# do 15 ao 20
print(lista[15:20])

# do 15 ao vinte de dois em dois
print(lista[15:20:2])

# Contagem invertida
print(lista[10:-10:])

# Contagem invertida
print(lista[-10:-5:])
