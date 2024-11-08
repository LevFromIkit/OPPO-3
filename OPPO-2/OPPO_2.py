class SmartHouse:
    def __init__(self):
        self.vendor = ''

class SmartLamp(SmartHouse):
    def __init__(self, power = 0, plug = '�� �������', vendor = 'NoName'):
        self.power = power
        self.plug = plug
        self.vendor = vendor
    def __str__(self):
        return '�������������: ' + self.vendor + ', ������: ' + str(self.plug) + ', ��������: ' + str(self.power)

class SmartPlug(SmartHouse):
    def __init__(self, maxPower = 0, vendor = 'NoName'):
        self.maxPower = maxPower
        self.vendor = vendor
    def __str__(self):
        return '�������������: ' + self.vendor + ', ������������ ��������: ' + str(self.maxPower)

class Thermostat(SmartHouse):
    def __init__(self, minTemp = 0, maxTemp = 0, vendor = 'NoName'):
        self.minTemp = minTemp
        self.maxTemp = maxTemp
        self.vendor = vendor
    def __str__(self):
        return '�������������: ' + self.vendor + ', ���.�����������: ' + str(self.minTemp) + ', ����.�����������: ' + str(self.maxTemp)

def removeDevice(vendor_name = ''):
    global lampContainer, plugContainer, thermostatContainer
    lampContainer = [lamp for lamp in lampContainer if lamp.vendor != vendor_name]
    plugContainer = [plug for plug in plugContainer if plug.vendor != vendor_name]
    thermostatContainer = [thermostat for thermostat in thermostatContainer if thermostat.vendor != vendor_name]

def printLamp(index = -1):
    print('����� �����:')
    if index != -1:
        print('\t' + lampContainer[index].print())
    else:
        for i in lampContainer:
            print('\t' + str(i))

def printPlug(index = -1):
    print('����� �������:')
    if index != -1:
        print('\t' + plugContainer[index].print())
    else:
        for i in plugContainer:
            print('\t' + str(i))

def printThermostat(index = -1):
    print('���������:')
    if index != -1:
        print('\t' + thermostatContainer[index].print())
    else:
        for i in thermostatContainer:
            print('\t' + str(i))

def printSmartAllDevice():
    print('\n----------PRINT----------')
    if lampContainer:
        printLamp()
    if plugContainer:
        printPlug()
    if thermostatContainer:
        printThermostat()

lampContainer = []
plugContainer = []
thermostatContainer = []

lampContainer.append(SmartLamp(25, 'e24', 'Star'))
lampContainer.append(SmartLamp(12, 'e14'))
plugContainer.append(SmartPlug(1000, 'Xiaomi'))
thermostatContainer.append(Thermostat(5, 100))

printSmartAllDevice()
removeDevice('NoName')
printSmartAllDevice()

print('\n\n\n-------- Work with File --------')

input_txt = open('C://Users/Honor/Downloads/input-oppo-2.txt', 'r')
for i in input_txt:
    command = i.split()
    if command[0] == 'PRINT':
        printSmartAllDevice()
    elif command[0] == 'ADD':
        if command[1] == '��������':
            lampContainer.append(SmartLamp(*command[2:]))
        elif command[1] == '�������':
            plugContainer.append(SmartPlug(*command[2:]))
        elif command[1] == '���������':
            thermostatContainer.append(Thermostat(*command[2:]))
        else:
            print('���������� �� ��������������')
    elif command[0] == 'REM':
        removeDevice(*command[1:])
    else:
        print('������� �� ����������')