

print('Início do programa.')

# Usar o depurador!
# Analizar as variáveis!


# Aqui a função é parametrizada pelos
# parâmetros formais ou parâmetros
# Valor_01 e Valor_02
def funcao_soma(Valor_01, Valor_02):
    # Aqui a função possui os argumentos
    # ou parâmetros reais Valor_01 e Valor_02

    print('\nInício da função funcao_soma')

    print(f"{'Valor_01:':>14}{Valor_01:>5}")
    print(f"{'Valor_02:':>14}{Valor_02:>5}")
    print(f"{'Soma:':>14}{Valor_01 + Valor_02:>5}")

    print('Fim da função funcao_soma\n')


Parametro_01 = 10
Parametro_02 = 12

# Chamando a função funcao_soma()
# e passando os parâmetros Parametro_01 e Parametro_02
# Ou seja parametrizando a função
funcao_soma(Parametro_01, Parametro_02)

print('Fim do programa.')
