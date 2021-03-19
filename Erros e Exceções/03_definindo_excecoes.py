
class WrongNumberError(Exception):
    def __init__(self, message):
        self.message = message


def raise_function(num):
    if num == 9:
        raise WrongNumberError('Não gosto do número 9!')


try:
    raise_function(9)
except WrongNumberError as err:
    print(err)
else:
    print('OK! Não é 9.')

try:
    raise_function(2)
except WrongNumberError as err:
    print(err)
else:
    print('OK! Não é 9.')
