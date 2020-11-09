# A small calculator that adds and subtracts

a = int(input('Введите первое число\n'))
b = int(input('Введите второе число\n'))
znak = input('Введите знак "+" или "-"\n')
if znak == "+":
    print('Сумма чисел равна', a+b)
elif znak == "-":
    print('Разница чисел равна', a-b)
else:
    print('Неверно введен знак')
