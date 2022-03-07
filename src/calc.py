from typing import List

def is_prime(n:int) -> bool:
    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
       return False

    i = 3

    while i * i <= n:
        if n % i == 0:
            return False

        i += 2

    return True


def input_numbers(filepath:str) -> List[int]:
    numbers = []

    with open(filepath) as f:
        numbers = list(map(lambda t: int(t), f))

    return numbers
