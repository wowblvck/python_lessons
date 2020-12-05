new_list = ['hi!', 'salam', 12, 64, 'goodboy']
try:
    my_get_index = int(input('Give index: '))
    if my_get_index >= 0 and my_get_index >= len(new_list):
        raise IndexError
    print(new_list[my_get_index])
except ValueError:
    print('Неверное значение')
except IndexError:
    print('Неверный индекс')
