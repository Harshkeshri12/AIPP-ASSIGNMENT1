from typing import Iterable, Tuple


def sum_even_odd(numbers: Iterable[int]) -> Tuple[int, int]:
    """
    Calculate the sum of even numbers and the sum of odd numbers in `numbers`.

    Args:
        numbers: An iterable of integers.

    Returns:
        A tuple (sum_even, sum_odd).

    Example:
        >>> sum_even_odd([1,2,3,4,5])
        (6, 9)  # even sum = 2+4=6, odd sum = 1+3+5=9
    """
    sum_even = 0
    sum_odd = 0

    for n in numbers:
        # Ensure we work with integers; if non-int types are passed, try to convert
        try:
            value = int(n)
        except Exception:
            # skip values that cannot be converted to int
            continue

        if value % 2 == 0:
            sum_even += value
        else:
            sum_odd += value

    return sum_even, sum_odd


def _parse_input_to_list(text: str):
    """Convert a comma/space-separated string of numbers into a list of ints.

    Accepts input like: "1, 2,3,4" or "1 2 3 4" or a mix.
    Non-numeric tokens are ignored.
    """
    # Split on commas first, then on whitespace
    parts = []
    for chunk in text.split(','):
        parts.extend(chunk.split())

    nums = []
    for p in parts:
        if not p:
            continue
        try:
            nums.append(int(p))
        except Exception:
            try:
                # allow floats by converting to int (truncating)
                nums.append(int(float(p)))
            except Exception:
                # ignore non-numeric tokens
                continue
    return nums


def main():
    print("Sum of Even and Odd Numbers Calculator")
    print("Enter a list of numbers (comma or space separated). Type 'quit' to exit.")

    while True:
        text = input("\nEnter numbers: ")
        if text.strip().lower() in ("quit", "q", "exit"):
            print("Goodbye!")
            break

        numbers = _parse_input_to_list(text)
        if not numbers:
            print("No valid numbers found in input. Please try again.")
            continue

        even_sum, odd_sum = sum_even_odd(numbers)
        print(f"Sum of even numbers: {even_sum}")
        print(f"Sum of odd numbers : {odd_sum}")


if __name__ == "__main__":
    main()
