import turtle


def count_sum(a = 0, b = 0):
    print(a + b)


def name_get():
    nm = input('Как вас зовут?')
    print('Привет', nm)


a = int(input('Введите число'))
b = int(input('Введите число'))
c = int(input('Введите число'))
d = int(input('Введите число'))
e = int(input('Введите число'))
number_list = [a, b, c, d, e]
# print(number_list[0])

a = int(input('Type the number'))
b = int(input('Type the other number'))
count_sum(a, b)

name_get()
