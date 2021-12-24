# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
# порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
# завершать скрипт.

from time import sleep

# ключ = цвет, значение = список, содержащий время и код цвета
colors = {
    'red': [7, '6;30;41'],
    'yellow': [2, '5;30;43'],
    'green': [1, '6;30;42']
}


class TrafficLight:
    def __init__(self):
        self.__color = None

    def running(self):
        while True:
            self.next_color()
            self.show_color()
            self._wait()

    def next_color(self):
        if self.__color == 'red':
            self.__color = 'yellow'
        elif self.__color == 'yellow':
            self.__color = 'green'
        else:
            self.__color = 'red'

    def show_color(self):
        print(f'\x1b[{colors[self.__color][1]}m{self.__color}\x1b[0m')

    def _wait(self):
        sleep(colors[self.__color][0])


my_tl = TrafficLight()
my_tl.running()
