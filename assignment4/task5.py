"""task5: count lines in a text file.

Provides two functions:
- count_lines(filename: str) -> int: return number of lines in the file (raises FileNotFoundError if missing).
- count_lines_in_file() -> int: prompt the user for a filename and return the line count (or -1 on error).
"""

from typing import Optional


def count_lines(filename: str) -> int:
	"""Return the number of lines in the given text file.

	Args:
		filename: Path to the text file.

	Returns:
		The number of lines in the file as an int.

	Raises:
		FileNotFoundError: If the file does not exist.
		OSError: For other I/O related errors.
	"""
	with open(filename, 'r', encoding='utf-8') as f:
		# Use a generator to avoid loading the whole file into memory.
		return sum(1 for _ in f)


def count_lines_in_file() -> int:
	"""Prompt the user for a .txt filename and return its line count.

	Returns -1 on error (file not found or read error).
	"""
	filename = input("Enter the path to the .txt file: ").strip()
	if not filename:
		print("No filename provided.")
		return -1

	try:
		return count_lines(filename)
	except FileNotFoundError:
		print(f"File not found: {filename}")
		return -1
	except Exception as e:
		print(f"Error reading file: {e}")
		return -1


if __name__ == '__main__':
	result = count_lines_in_file()
	if result >= 0:
		print(f"Number of lines: {result}")
