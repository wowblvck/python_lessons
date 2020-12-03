import random


def random_error():
    i = random.randint(0, 2)
    if i == 0:
        raise ValueError
    elif i == 1:
        raise TypeError
    else:
        raise RuntimeError


try:
    random_error()
except ValueError:
    print('Come on. Warning ValueError')
except TypeError:
    print('Come on. Warning TypeError')
except RuntimeError:
    print('Come on. Warning RuntimeError')
