c = input('Hello! This is a program with homework. type 1 if you want to know about our student, 2 if you want to meet our zoo, 3 if you want to get some info about a book, 4 if you want to know about a watermellon, 5 if you want to read about football match, 6 if you want to have some coffe and 7 if you want to meet our online shop')
if c == 1:
    class Student():
        def __init__(self):
            self.name  = 'Миша'
            self.grade = '7a'

        def say_hello(self):
            print('Здравствуйте! Меня зовут', self.name, 'и я учусь в классе', self.grade)

    student_hi = Student()
    student_hi.say_hello()

if c == 2:
    class Animal():
        def __init__(self):
            self.name = 'Лев Фибин'
            self.sound = 'Рроар'

        def please_say_it(self):
            print('Здравствуйте поситители нашего зоопарка! Это ', self.name, 'и давайте послушаем как он рычит', self.sound)

    animal_l = Animal()
    animal_l.please_say_it()

if c == 3:
    class Book():
        def __init__(self):
            self.name = 'Harry Potter and the Goblet of Fire'
            self.author = 'J. K. Rowling'

        def get_info(self):
            print('Вот некая информация: имя книги:', self.name, 'и автор', self.author)

    book_the_book = Book()
    book_the_book.get_info()

if c == 4:
    class Fruit():
        def __init__(self):
            self.name = 'watemellon'
            self.color = 'green outside and red inside'

        def reveal(self):
            print(f'Name:{self.name}')
            print(f'Color:{self.color}')
            print('This is some info about a fruit called watermelon: it`s name is', self.name, 'and it`s color is', self.color)

    fruit_great = Fruit()
    fruit_great.reveal()

if c == 5:
    class Footballplayer():
        def __init__(self):
            self.name = 'Fobin'
            self.position = 'near the goal'
            self.amount_of_the_scoared_goals = 0

        def scoar_a_goal(self):
            for i in range (10):
                print('Fobin is running throw the other players and the importamt moment! Yes, he is near the goals and now... Goal!')
                self.amount_of_the_scoared_goals = self.amount_of_the_scoared_goals + 1
                print('The amount of goals that Fobin scoared is', self.amount_of_the_scoared_goals)

    player1 = Footballplayer()
    player1.scoar_a_goal()

if c == 6:
    class coffe_machine():
        def __init__(self):
            self.water = 100
            self.coffe = 100

        def make_coffe(self):
            a = input('Which coffe would you like? Espresso or Capuchino?')
            if a == 'Espresso':
                self.water = self.water - 25
                self.coffe = self.coffe - 30
                print('Take your coffe a the table of taking your coffe.')
            if a == 'Capuchino':
                self.coffe = self.coffe - 50
                self.water = self.water - 10
                print('Take your coffe at the table of taking your coffe.')

    coffe = coffe_machine()
    coffe.make_coffe()

class Online_shop():
    def __init__(self):
        self.name = 'family tree'
        self.thing1 = 'rabbit soft toy'
        self.thing2 = 'sofa'
        self.thing3 = 'bed for kids'
        self.thing4 = 'bed for adults'
        self.thing5 = 'dest with chair'
        self.thing6 = 'dining table with 4 chairs'

    def show(self):
        print(f'item1{self.thing1}')
        print(f'item2{self.thing2}')
        print(f'item3{self.thing3}')
        print(f'item4{self.thing4}')
        print(f'item5{self.thing5}')
        print(f'item6{self.thing6}')

    def take_your_bag(self):
        bag_list = []
        a = input('Hello! This is our shop', self.name, 'and we`ve got some items that you might be interested in. Just tipe here the amount of items that you would like to buy')
        for i in range(a):
            b = input('Type here 1 item, that you want to buy')
            b.append(bag_list)
        print('We have made a list of items that you will buy!')

    def pay(self):
        print('Thank you for shopping with "family tree". You have bought items on sum 111 RUB. You can pay us by writing the nuber of your card.')

    def reveal_the_list(self):
        print('And now we will show you the items that you bought:')
        print(*'bag_list')

shop = Online_shop()
shop.show()
shop.take_your_bag()
shop.pay()
shop.reveal_the_list()
