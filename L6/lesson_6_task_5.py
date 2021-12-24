# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод
# draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
# классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки ручкой {self.title}.')

    def asd(self, other):
        other.title = 'a'


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки карандашом {self.title}.')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки маркером {self.title}.')


my_pen = Pen('Pilot')
my_pencil = Pencil('Koh-i-Noor')
my_handle = Handle('Mazari')

my_pen.draw()
my_pen.asd(my_pencil)
my_pencil.draw()
my_handle.draw()
