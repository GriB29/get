import RPi.GPIO as GPIO


class PWM_DAC:
    def __init__(self, gpio_pin: int, pwm_frequency: float, dynamic_range: float, verbose: bool = False) -> None:
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dynrange = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.gpio_pin, self.pwm_frequency)
        self.pwm.start(.0)
    
    def __del__(self) -> None:
        self.pwm.stop()
        GPIO.cleanup()

    def set_voltage(self, voltage: float) -> None:
        """
        Принимает на вход вещественное число и подаёт его двоичное представление после квантования на вход ЦАП
        """
        if not (0.0 <= voltage <= self.dynrange):
            if self.verbose:
                print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynrange:.2f}) В")
                print("Устанавливаем 0.0 В")
            voltage = 0
        k = voltage / self.dynrange * 100
        if self.verbose:
            print(f"Коэффициент заполнения: {k:.1f}%")
        self.pwm.ChangeDutyCycle(k) # self.set_number( * 255)


if __name__ == "__main__":
    dac = PWM_DAC(12, 500, 3.33, True)
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
    finally:
        dac.__del__()
