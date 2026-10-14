def filter_even_numbers(numbers):
    return list(filter(lambda number: number % 2 == 0, numbers))


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    even_numbers = filter_even_numbers(numbers)

    print("Original list:", numbers)
    print("Even numbers:", even_numbers)