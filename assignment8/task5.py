def convert_date_format(date_str):
    """Convert 'YYYY-MM-DD' to 'DD-MM-YYYY'."""
    try:
        y, m, d = date_str.split("-")
        if len(y) != 4 or len(m) != 2 or len(d) != 2:
            return "Invalid format"
        return f"{d}-{m}-{y}"
    except ValueError:
        return "Invalid input"


# --- AI-generated Test Cases ---
test_dates = [
    ("2023-10-15", "15-10-2023"),
    ("1999-01-01", "01-01-1999"),
    ("2025-12-31", "31-12-2025"),
    ("2025-2-28", "Invalid format"),
    ("15-10-2023", "Invalid input")
]

print("\n✅ Date Format Converter Test Results:")
for date_str, expected in test_dates:
    print(f"{date_str:15} -> {convert_date_format(date_str)} (Expected: {expected})")
