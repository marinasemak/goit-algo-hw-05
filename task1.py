from typing import Callable


def caching_fibonacci() -> Callable[[int], int]:
    cache = {}

    def fibonacci(n: int) -> int:
        """
        Calculates fibonacci number
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]

    return fibonacci


calculate_fibonacci = caching_fibonacci()

print(calculate_fibonacci(1))
print(calculate_fibonacci(6))
print(calculate_fibonacci(10))
