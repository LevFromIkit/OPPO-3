import unittest
from io import StringIO
import sys
from main import SmartLamp, SmartPlug, Thermostat, remove_device, print_lamp, print_plug, print_thermostat, print_smart_all_device, add_lamp, main


class TestSmartDevices(unittest.TestCase):
    
    # Включаем максимальный вывод для отладки
    maxDiff = None

    def setUp(self):
        """Создание начальных данных для тестов"""
        self.lamp1 = SmartLamp(25, 'e24', 'Star')
        self.lamp2 = SmartLamp(12, 'e14', 'NoName')
        self.plug1 = SmartPlug(1000, 'Xiaomi')
        self.thermostat1 = Thermostat(5, 100, 'NoName')

        self.lamp_container = [self.lamp1, self.lamp2]
        self.plug_container = [self.plug1]
        self.thermostat_container = [self.thermostat1]

    def test_smart_lamp_creation(self):
        """Тест создания умной лампы и правильного отображения"""
        lamp = SmartLamp(40, 'e27', 'Philips')
        self.assertEqual(lamp.power, 40)
        self.assertEqual(lamp.plug, 'e27')
        self.assertEqual(lamp.vendor, 'Philips')
        self.assertEqual(str(lamp), 'Производитель: Philips, Разьём: e27, Мощность: 40')

    def test_empty_smart_lamp_creation(self):
        """Тест создания умной лампы без указания характеристик и правильного отображения"""
        lamp = SmartLamp('Start')
        self.assertEqual(lamp.power, 40)
        self.assertEqual(lamp.plug, 'e27')
        self.assertEqual(lamp.vendor, 'Start')
        self.assertEqual(str(lamp), 'Производитель: Start, Разьём: e27, Мощность: 40')

    def test_smart_plug_creation(self):
        """Тест создания умной розетки и правильного отображения"""
        plug = SmartPlug(1500, 'Samsung')
        self.assertEqual(plug.max_power, 1500)
        self.assertEqual(plug.vendor, 'Samsung')
        self.assertEqual(str(plug), 'Производитель: Samsung, Максимальная мощность: 1500')

    def test_error_type_smart_plug_creation(self):
        """Тест создания умной розетки с неправильным типом и правильного отображения"""
        plug = SmartPlug('140', 'Samsung')
        self.assertEqual(plug.max_power, 140)
        self.assertEqual(plug.vendor, 'Samsung')
        self.assertEqual(str(plug), 'Производитель: Samsung, Максимальная мощность: 140')

    def test_thermostat_creation(self):
        """Тест создания термостата и правильного отображения"""
        thermostat = Thermostat(0, 50, 'Honeywell')
        self.assertEqual(thermostat.min_temp, 0)
        self.assertEqual(thermostat.max_temp, 50)
        self.assertEqual(thermostat.vendor, 'Honeywell')
        self.assertEqual(str(thermostat), 'Производитель: Honeywell, Мин.Температура: 0, Макс.Температура: 50')

    def test_remove_device(self):
        """Тест удаления устройств указанного производителя"""
        self.lamp_container, self.plug_container, self.thermostat_container = remove_device(
            'NoName', self.lamp_container, self.plug_container, self.thermostat_container)
        
        # Проверяем, что устройство с производителем 'NoName' удалено
        self.assertEqual(len(self.lamp_container), 1)
        self.assertEqual(len(self.plug_container), 1)
        self.assertEqual(len(self.thermostat_container), 0)

    def test_error_remove_device(self):
        """Тест удаления устройств производителя не присутствующего в списке"""
        self.lamp_container, self.plug_container, self.thermostat_container = remove_device(
            'BigName', self.lamp_container, self.plug_container, self.thermostat_container)
        
        # Проверяем, что устройство ни одно устройство не было удалено
        self.assertEqual(len(self.lamp_container), 2)
        self.assertEqual(len(self.plug_container), 1)
        self.assertEqual(len(self.thermostat_container), 1)
    
    def test_empty_remove_device(self):
        """Тест удаления устройств без указания производителя"""
        self.lamp_container, self.plug_container, self.thermostat_container = remove_device(
            'BigName', self.lamp_container, self.plug_container, self.thermostat_container)
        
        # Проверяем, что устройство ни одно устройство не было удалено
        self.assertEqual(len(self.lamp_container), 2)
        self.assertEqual(len(self.plug_container), 1)
        self.assertEqual(len(self.thermostat_container), 1)

    def test_print_lamp(self):
        """Тест правильности вывода списка ламп"""
        output = StringIO()
        sys.stdout = output
        print_lamp(self.lamp_container)
        sys.stdout = sys.__stdout__
        expected_output = "Умные лампы:\n\tПроизводитель: Star, Разьём: e24, Мощность: 25\n\tПроизводитель: NoName, Разьём: e14, Мощность: 12\n"
        self.assertEqual(output.getvalue(), expected_output)

    def test_print_plug(self):
        """Тест правильности вывода списка розеток"""
        output = StringIO()
        sys.stdout = output
        print_plug(self.plug_container)
        sys.stdout = sys.__stdout__
        expected_output = "Умные розетки:\n\tПроизводитель: Xiaomi, Максимальная мощность: 1000\n"
        self.assertEqual(output.getvalue(), expected_output)

    def test_print_thermostat(self):
        """Тест правильности вывода списка термостатов"""
        output = StringIO()
        sys.stdout = output
        print_thermostat(self.thermostat_container)
        sys.stdout = sys.__stdout__
        expected_output = "Термостат:\n\tПроизводитель: NoName, Мин.Температура: 5, Макс.Температура: 100\n"
        self.assertEqual(output.getvalue(), expected_output)

    def test_print_all_devices(self):
        """Тест правильности вывода всех устройств"""
        output = StringIO()
        sys.stdout = output
        print_smart_all_device(self.lamp_container, self.plug_container, self.thermostat_container)
        sys.stdout = sys.__stdout__
        expected_output = (
            "\n----------PRINT----------\n"
            "Умные лампы:\n\tПроизводитель: Star, Разьём: e24, Мощность: 25\n\tПроизводитель: NoName, Разьём: e14, Мощность: 12\n"
            "Умные розетки:\n\tПроизводитель: Xiaomi, Максимальная мощность: 1000\n"
            "Термостат:\n\tПроизводитель: NoName, Мин.Температура: 5, Макс.Температура: 100\n"
        )
        self.assertEqual(output.getvalue(), expected_output)

    def test_add_lamp(self):
        """Тест добавления новой лампы в контейнер"""
        add_lamp(self.lamp_container, 60, 'e27', 'Philips')
        self.assertEqual(len(self.lamp_container), 3)
        self.assertEqual(self.lamp_container[2].power, 60)
        self.assertEqual(self.lamp_container[2].plug, 'e27')
        self.assertEqual(self.lamp_container[2].vendor, 'Philips')

    def test_main_function(self):
        """Тест обработки команд из файла"""
        # Симулируем файл с командами
        file_content = """  PRINT
                            ADD Лампочка 19 54 Volt
                            ADD Розетка 32 NoName
                            ADD Термостат 14 81 JJ
                            PRINT
                            REM NoName
                            PRINT"""
        
        # Используем StringIO для имитации ввода
        input_txt = StringIO(file_content)
        sys.stdin = input_txt

        # Захватываем вывод в StringIO
        output = StringIO()
        sys.stdout = output

        # Выполнение основной программы
        main()

        sys.stdout = sys.__stdout__
        expected_output = (
            "\n----------PRINT----------\n"
            "Умные лампы:\n\tПроизводитель: Star, Разьём: e24, Мощность: 25\n\tПроизводитель: NoName, Разьём: e14, Мощность: 12\n"
            "Умные розетки:\n\tПроизводитель: Xiaomi, Максимальная мощность: 1000\n"
            "Термостат:\n\tПроизводитель: NoName, Мин.Температура: 5, Макс.Температура: 100\n"
            "\n----------REM----------\n"
            "Удалили устройства производителя NoName\n"
            "\n\n----------PRINT----------\n"
            "Умные лампы:\n\tПроизводитель: Star, Разьём: e24, Мощность: 25\n"
            "Умные розетки:\n\tПроизводитель: Xiaomi, Максимальная мощность: 1000\n"
            "\n\n\n-------- Work with File --------\n"
            "\n----------PRINT----------\n"
            "Умные лампы:\n\tПроизводитель: Star, Разьём: e24, Мощность: 25\n"
            "Умные розетки:\n\tПроизводитель: Xiaomi, Максимальная мощность: 1000\n"
            "\n----------PRINT----------\n"
            "Умные лампы:\n\tПроизводитель: Star, Разьём: e24, Мощность: 25\n\tПроизводитель: Volt, Разьём: 54, Мощность: 19\n"
            "Умные розетки:\n\tПроизводитель: Xiaomi, Максимальная мощность: 1000\n\tПроизводитель: NoName, Максимальная мощность: 32\n"
            "Термостат:\n\tПроизводитель: JJ, Мин.Температура: 14, Макс.Температура: 81\n"
            "\n----------REM----------\nУдалили устройства производителя NoName\n"
            "\n\n----------PRINT----------\n"
            "Умные лампы:\n\tПроизводитель: Star, Разьём: e24, Мощность: 25\n\tПроизводитель: Volt, Разьём: 54, Мощность: 19\n"
            "Умные розетки:\n\tПроизводитель: Xiaomi, Максимальная мощность: 1000\n\tПроизводитель: NoName, Максимальная мощность: 32\n"
            "Термостат:\n\tПроизводитель: JJ, Мин.Температура: 14, Макс.Температура: 81\n"
        )
        self.assertEqual(output.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
