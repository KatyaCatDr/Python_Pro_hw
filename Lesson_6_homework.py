class Car():
    def __init__(self):
        self.make = 'Sedan'
        self.model = '15'
        self.supplies = 100

    def show(self):
        print(f'Make: {self.make}')
        print(f'Model: {self.model}')

    def car_cheking(self):
        run = True
        while run:
            a = input('Do you want to start/continue riding the car?(yes/no)')
            if a == 'yes':
                print('Ok, you have some supplies! Have a nice ride! You have rode some kilometers! And please watch out for your car supplies!')
                self.supplies -= 10
                print('Your Supplies:', self.supplies)
                if self.supplies == 0:
                    b = input('Sorry, you have no more supplies. Now you can finish your ride or get some more supplies. Would you like to do that?(yes/no)')
                    if b == 'yes':
                        print('Congats! Now you can ride another car!')
                        self.supplies = 100
                    elif b == 'no':
                        print('Ok, that is your shoise. Just let us show you the info of the car, in case you would like to come back.')
                        break
            elif a == 'no':
                print('Ok, that is your shoise. Just let us show you the info of the car, in case you would like to come back.')
                break
car = Car()
car.car_cheking()
car.show()# Python_Pro_hw
