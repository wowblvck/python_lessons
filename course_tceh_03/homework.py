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


def my_args(x, y):
    if x > 0 and y > 0:
        return x + y
    elif x < 0 and y < 0:
        return x - y
    elif (x > 0 > y) or (x < 0 < y):
        return 0


print(my_args(-5, -2))


def max_args(x, y, z):
    lst = [x, y, z]
    lst.sort()
    print(lst[1], lst[2])


max_args(5, -3, 17)


def list_numbers(*lnums, flag_bool):
    result_num = []
    if flag_bool:
        for nums in lnums:
            if nums % 2 != 0:
                result_num.append(nums)
        print(result_num)
    else:
        for nums in lnums:
            if nums % 2 == 0:
                result_num.append(nums)
        print(result_num)


list_numbers(5, 4, 16, 32, 64, 25, flag_bool=True)


def all_args(*args):
    l_args = list(args)
    l_args.sort()
    print(l_args[0], l_args[-1])


all_args(5, 14, 2, 51, 112, -5, -4, 18)


def string_case(string, up_or_low=True):
    if up_or_low:
        return string.upper()
    else:
        return string.lower()


print(string_case('Hi tTHes', False))


def string_max(*strings, glue=':'):
    string_list = []
    for three_string in strings:
        if len(three_string) > 3:
            string_list.append(three_string)
    return glue.join(string_list)


print(string_max('hi', 'indar', 'how', 'u', 'deal'))
