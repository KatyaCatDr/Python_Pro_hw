import random
'''a = int(input('Введите число'))
b = int(input('Введите число'))
c = int(input('Введите число'))
d = int(input('Введите число'))
def how_many():
    pass


list_1 = [a, b, c, d]
for p in list_1:
    how_many()'''

'''def password_get():
    global list1
    list1 = [1, 5, 'i', 'o', 4, 0, 9, 0]
    for i in range(3):
    a = random.choise(list1)
print(a)'''

def count_symbol(a='', n=''):
    c = 0
    for l in a:
        if l == n:
            c += 1
    print(f'{n} comes out {c} times in the line {a}')

count_symbol('Hello', 'e')
