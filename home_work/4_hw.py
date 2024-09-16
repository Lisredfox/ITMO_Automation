class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def square_rectangle(self):
        return self.width * self.height

    def perimetr_recrangle(self):
        return 2 * (self.width + self.height)


object_1 = Rectangle(10, 10)
object_2 = Rectangle(5, 5)
object_3 = Rectangle(9, 9)

print(f'Площадь объекта 1 = {object_1.square_rectangle()}')
print(f'Периметр объекта 1 = {object_1.perimetr_recrangle()}')
print(f'Площадь объекта 2 = {object_2.square_rectangle()}')
print(f'Периметр объекта 2 = {object_2.perimetr_recrangle()}')
print(f'Площадь объекта 3 = {object_3.square_rectangle()}')
print(f'Периметр объекта 3 = {object_3.perimetr_recrangle()}')


class Math:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print(self.a + self.b)

    def multiplication(self):
        print(self.a * self.b)

    def division(self):
        print(self.a / self.b)

    def subtraction(self):
        print(self.a - self.b)

value = Math(5, 5)
value.addition()
value.multiplication()
value.division()
value.subtraction()


class Button:

    def __init__(self, text, type='кнопка', loc=''):
        self.text = text
        self.type = type
        self.loc = loc

    def click(self):
        print(f'Клик по кнопке {self.text}')

text_box = Button('Text Box')
check_box = Button('Check Box')
radio_button = Button('Radio Button')
web_tables = Button('Web Tables')
buttons = Button('Buttons')
links = Button('Links')
br_links_images = Button('Broken Links - Images')
up_and_down = Button('Upload and Download')
dyn_properties = Button('Dynamic Properties')

text_box.click()
check_box.click()
radio_button.click()
web_tables.click()
buttons.click()
links.click()
br_links_images.click()
up_and_down.click()
dyn_properties.click()
