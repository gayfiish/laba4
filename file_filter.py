from collections.abc import Iterator


def filter_numbers_from_file(
    filename: str,
    min_value: int,
) -> Iterator[int]:
    """Yield numbers from a file that are not less than min_value."""
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            try:
                number = int(line)
            except ValueError:
                continue

            if number >= min_value:
                yield number


if __name__ == "__main__":
    try:
        min_value = int(input("Enter minimum value: "))

        filtered_numbers = list(
            filter_numbers_from_file("numbers.txt", min_value)
        )

        print("Filtered numbers:", filtered_numbers)
    except ValueError:
        print("Error: enter an integer.")
    except FileNotFoundError:
        print("Error: numbers.txt was not found.")