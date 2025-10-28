# Function to reverse a string
def reverse_string(s):
	"""
	Return the reverse of the given string.

	Args:
		s: The input to reverse. If not a string, it will be converted with str().

	Returns:
		The reversed string.
	"""
	if s is None:
		return ""
	# Ensure we work with a string
	s = str(s)
	# Use slicing which is simple and efficient for reversing
	return s[::-1]


if __name__ == "__main__":
	examples = ["hello", "", "A", 12345, None]
	for e in examples:
		print(f"Original: {e!r} -> Reversed: {reverse_string(e)!r}")

