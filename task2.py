import re
from typing import Callable


def generator_numbers(text: str):
    """
    Generator function takes all floats from the text
    """
    words_list = re.findall(r"\s\d+\.\d+\s", text)
    for num in words_list:
        yield float(num)


def sum_profit(text: str, func: Callable):
    """
    Sum all float numbers
    """
    sum = 0
    for k in generator_numbers(text):
        sum += k
    return sum


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
