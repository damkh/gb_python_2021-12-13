"""
4.1 Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
    А также класс «Оргтехника», который будет базовым для классов-наследников.
    Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
    В базовом классе определить параметры, общие для приведенных типов.
    В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
4.2 Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и
    передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
    а также других данных, можно использовать любую подходящую структуру, например словарь.
4.3 Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
    Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
    Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
    изученных на уроках по ООП.
"""

from abc import ABC, abstractmethod

company_departments = ['TOP', 'IT', 'ACC', 'FIN', 'SERVICE']
lcdm_year = 13800*10 ** 9
max_year = 9999


# class Date скопирован из lesson_8_task_1
class Date:
    def __init__(self, str_dd_mm_yyyy):
        self.str_dd_mm_yyyy = str_dd_mm_yyyy
        self.dig_dd = None
        self.dig_mm = None
        self.dig_yyyy = None

    @classmethod
    def date_to_dig(cls, str_dd_mm_yyyy):
        try:
            dig_dates = map(int, str_dd_mm_yyyy.split('-'))
            date_obj = cls(str_dd_mm_yyyy)
            date_obj.dig_dd, date_obj.dig_mm, date_obj.dig_yyyy = dig_dates
            if Date.check_date_items(date_obj.dig_dd, date_obj.dig_mm, date_obj.dig_yyyy):
                return date_obj
            else:
                print(f'Формат даты {str_dd_mm_yyyy} неверен')
        except ValueError as e:
            print(f'Ошибка в формате даты {str_dd_mm_yyyy}, ERROR {e}')
        except Exception as e:
            print(f'ERROR {e} in Date.date_to_dig')

    @staticmethod
    def check_date_items(day, month, year):
        return 1 <= day <= 31 and 1 <= month <= 12 and -lcdm_year < year < max_year


class OfficeEquipmentStore:
    def __init__(self, free_positions):
        self.free_positions = free_positions
        self.equipment_amount_register = {
            'printer': [(0, '01-01-1970')],
            'scanner': [(0, '01-01-1970')],
            'copier': [(0, '01-01-1970')]
        }
        self.equip_ids = []

    def __str__(self):
        print_mes = '*** Состояние склада ***\n'
        for equip in self.equipment_amount_register:
            print_mes += f'\t{equip}: {self.equipment_amount_register[equip]}\n'
        print_mes += f'\tКоличество свободных мест на складе: {self.free_positions}\n'
        print_mes += f'\tОборудование на складе: {self.equip_ids}\n'
        print_mes += '************************'
        return print_mes

    def increase_free_positions(self):
        self.free_positions += 1

    def decrease_free_positions(self):
        self.free_positions -= 1

    def check_if_id_is_in(self, equip_id):
        if equip_id not in self.equip_ids:
            return True
        else:
            print(f'PROBLEM: {equip_id} уже есть на складе')

    def append_to_store(self, equip_id):
        if self.check_if_id_is_in(equip_id):
            self.equip_ids.append(equip_id)
            return True
        else:
            print(f'PROBLEM: Не удалось добавить {equip_id}')

    def register_transfer_to_store(self, equip_key, transfer_date):
        try:
            last_amount = self.equipment_amount_register[equip_key][-1][0]
            new_amount = last_amount + 1
            self.equipment_amount_register[equip_key].append((new_amount, transfer_date))
        except Exception as e:
            print(f'{e} in register_transfer_to_store')
        else:
            return True

    def register_transfer_from_store(self, equip_key, transfer_date):
        try:
            last_amount = self.equipment_amount_register[equip_key][-1][0]
            new_amount = last_amount - 1
            if new_amount >= 0:
                self.equipment_amount_register[equip_key].append((new_amount, transfer_date))
            else:
                print(f'PROBLEM: Количество устройств равно {last_amount}')
        except Exception as e:
            print(f'{e} in register_transfer_from_store')


