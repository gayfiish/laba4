from collections.abc import Callable, Iterable
from typing import TypeVar, cast


T = TypeVar("T")
_NO_INITIAL = object()


def custom_reduce(
    function: Callable[[T, T], T],
    values: Iterable[T],
    initial: object = _NO_INITIAL,
) -> T:
    """Reduce an iterable to a single value using the given function."""
    iterator = iter(values)

    if initial is _NO_INITIAL:
        try:
            result = next(iterator)
        except StopIteration:
            raise TypeError(
                "custom_reduce() of empty iterable with no initial value"
            )
    else:
        result = cast(T, initial)

    for value in iterator:
        result = function(result, value)

    return result


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]

    total = custom_reduce(lambda x, y: x + y, numbers)
    product = custom_reduce(lambda x, y: x * y, numbers)

    print("Numbers:", numbers)
    print("Sum:", total)
    print("Product:", product)