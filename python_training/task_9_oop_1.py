# Создайте класс Input, принимающий 1 аргумент при инициализации (Loc)
# Создайте объект search (экземпляр класса Input)
# выведите в консоль значение аргумента Loc, объекта search

class Input:

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

class Button:

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

class Title:

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

class Link:
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc


search = Input('Ввод ','input#search')
ok = Button('ОК ', 'button#ok')
local = Title('Название ', 'title#local')
url = Link('Ссылка ', 'link#url')

print(search.text + search.loc)
print(ok.text + ok.loc)
print(local.text + local.loc)
print(url.text + url.loc)