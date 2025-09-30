import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

dynamic_range = 3.183
dac_bits = [16, 20, 21, 25, 26, 17, 27, 22]
GPIO.setup(dac_bits, GPIO.OUT)


def voltage_to_number(voltage: float) -> int:
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f}) В")
        print("Устанавливаем 0.0 В")
        return 0
    return int(voltage / dynamic_range * 255)


def number_to_dac(number: int) -> None:
    if not (0 <= number <= 255):
        print("Число выходит за допустимый предел 0...255")
        print("Устанавливаем 0")
        return
    print("Число на вход в ЦАП:", number)
    bin_from_dec = [int(element) for element in bin(number)[2:].zfill(8)]
    print("Биты:", bin_from_dec)

    for i in range(len(dac_bits)):
        GPIO.output(dac_bits[i], bin_from_dec[i])


if __name__ == "__main__":
    try:
        while True:
            try:
                voltage = float(input("\nВведите напряжение (в вольтах): "))
                number = voltage_to_number(voltage)
                number_to_dac(number)
            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз.\n")
    except KeyboardInterrupt:
        print("Выключение...")
    except Exception as e:
        print(f"Неизвестная ошибка: \"[{e.__class__.__name__}]: {e.args if len(e.args) > 0 else '<no args>'}\"")
    
    GPIO.output(dac_bits, 0)
    GPIO.cleanup()
