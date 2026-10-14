from collections.abc import Iterator


def is_prime(number: int) -> bool:
    """Return True if the number is prime."""
    if number < 2:
        return False

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False

    return True


def generate_primes(limit: int) -> Iterator[int]:
    """Yield prime numbers from 2 up to the given limit."""
    for number in range(2, limit + 1):
        if is_prime(number):
            yield number


if __name__ == "__main__":
    try:
        limit = int(input("Enter upper limit: "))
        print("Prime numbers:", list(generate_primes(limit)))
    except ValueError:
        print("Error: enter an integer.")