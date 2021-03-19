

print('Início do programa.')

# Usar o depurador!
# Analizar as variáveis!


def funcao_soma(Valor_01, Valor_02):
    print('\nInício da função funcao_soma')

    print(f"{'Valor_01:':>14}{Valor_01:>5}")
    print(f"{'Valor_02:':>14}{Valor_01:>5}")
    print(f"{'Soma:':>14}{Valor_01 + Valor_02:>5}")

    Soma = Valor_01 + Valor_02
    Par = Soma % 2 == 0

    print('Fim da função funcao_soma\n')

    # retorna dois valores

    return Soma, Par


Parametro_01 = 10
Parametro_02 = 12
SomaFinal = 0
Par = False

print('Antes da execução da função')
print(f"{'Parametro_01:'}{Parametro_01:>5}")
print(f"{'Parametro_02:'}{Parametro_02:>5}")
print(f"{'SomaFinal:'}{SomaFinal:>5}")
print(f"{'SomaFinal é Par?:'}{Par:>5}")

# recebe dois valores
SomaFinal, Par = funcao_soma(Parametro_01, Parametro_02)

print('Depois da execução da função')
print(f"{'Parametro_01:'}{Parametro_01:>5}")
print(f"{'Parametro_02:'}{Parametro_02:>5}")
print(f"{'SomaFinal:'}{SomaFinal:>5}")
print(f"{'SomaFinal é Par?:'}{Par:>5}")

print('Fim do programa.')
