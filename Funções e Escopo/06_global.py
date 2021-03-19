

print('Início do programa.')

# Usar o depurador!
# Analizar as variáveis!


def funcao_soma(Valor_01, Valor_02):
    print('\nInício da função funcao_soma')

    # a palavra reservada global avisa que será usada uma
    # variável de um escopo MAIS EXTERNO
    global Parametro_01
    Parametro_01 += 1

    print(f"{'Valor_01:':>14}{Valor_01:>5}")
    print(f"{'Valor_02:':>14}{Valor_01:>5}")
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
# Parametro_01 foi alterado

# Não é recomendável usar variáveis globais!

print('Fim do programa.')
