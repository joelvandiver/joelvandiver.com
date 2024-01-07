from typing import Callable


def x[T, U](a: T, mapper: Callable[[T], U]) -> U:
    return mapper(a)


print(x(5, lambda x: float(x)))
