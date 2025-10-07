import signal_generator as sg
from r2r_dac import R2R_DAC
from time import time


amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000


if __name__ == "__main__":
    dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.135)
    try:
        while True:
            dac.set_voltage(amplitude * sg.get_sin_wave_amplitude(signal_frequency, time()))
            sg.wait_for_sampling_period(sampling_frequency)
    except KeyboardInterrupt:
        print("Выключение...")
    except Exception as e:
        print(f"Неизвестная ошибка: \"[{e.__class__.__name__}]: {e.args if len(e.args) > 0 else '<no args>'}\"")
    
    dac.__del__()
