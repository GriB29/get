from numpy import sin, pi, floor
from time import sleep


def get_sin_wave_amplitude(freq: float, time: float) -> float:
    """
    Возвращает сдвинутую вверх нормализованную форму функции sin(2pi * freq * time)
    [-1, 1] -> [0, 2] -> [0, 1]
    """
    return (sin(2.0 * pi * freq * time) + 1.0) / 2.0

def wait_for_sampling_period(sampling_frequency: float) -> None:
    """
    Ждёт 1 период заданной частоты
    """
    sleep(1.0 / sampling_frequency)

def get_triangle_amplitude(freq: float, time: float) -> float:
    """
    Возвращает треугольный сигнал [0, 1]
    """
    return abs(2.0 * (time * freq - floor(time * freq)) - 1)
