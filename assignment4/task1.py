("""Leap year checker (assignment task)

Provides a single function `is_leap_year(year)` that returns True when
`year` is a leap year under the Gregorian rules, otherwise False.

When run as a script it runs a short set of assertions and prints
example output.
""")

from __future__ import annotations

def is_leap_year(year) -> bool:
	"""Return True if `year` is a leap year (Gregorian calendar).

	Rules:
	- Every year divisible by 4 is a leap year,
	  except years divisible by 100 are not leap years,
	  except years divisible by 400 are leap years.

	Args:
		year: An integer year (or int-coercible). Must be non-negative.

	Returns:
		True if leap year, False otherwise.

	Raises:
		TypeError: if `year` cannot be converted to int.
		ValueError: if `year` is negative.
	"""
	try:
		y = int(year)
	except Exception:
		raise TypeError("year must be an integer") from None

	if y < 0:
		raise ValueError("year must be non-negative")

	return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)


def _run_self_test() -> None:
	# Happy-path assertions
	assert is_leap_year(2000) is True   # divisible by 400
	assert is_leap_year(2400) is True
	assert is_leap_year(2004) is True   # divisible by 4, not 100
	assert is_leap_year(1900) is False  # divisible by 100 but not 400
	assert is_leap_year(2001) is False
	assert is_leap_year(0) is True      # year 0 treated as leap (0 % 400 == 0)


if __name__ == "__main__":
	_run_self_test()

	example_years = [1900, 2000, 2004, 2001, 0, 2400]
	for y in example_years:
		print(f"{y}: {'Leap' if is_leap_year(y) else 'Not Leap'}")



































































