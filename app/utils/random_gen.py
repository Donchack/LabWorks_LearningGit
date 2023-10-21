from random import randint


def get_rand_int_seq(min: int, max: int, len: int):
    """
    Возвращает список случайных целых чисел
    в диапазоне от min до max размером len.
    
    Args:
    - min: минимальное число при генерации.
    - max: максимальное число при генерации.
    - len: количество генерируемых чисел.
    
    Returns:
    - Список случайных целых чисел
    """
    return [randint(min, max) for _ in range(len)]