def is_prime(n):
    """
    Check if a number is prime.
    
    Args:
        n (int): The number to check
    
    Returns:
        bool: True if the number is prime, False otherwise
    """
    # Handle edge cases
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd numbers up to the square root of n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True

# Example usage
if __name__ == "__main__":
    # Test some numbers
    test_numbers = [2, 3, 4, 17, 20, 97]
    for num in test_numbers:
        print(f"{num} is{' ' if is_prime(num) else ' not '}prime")
