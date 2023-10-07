import pygame

WIDTH = 360
HEGHT = 650
FPS = 30

cyclecount = 0
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEGHT)) # создаём экземпляр класса экран
pygame.display.set_caption('Flappy bird')
clock = pygame.time.Clock() # отсчёты времени (FPS)

bg = pygame.image.load('img/bg.png') # ИЗОБРАЖЕНИЕ ФОНА
ground = pygame.image.load('img/ground.png') # изб земли
ground_x = 0
bird1 = pygame.image.load('img/bird1.png')
bird_x = 50
bird_y = 250
bird2 = pygame.image.load('img/bird2.png')
bird3 = pygame.image.load('img/bird3.png')

running = True
while running:
    cyclecount = cyclecount + 1
    '''Игровой цикл'''
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # условие нажатие накрестик
            running = False

    ground_x = ground_x - 5
    if ground_x <= -500:
        ground_x = 0

    screen.blit(bg, (0, 0))  # отрисовка
    screen.blit(ground, (ground_x, 570))

    if cyclecount <= 10:
        screen.blit(bird1, (bird_x, bird_y))
    elif cyclecount > 10 and cyclecount <= 20:
        screen.blit(bird2, (bird_x, bird_y))
    elif cyclecount > 20 and cyclecount < 30:
        screen.blit(bird3, (bird_x, bird_y))
    else:
        cyclecount = 0

    pygame.display.flip() # обновление экрана

pygame.quit()

'''Скелет любого проекта или шаблон Pygame
Скелет проекта важен для игры тем, что он даёт игре понять, какие основные функции она должна выполнять.
Например, эти функции чаще всего управление с помощью клавиатуры и функция нажатия на крестик. Также
движение. Это элементы, без которых программа не интересна. А остальные детали в ней - это лишь украше-
ния. Другими словами скелет пректа - это часть без которой программа будет лишь бесконечным видео с 
одиним и тем же кадром
   Графический объект в Python
Графический объект - это объект который нужно вывести на экран со специальной функцией. Можно сазать
что это картинка, для которой можно написать функцию движения. С помощью графических объектов и соз-
даются игры.'''

a = int(input('Введите количество клеток в строке'))
b = int(input('Введите количество строк'))
list = ['#']
d = '#'
for i in range(b):
    for i in range(a - 1):
        if d == '#':
            list.append(' ')
            d = ' '
        else:
            list.append('#')
            d = '#'
    print(''.join(list))
    if list[0] == '#':
        list.clear()
        list = [' ']
        d = ' '
    else:
        list.clear()
        list = ['#']
        d = '#'
