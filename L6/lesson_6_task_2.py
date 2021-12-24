# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
# атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод
# расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина*ширина*масса
# асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу
# метода.
# Например: 20м*5000м*25кг*5см = 12500 т

# Масса 1 кв.м. асфальта толщиной 1 см
asphalt_kg_per_cm = 15


class Road:
    def __init__(self, road_length, road_width, road_depth):
        self._road_length = road_length
        self._road_width = road_width
        self._road_depth = road_depth

    def calc_asphalt_mass(self):
        return self._road_length * self._road_width * self._road_depth * asphalt_kg_per_cm


a_road_length = 10
a_road_width = 20
a_road_depth = 0.05
try:
    my_road = Road(a_road_length, a_road_width, a_road_depth)
    print(f'Масса асфальта: {my_road.calc_asphalt_mass()}')
except TypeError as e2:
    print(f'TypeError: {e2}')
