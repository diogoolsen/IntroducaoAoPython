from math import sqrt


def quadrado(valor):
    return valor * valor


def subtracao(minuendo, subtraendo):
    return minuendo - subtraendo


def soma(termo_1, termo_2):
    return termo_1 + termo_2


def multiplicacao(multiplicando, multiplicador):
    return multiplicando * multiplicador


def raiz(valor):
    return sqrt(valor)


def inverte_sinal(valor):
    return valor * (-1)


def divisao(dividendo, divisor):
    return dividendo / divisor


def delta(a, b, c):
    return subtracao(quadrado(b), multiplicacao(multiplicacao(4, a), c))


def bhaskara(a, b, c):
    r1 = divisao(
        soma(inverte_sinal(b), raiz(delta(a, b, c))),
        multiplicacao(2, a))

    r2 = divisao(
        subtracao(inverte_sinal(b), raiz(delta(a, b, c))),
        multiplicacao(2, a))

    print('Para a equação: ', a, 'x^2 + ', b, 'x + ', c, ' = 0')
    print('As raizes são: ', r1, ' e ', r2)


# fonte: https://brasilescola.uol.com.br/matematica/formula-bhaskara.htm
bhaskara(1, 12, -13)  # São -1 e 13
bhaskara(2, -16, -18)  # São 9 e -1
