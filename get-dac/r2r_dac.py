import RPi.GPIO as GPIO


class R2R_DAC:
    def __init__(self, gpio_bits: list, dynamic_range: float, verbose: bool = False) -> None:
        self.gpio_bits = gpio_bits
        self.dynrange = dynamic_range
        self.verbose = verbose
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial=0)
    
    def __del__(self) -> None:
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()
    
    def set_number(self, number: int) -> None:
        """
        Принимает целое число на вход и подаёт его двоичное представление на вход ЦАП
        """
        if not (0 <= number <= 255):
            if self.verbose:
                print("Число выходит за допустимый предел 0...255")
                print("Устанавливаем 0")
            number = 0
        bin_from_dec = [int(element) for element in bin(number)[2:].zfill(8)]
        if self.verbose:
            print("Число на вход в ЦАП:", number)
            print("Биты:", bin_from_dec)

        for i in range(len(self.gpio_bits)):
            GPIO.output(self.gpio_bits[i], bin_from_dec[i])

    def set_voltage(self, voltage: float) -> None:
        """
        Принимает на вход вещественное число и подаёт его двоичное представление после квантования на вход ЦАП
        """
        if not (0.0 <= voltage <= self.dynrange):
            if self.verbose:
                print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynrange:.2f}) В")
                print("Устанавливаем 0.0 В")
            voltage = 0
        self.set_number(int(voltage / self.dynrange * 255))


if __name__ == "__main__":
    dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.135, True)
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
