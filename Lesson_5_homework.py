'''Свободное падение - это ускорение в падении. Другими словами это когда
что-то падает, и при падении ускоряется. Это естественный факт. Эсли
объект падает просто (свободоно), то объект при этом ускоряется, так
как приближается к земле и атмосфера давит на него.'''
'''br = 0
a = input('How will you name the person?')
class Person():
    def __init__(self):
        self.name = a
        self.age = 0

    def show(self):
        print('Info')
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')

    def say_hello(self):
        print('Hello, my name is', self.name, 'and I am', self.age, 'years old.')

    def say_age(self):
        for i in range(18):
            self.age = self.age + 1
            b = input('Should we continue? (yes/no)')
            if b == 'yes':
                print(a, 'is', self.age, 'years old')
                pr.is_adult()
            else:
                print('Ok. Thank you for using our programm.')
                pr.is_adult()

    def is_adult(self):
        if self.age >= 18:
            print(a, 'is adult.')
        if self.age < 18:
            print(a, 'is not adult.')


pr = Person()
pr.show()
pr.say_hello()
pr.say_age()'''
class Animal():
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def speak(self):
        print('Roar, moooooooo, kwa, meeeeee')

class Lion():
    def eat(self):
        d = input('Do you want to play with ths lion? (yes/no)')
        if d == 'yes':
            print('Ok. Have a great time together!')
        else:
            print('OK. If you said no because you thought he will bite you, then don`t worry. He is friendly', self.color, 'lion')

animal = Animal(Lion, 'yellow')
animal.speak()
lion = Lion()
lion.eat()
print(animal)# Python_Pro_hw
