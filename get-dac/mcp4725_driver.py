import smbus
# raspi-gpio set 2 a0
# raspi-gpio set 3 a0


class MCP4725:
    def __init__(self, dynamic_range: float, address=0x61, verbose: bool = False) -> None:
        self.bus = smbus.SMBus(1)

        self.address = address
        self.wm = 0x00
        self.pds = 0x00

        self.verbose = verbose
        self.dynrange = dynamic_range

    def __del__(self) -> None:
        self.bus.close()
    
    def set_number(self, number: int) -> None:
        """
        Принимает на вход вещественное число и подаёт его представление после квантования на вход ЦАП
        """
        # if not isintance(number, int):
            # print("На вход только числа!!1")
        if not (0 <= number <= 4095):
            print("Число выходит за разрядность MCP4725 (12bit)")
        
        first_byte = self.wm | self.pds | number >> 8
        second_byte = number & 0xFF
        self.bus.write_byte_data(self.address, first_byte, second_byte)

        if self.verbose:
            print(f"Число: {number}, данные I2C: [0x{(self.address << 1):02X}, 0x{first_byte:02X}, 0x{second_byte:02X}]")
        
    def set_voltage(self, voltage: float) -> None:
        """
        Принимает на вход вещественное число и подаёт его двоичное представление после квантования на вход ЦАП
        """
        if not (0.0 <= voltage <= self.dynrange):
            if self.verbose:
                print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynrange:.2f}) В")
                print("Устанавливаем 0.0 В")
            voltage = 0
        self.set_number(int(voltage / self.dynrange * 4095))



if __name__ == "__main__":
    dac = MCP4725(5.22, verbose=True)
    try:
        while True:
            try:
                voltage = float(input("\nВведите напряжение (в вольтах): "))
                dac.set_voltage(voltage)
            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз.\n")
    except KeyboardInterrupt:
        print("Выключение...")
    except Exception as e:
        print(f"Неизвестная ошибка: \"[{e.__class__.__name__}]: {e.args if len(e.args) > 0 else '<no args>'}\"")
    
    dac.__del__()
