class SmartHouse:
    def __init__(self):
        self.vendor = ''


class SmartLamp(SmartHouse):
    def __init__(self, power=0, plug='не указано', vendor='NoName'):
        self.power = power
        self.plug = plug
        self.vendor = vendor

    def __str__(self):
        return f'Производитель: {self.vendor}, Разьём: {str(self.plug)}, Мощность: {str(self.power)}'


class SmartPlug(SmartHouse):
    def __init__(self, max_power=0, vendor='NoName'):
        self.max_power = max_power
        self.vendor = vendor

    def __str__(self):
        return f'Производитель: {self.vendor}, Максимальная мощность: {str(self.max_power)}'


class Thermostat(SmartHouse):
    def __init__(self, min_temp=0, max_temp=0, vendor='NoName'):
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.vendor = vendor

    def __str__(self):
        return f'Производитель: {self.vendor}, Мин.Температура: {str(self.min_temp)}, Макс.Температура: {str(self.max_temp)}'


def remove_device(vendor_name=''):
    global lampContainer, plugContainer, thermostatContainer
    lampContainer = [lamp for lamp in lampContainer if lamp.vendor != vendor_name]
    plugContainer = [plug for plug in plugContainer if plug.vendor != vendor_name]
    thermostatContainer = [thermostat for thermostat in thermostatContainer if thermostat.vendor != vendor_name]
    print('\n----------REM----------')
    print(f'Удалили устройства производителя {vendor_name}\n')


def print_lamp(index=-1):
    print('Умные лампы:')
    if index != -1:
        print('\t' + lampContainer[index].print())
    else:
        for i in lampContainer:
            print('\t' + str(i))


def print_plug(index=-1):
    print('Умные розетки:')
    if index != -1:
        print('\t' + plugContainer[index].print())
    else:
        for i in plugContainer:
            print('\t' + str(i))


def print_thermostat(index=-1):
    print('Термостат:')
    if index != -1:
        print('\t' + thermostatContainer[index].print())
    else:
        for i in thermostatContainer:
            print('\t' + str(i))


def print_smart_all_device():
    print('\n----------PRINT----------')
    if lampContainer:
        print_lamp()
    if plugContainer:
        print_plug()
    if thermostatContainer:
        print_thermostat()


lampContainer = []
plugContainer = []
thermostatContainer = []

lampContainer.append(SmartLamp(25, 'e24', 'Star'))
lampContainer.append(SmartLamp(12, 'e14'))
plugContainer.append(SmartPlug(1000, 'Xiaomi'))
thermostatContainer.append(Thermostat(5, 100))

print_smart_all_device()
remove_device('NoName')
print_smart_all_device()

print('\n\n\n-------- Work with File --------')

with open('input-oppo-2.txt', 'r') as input_txt:
    contents = input_txt.read()

for i in contents.split('\n'):
    command = i.split()
    if command[0] == 'PRINT':
        print_smart_all_device()
    elif command[0] == 'ADD':
        if command[1] == 'Лампочка':
            lampContainer.append(SmartLamp(*command[2:]))
        elif command[1] == 'Розетка':
            plugContainer.append(SmartPlug(*command[2:]))
        elif command[1] == 'Термостат':
            thermostatContainer.append(Thermostat(*command[2:]))
        else:
            print('Устройтсво не поддерживается')
    elif command[0] == 'REM':
        remove_device(*command[1:])
    else:
        print('Команда не распознана')