class OfficeEquipment(ABC):
    def __init__(self, equip_id, equip_manuf, equip_model):
        self.equip_dict = {
            'ID': equip_id,
            'Manufacturer': equip_manuf,
            'Model': equip_model
        }
        self.location = []

    @classmethod
    def receive_to_store(cls, store, equip_id, equip_manuf, equip_model, receive_date):
        try:
            if Date.date_to_dig(receive_date) and store.append_to_store(equip_id):
                an_equipment = cls(equip_id, equip_manuf, equip_model)
                an_equipment.location.append((receive_date, 'Store'))
                store.decrease_free_positions()
                an_equipment.increase_self_amount_in_store(store, receive_date)
                print(f'{equip_id} {equip_manuf} {equip_model} принят на склад {receive_date}')
                return an_equipment
            else:
                print(f'PROBLEM: {equip_id} не принят')
        except Exception as e:
            print(e)

    def transfer_to_department(self, store, transfer_date, department):
        try:
            if Date.date_to_dig(transfer_date) and OfficeEquipment.check_department(department):
                self.location.append((transfer_date, department))
                store.increase_free_positions()
                self.decrease_self_amount_in_store(store, transfer_date)
                print(f'Передача {self.equip_dict["ID"]} в отдел {department} проведена успешно')
            else:
                print(f'PROBLEM: Передача {self.equip_dict["ID"]} в отдел {department} НЕ проведена')
        except Exception as e:
            print(e)

    @abstractmethod
    def increase_self_amount_in_store(self, store, transfer_date):
        pass

    @abstractmethod
    def decrease_self_amount_in_store(self, store, transfer_date):
        pass

    @staticmethod
    def check_department(department):
        if department in company_departments:
            return True
        else:
            print(f'PROBLEM: В компании нет отдела {department}')


class Printer(OfficeEquipment):
    def __init__(self, equip_id, equip_manuf, equip_model):
        super().__init__(equip_id, equip_manuf, equip_model)
        self.is_color = None
        self.print_tech = None
        self.connection_type = {
            'usb': None,
            'rj45': None,
            'wifi': None
        }

    def increase_self_amount_in_store(self, store, transfer_date):
        store.register_transfer_to_store('printer', transfer_date)

    def decrease_self_amount_in_store(self, store, transfer_date):
        store.register_transfer_from_store('printer', transfer_date)


class Scanner(OfficeEquipment):
    def __init__(self, equip_id, equip_manuf, equip_model):
        super().__init__(equip_id, equip_manuf, equip_model)
        self.paper_feed = None
        self.color_deep = None
        self.connection_type = {
            'usb': None,
            'rj45': None,
            'wifi': None
        }

    def increase_self_amount_in_store(self, store, transfer_date):
        store.register_transfer_to_store('scanner', transfer_date)

    def decrease_self_amount_in_store(self, store, transfer_date):
        store.register_transfer_from_store('scanner', transfer_date)


class Copier(OfficeEquipment):
    def __init__(self, equip_id, equip_manuf, equip_model):
        super().__init__(equip_id, equip_manuf, equip_model)
        self.paper_feed = None
        self.print_tech = None

    def increase_self_amount_in_store(self, store, transfer_date):
        store.register_transfer_to_store('copier', transfer_date)

    def decrease_self_amount_in_store(self, store, transfer_date):
        store.register_transfer_from_store('copier', transfer_date)


# Создать склад на 100 мест
store_1 = OfficeEquipmentStore(100)
# Создать 3 типа оборудования (принтер, сканер и копир)
equip_1 = Printer.receive_to_store(store_1, 'PP-12-32312', 'HP', 'LaserJet 435f DN', '14-01-2019')
equip_2 = Scanner.receive_to_store(store_1, 'SS-12-3523', 'Kyocera', 'DX 002 nd', '01-11-2019')
equip_3 = Copier.receive_to_store(store_1, 'CC-13-23253', 'Xerox', 'Ps n332 d2', '20-02-2020')
# Выдать состояние склада
print(store_1)
# Передать equip_1 в отдел IT
equip_1.transfer_to_department(store_1, '15-11-2019', 'IT')
# Выдать история передач оборудования в компании
print(f'История передач оборудования {equip_1.equip_dict["ID"]}: {equip_1.location}')
# Выдать состояние склада
print(store_1)
# Попытка передать equip_2 в отдел ITT - но такого отдела не существует
equip_2.transfer_to_department(store_1, '15-11-2019', 'ITT')
# Принять новое оборудование equip_4 на склад c уже существующим идентификатором CC-13-23253
equip_4 = Copier.receive_to_store(store_1, 'CC-13-23253', 'Xerox', 'KX-22-mcd', '5-11-2019')
# Принять новое оборудование equip_5 на склад с неверно указанной датой
equip_5 = Printer.receive_to_store(store_1, 'PP-123-333', 'Xerox', 'KX-22-mcd', '35-11-2019')
# Выдать состояние склада
print(store_1)
