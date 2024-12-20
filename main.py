"""
Этот модуль реализует классы для умных устройств: ламп, розеток и термостатов.
"""

class SmartHouse:
    """Базовый класс для умного дома."""
    def __init__(self, vendor):
        self.vendor = vendor


#Класс для умных ламп.
class SmartLamp(SmartHouse):
    """Класс для умных ламп."""
    def __init__(self, power, plug, vendor):
        self.power = power
        self.plug = plug
        super().__init__(vendor)

    def __str__(self):
        vendor = 'Производитель: ' + self.vendor
        plug = 'Разьём: ' + str(self.plug)
        power = 'Мощность: ' + str(self.power)
        return f'{vendor}, {plug}, {power}'


class SmartPlug(SmartHouse):
    """Класс для умных розеток."""
    def __init__(self, max_power, vendor):
        self.max_power = max_power
        super().__init__(vendor)

    def __str__(self):
        vendor = 'Производитель: ' + self.vendor
        max_power = 'Максимальная мощность: ' + str(self.max_power)
        return f'{vendor}, {max_power}'


class Thermostat(SmartHouse):
    """Класс для термостатов."""
    def __init__(self, min_temp, max_temp, vendor):
        self.min_temp = min_temp
        self.max_temp = max_temp
        super().__init__(vendor)

    def __str__(self):
        vendor = f'Производитель: {self.vendor}'
        min_temp = f'Мин.Температура: {str(self.min_temp)}'
        max_temp = f'Макс.Температура: {str(self.max_temp)}'
        return f'{vendor}, {min_temp}, {max_temp}'


def remove_device(vendor_name, lamp_container_in, plug_container_in, thermostat_container_in):
    """Удаляет устройства указанного производителя из списков."""
    lamp_container_out = list()
    plug_container_out = list()
    thermostat_container_out = list()

    for lamp in lamp_container_in:
        if lamp.vendor != vendor_name:
            lamp_container_out.append(lamp)
    for plug in plug_container_in:
        if plug.vendor != vendor_name:
            plug_container_out.append(plug)
    for thermostat in thermostat_container_in:
        if thermostat.vendor != vendor_name:
            thermostat_container_out.append(thermostat)

    print('\n----------REM----------')
    print(f'Удалили устройства производителя {vendor_name}\n')

    return lamp_container_out, plug_container_out, thermostat_container_out


def print_lamp(lamp_container):
    """Выводит список умных ламп."""
    print('Умные лампы:')
    for lamp in lamp_container:
        print('\t' + str(lamp))


def print_plug(plug_container):
    """Выводит список умных розеток."""
    print('Умные розетки:')
    for plug in plug_container:
        print('\t' + str(plug))


def print_thermostat(thermostat_container):
    """Выводит список термостатов."""
    print('Термостат:')
    for thermostat in thermostat_container:
        print('\t' + str(thermostat))


def print_smart_all_device(lamp_container, plug_container, thermostat_container):
    """Выводит все умные устройства."""
    print('\n----------PRINT----------')
    if lamp_container:
        print_lamp(lamp_container)
    if plug_container:
        print_plug(plug_container)
    if thermostat_container:
        print_thermostat(thermostat_container)

def add_lamp(lamp_container, power, plug, vendor):
    lamp_container.append(SmartLamp(power, plug, vendor))


def main():
    """Основная программа с работой с объектами."""
    lamp_container = list()
    plug_container = list()
    thermostat_container = list()
    lamp_container.append(SmartLamp(25, 'e24', 'Star'))
    lamp_container.append(SmartLamp(12, 'e14', 'NoName'))
    plug_container.append(SmartPlug(1000, 'Xiaomi'))
    thermostat_container.append(Thermostat(5, 100, 'NoName'))

    print_smart_all_device(lamp_container, plug_container, thermostat_container)
    lamp_container, plug_container, thermostat_container = remove_device('NoName',
                            lamp_container, plug_container, thermostat_container)
    print_smart_all_device(lamp_container, plug_container, thermostat_container)

    print('\n\n\n-------- Work with File --------')

    with open('input-oppo-2.txt', 'r', encoding='UTF-8') as input_txt:
        contents = input_txt.read()

    for line in contents.split('\n'):
        command = line.split()
        if command[0] == 'PRINT':
            print_smart_all_device(lamp_container, plug_container, thermostat_container)
        elif command[0] == 'ADD':
            if command[1] == 'Лампочка':
                lamp_container.append(SmartLamp(*command[2:]))
            elif command[1] == 'Розетка':
                plug_container.append(SmartPlug(*command[2:]))
            elif command[1] == 'Термостат':
                thermostat_container.append(Thermostat(*command[2:]))
            else:
                print('Устройтсво не поддерживается')
        elif command[0] == 'REM':
            remove_device(*command[1:], lamp_container, plug_container, thermostat_container)
        else:
            print('Команда не распознана')

if __name__ == "__main__":
    main()
