
def Divisão(dividendo, divisor):
    print('Iniciando Operação matemática!\n')

    try:
        quociente = float(dividendo) / float(divisor)

    except ZeroDivisionError as err:
        # Trata erro do tipo ZeroDivisionError
        print('Impossível dividir por zero!')
        print(err)

        quociente = 0
        resto = float(dividendo)

    except ValueError as err:
        # Trata erro do tipo TypeError
        print('Um dos valores digitados não é numérico.')
        print(err)

        quociente = 0
        resto = 0

    else:
        # Caso não ocorra erro
        resto = float(dividendo) % float(divisor)

        print('Divisão concluída!')

    finally:
        # Finalzia o bloco
        # Normalmente usado para liberar algum recurso,
        # como fechar arquivo ou desconectar do banco

        del(dividendo)
        del(divisor)

        print('Finalizando Operação matemática!\n')

    return quociente, resto


dividendo = input('Digite o Dividendo: ')
divisor = input('Digite o Divisor: ')

quociente, resto = Divisão(dividendo, divisor)

print(f'{dividendo}/{divisor}={quociente} e o resto é {resto}')
