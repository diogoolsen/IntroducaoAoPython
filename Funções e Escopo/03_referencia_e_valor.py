

print('Início do programa.')

# Usar o depurador!
# Analizar as variáveis!


# Os parâmetros são passados por:
#  - cópia de valor quando imutáveis
#  - referência quando mutáveis

# int, float, string, bools ̃sao imutaveis
# portanto a passagem de parâmetros destas
# variáveis é por cópia de valor

def funcao_soma(Valor_01, Valor_02):
    print('\nInício da função funcao_soma')

    print(f"{'Valor_01:':>14}{Valor_01:>5}")
    Valor_01 = 2
    print(f"{'Valor_01:':>14}{Valor_01:>5}")

    print('')

    print(f"{'Valor_01:':>14}{Valor_01:>5}")
    print(f"{'Valor_02:':>14}{Valor_02:>5}")
    print(f"{'Soma:':>14}{Valor_01 + Valor_02:>5}")

    print('Fim da função funcao_soma\n')


Parametro_01 = 10
Parametro_02 = 12

print('Antes da execução da função')
print(f"{'Parametro_01:'}{Parametro_01:>5}")
print(f"{'Parametro_02:'}{Parametro_02:>5}")

funcao_soma(Parametro_01, Parametro_02)

print('Depois da execução da função')
print(f"{'Parametro_01:'}{Parametro_01:>5}")
print(f"{'Parametro_02:'}{Parametro_02:>5}")
# Os valores não foram alterados

print('Fim do programa.')
