# Function to find the largest number in a list
from typing import Iterable, Union

Number = Union[int, float]


def find_max_iterative(numbers: Iterable[Number]) -> Number:
	"""
	Find and return the largest number in the iterable using an explicit loop.

	Behavior & contract:
	- Accepts any iterable of numbers (ints and floats).
	- Raises ValueError if the iterable contains no elements.
	- Let Python raise TypeError if elements are not comparable (e.g., mixed types like int and str).

	Complexity:
	- Time: O(n) — a single pass over the data.
	- Space: O(1) — constant extra memory.
	"""
	it = iter(numbers)
	try:
		max_val = next(it)
	except StopIteration:
		raise ValueError("find_max_iterative: input is empty")

	for x in it:
		# Rely on Python's ordering semantics; this will raise if x and max_val are not comparable.
		if x > max_val:
			max_val = x
	return max_val


def find_max_builtin(numbers: Iterable[Number]) -> Number:
	"""
	Find the largest number using Python's built-in max().

	This is concise and relies on Python's optimized implementation. It has the same time/space
	complexity characteristics as the iterative version but delegates checks and comparisons to
	the built-in.
	"""
	try:
		return max(numbers)
	except ValueError:
		# Re-raise with a clearer message consistent with the iterative version
		raise ValueError("find_max_builtin: input is empty")


if __name__ == "__main__":
	# Quick demonstration of both functions and edge cases
	examples = [
		[3, 1, 4, 2],          # normal ints
		[-5, -1, -9],          # negative numbers
		[2.5, 3.7, 1.2],       # floats
		[1, 2.0, 3],           # mixed int/float (valid)
		[],                    # empty -> should raise ValueError
		# [1, 'a', 3]          # uncomment to see TypeError for incomparable elements
	]

	for ex in examples:
		try:
			it = find_max_iterative(ex)
			bi = find_max_builtin(ex)
			print(f"input: {ex!r} -> iterative: {it!r}, builtin: {bi!r}, match: {it==bi}")
		except Exception as e:
			print(f"input: {ex!r} -> raised {type(e).__name__}: {e}")

