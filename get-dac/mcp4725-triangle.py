import signal_generator as sg
from mcp4725_driver import MCP4725
from time import time


amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000


if __name__ == "__main__":
    dac = MCP4725(5.22)
    try:
        while True:
            dac.set_voltage(amplitude * sg.get_triangle_amplitude(signal_frequency, time()))
            sg.wait_for_sampling_period(sampling_frequency)
    except KeyboardInterrupt:
        print("Выключение...")
    except Exception as e:
        print(f"Неизвестная ошибка: \"[{e.__class__.__name__}]: {e.args if len(e.args) > 0 else '<no args>'}\"")
