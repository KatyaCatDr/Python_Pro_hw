class Rectangle():
    global width
    global length
    def __init__(self):
        width = 0
        length = 0

    def count_area(self):
        a = int(input('Type the lenght of the rectangle: '))
        length = a
        b = int(input('Type the width of the rectangle: '))
        width = b
        print('The area of your rectangle is', a * b)

    def count_perimeter(self):
        c = int(input('Type the lenght of the rectangle: '))
        length = c
        d = int(input('Type the width of the rectangle: '))
        width = d
        print('The perimeter of your rectangle is', c + c + d + d)

rect = Rectangle()
rect.count_area()
rect.count_perimeter()

class Circle():
    global e
    global f
    def __init__(self):
        radius = 0

    def count_area_2(self):
        e = int(input('Type the radius of the circle: '))
        radius = e
        print('The area of your circle is', 3.14 * e ** e)

    def count_perimeter_2(self):
        f = int(input('Type the radius of the circle: '))
        radius = f
        print('The perimeter of your circle is', 2 * 3.14 * f)

circle = Circle()
circle.count_area_2()
circle.count_perimeter_2()

class Triangle():
    global g
    global h
    def __init__(self):
        base = 0
        height = 0

    def count_area_3(self):
        g = int(input('Type the base of your triangle: '))
        base = g
        h = int(input('Type the height of your triangle: '))
        height = h
        print('The area of your triangle is', g * h // 2)

triangle = Triangle()
triangle.count_area_3()# Python_Pro_hw
