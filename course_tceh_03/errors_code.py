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


def list_int(*args):
    x = 0
    for a in args:
        if type(a) == int:
            x += 1
    if x < len(args):
        raise ValueError
    else:
        print(tuple(sorted(args)))


try:
    list_int(5, 12, -1, 8, 34)
except ValueError:
    print('Ti dolboeb')
