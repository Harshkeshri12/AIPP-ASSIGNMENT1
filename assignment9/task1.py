def sum_even_odd(numbers):
    """Calculate the sum of even and odd numbers in a list.

    Args:
        numbers (list): A list of integers.

    Returns:
        tuple: A tuple containing:
            - int: Sum of even numbers.
            - int: Sum of odd numbers.
    """
    even_sum = 0
    odd_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    return even_sum, odd_sum


print(sum_even_odd([1, 2, 3, 4, 5, 6]))
