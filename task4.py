# Recursive factorial implementation
# Function: factorial_recursive(n)
def factorial_recursive(n):
	"""
	Calculate n! using recursion.

	Args:
		n (int): non-negative integer

	Returns:
		int: n!

	Raises:
		TypeError: if n is not an int
		ValueError: if n is negative
	"""
	if not isinstance(n, int):
		raise TypeError("factorial_recursive: n must be an integer")
	if n < 0:
		raise ValueError("factorial_recursive: n must be >= 0")
	if n in (0, 1):
		return 1
	return n * factorial_recursive(n - 1)


# Iterative factorial implementation
# Function: factorial_iterative(n)
def factorial_iterative(n):
	"""
	Calculate n! using an iterative loop.

	Args:
		n (int): non-negative integer

	Returns:
		int: n!

	Raises:
		TypeError: if n is not an int
		ValueError: if n is negative
	"""
	if not isinstance(n, int):
		raise TypeError("factorial_iterative: n must be an integer")
	if n < 0:
		raise ValueError("factorial_iterative: n must be >= 0")
	result = 1
	for i in range(2, n + 1):
		result *= i
	return result


if __name__ == "__main__":
	# Quick demonstration and verification
	test_values = [0, 1, 5, 10]
	for v in test_values:
		r = factorial_recursive(v)
		it = factorial_iterative(v)
		same = r == it
		print(f"{v}! -> recursive: {r}, iterative: {it}, match: {same}")

	# Edge-case checks
	try:
		factorial_recursive(-1)
	except Exception as e:
		print("factorial_recursive(-1) raised:", type(e).__name__, e)

	try:
		factorial_iterative(-1)
	except Exception as e:
		print("factorial_iterative(-1) raised:", type(e).__name__, e)

