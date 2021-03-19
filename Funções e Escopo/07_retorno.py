

print('Início do programa.')

# Usar o depurador!
# Analizar as variáveis!

# Formalmente o retorno é considerado um parâmetro


def funcao_soma(Valor_01, Valor_02):
    print('\nInício da função funcao_soma')

    print(f"{'Valor_01:':>14}{Valor_01:>5}")
    print(f"{'Valor_02:':>14}{Valor_01:>5}")
    print(f"{'Soma:':>14}{Valor_01 + Valor_02:>5}")

    print('Fim da função funcao_soma\n')

    # Soma = Valor_01 + Valor_02
    # return Soma

    return Valor_01 + Valor_02

    # Nada mais é executado depois do return


Parametro_01 = 10
Parametro_02 = 12
SomaFinal = 0

print('Antes da execução da função')
print(f"{'Parametro_01:'}{Parametro_01:>5}")
print(f"{'Parametro_02:'}{Parametro_02:>5}")
print(f"{'SomaFinal:'}{SomaFinal:>5}")

SomaFinal = funcao_soma(Parametro_01, Parametro_02)

print('Depois da execução da função')
print(f"{'Parametro_01:'}{Parametro_01:>5}")
print(f"{'Parametro_02:'}{Parametro_02:>5}")
print(f"{'SomaFinal:'}{SomaFinal:>5}")
# SomaFinal foi alterado

print('Fim do programa.')
