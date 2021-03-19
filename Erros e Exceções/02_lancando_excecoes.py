
def Divisão(dividendo, divisor):
    if not(dividendo.isnumeric() and divisor.isnumeric()):
        # Lança uma exceção do tipo ValuError
        raise ValueError('Um dos valores digitados não é numérico.')

    if float(divisor) == 0:
        # Lança uma exceção do tipo ZeroDivisionError
        raise ZeroDivisionError('Impossível dividir por zero!')

    print('Iniciando Operação matemática!\n')

    quociente = float(dividendo) / float(divisor)
    resto = float(dividendo) % float(divisor)

    return quociente, resto


dividendo = input('Digite o Dividendo: ')
divisor = input('Digite o Divisor: ')

try:
    quociente, resto = Divisão(dividendo, divisor)
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)
else:
    print(f'{dividendo}/{divisor}={quociente} e o resto é {resto}')
finally:
    del(dividendo)
    del(divisor)

    print('\nFinalizando Operação matemática!\n')
