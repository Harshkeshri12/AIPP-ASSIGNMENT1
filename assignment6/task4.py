def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Example
print("Sum of first 10 numbers:", sum_to_n(10))
