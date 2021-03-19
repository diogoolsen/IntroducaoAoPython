

print('Início do programa.')

# Usar o depurador!
# Analizar as variáveis!

# O Código não executa!!


def funcao_soma(Valor_01, Valor_02):
    print('\nInício da função funcao_soma')

    Valor_01 += 1
    print(id(Valor_01))

    # A Variável Parametro_01 não existe dentro
    # do escopo de funcao_soma
    Parametro_01
    print(id(Parametro_01))
    print(Parametro_01)

    print(f"{'Valor_01:':>14}{Valor_01:>5}")
    print(f"{'Valor_02:':>14}{Valor_02:>5}")
    print(f"{'Soma:':>14}{Valor_01 + Valor_02:>5}")

    print('Fim da função funcao_soma\n')


Parametro_01 = 10
Parametro_02 = 12

# print(id(Parametro_01))

funcao_soma(Parametro_01, Parametro_02)

print(Parametro_01)

# A variável Valor_01 não existe fora do escopo de funcao_soma
# Valor_01 += 1

print('Fim do programa.')
