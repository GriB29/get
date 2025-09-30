from numpy import sin, pi
from time import sleep


def get_sin_wave_amplitude(freq: float, time: float) -> float:
    """
    Возвращает сдвинутую вверх нормализованную форму функции sin(2pi * freq * time)
    [-1, 1] -> [0, 2] -> [0, 1]
    """
    return (sin(2 * pi * freq * time) + 1) / 2

def wait_for_sampling_period(sampling_frequency: float) -> None:
    """
    Ждёт 1 период заданной частоты
    """
    sleep(1 / sampling_frequency)
