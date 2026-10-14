from functools import wraps
from time import perf_counter
from typing import Callable, TypeVar


T = TypeVar("T")


def measure_time(func: Callable[..., T]) -> Callable[..., T]:
    """Measure and print the execution time of a function."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = perf_counter()

        result = func(*args, **kwargs)

        end_time = perf_counter()
        execution_time = end_time - start_time

        print(f"Execution time: {execution_time:.6f} seconds")

        return result

    return wrapper


@measure_time
def calculate_sum(limit: int) -> int:
    """Return the sum of integers from 0 to limit - 1."""
    return sum(range(limit))


if __name__ == "__main__":
    result = calculate_sum(1_000_000)
    print("Result:", result)