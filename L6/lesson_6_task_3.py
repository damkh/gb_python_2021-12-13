# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и
# премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В
# классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (
# get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': 0, 'bonus': 0}

    def get_income(self):
        return self._income

    def set_income(self, wage, bonus):
        try:
            self._income = {
                'wage': float(wage),
                'bonus': float(bonus)
            }
        except Exception as e:
            print(f'set_income Error: {e}')

    def __str__(self):
        return f'{self.name} {self.surname} is {self.position} ' \
               f'with wage {self.get_income()["wage"]} and bonus {self.get_income()["bonus"]}'


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        try:
            return f'{self._income["wage"] + self._income["bonus"]}'
        except Exception as e:
            print(f'get_total_income Error: {e}')


my_position = Position('Peter', 'Parker', 'admin')
my_position.set_income(20.1, 30.4)
print(my_position)
print(f'Full name: {my_position.get_full_name()}')
print(f'Total income: {my_position.get_total_income()}')

