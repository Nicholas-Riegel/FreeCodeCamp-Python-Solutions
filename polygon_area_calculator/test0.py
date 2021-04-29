class Rectangle:

    def __init__(x, width, height):
        x.width = width
        x.height = height

    def set_width(x, width):
        x.width = width
    
    def set_height(x, height):
        x.height = height

    def get_area(x):
        return x.width * x.height
    
    def get_perimeter(x):
        return 2*(x.width + x.height)

    def get_diagonal(x):
        return (x.width ** 2 + x.height ** 2) ** .5

    def get_picture(x):
        picture = str()
        if x.width > 50 or x.height > 50:
            return 'Too big for picture.'
        else:
            picture = ('*' * x.width + '\n')*x.height
            return picture

    def get_amount_inside(x, rectangle):
        inside_widths = str(x.width / rectangle.width) .split('.')[0]
        inside_heights = str(x.height / rectangle.height) .split('.')[0]
        return int(inside_widths) * int(inside_heights)

    def __str__(x):
        return 'Rectangle(width='+str(x.width)+', height='+str(x.height)+')'

rect0 = Rectangle(5, 5)
print('Area:', rect0.get_area() )
print('Perimeter:', rect0.get_perimeter() )
print('Picture:\n' + rect0.get_picture() )
rect1 = Rectangle(10, 15)
print('Inside amounts:', rect0.get_amount_inside(rect1))
print(rect0)
print(rect1)

class Square(Rectangle):
    def __init__(x, side):
        x.width = side
        x.height = side
        x.side = side
    
    def set_side(x, side):
        x.width = side
        x.height = side

    def set_width(x, width):
        x.width = width
        x.height = width
        x.side = width

    def set_height(x, height):
        x.width = height
        x.height = height
        x.side = height
    
    def __str__(x):
        return 'Square(side='+str(x.side)+')'

square0=Square(3)
print(square0.get_area())
print(square0)