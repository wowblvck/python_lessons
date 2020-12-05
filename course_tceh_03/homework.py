def get_index(x):
    new_list = ['hi!', 'salam', 12, 64, 'goodboy']
    print(new_list[x])


try:
    my_get_index = int(input('Give index: '))
    get_index(my_get_index)
except ValueError as ve:
    print('Error: ', ve)
except IndexError as ie:
    print('Error: ', ie)s
