def assign_grade(score):
    """Assign grade based on score:
    90-100: A, 80-89: B, 70-79: C, 60-69: D, <60: F
    """
    if not isinstance(score, (int, float)):
        return "Invalid input"
    if score < 0 or score > 100:
        return "Invalid input"
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


# --- AI-generated Test Cases ---
test_scores = [
    (95, "A"),
    (90, "A"), (89, "B"),
    (80, "B"), (79, "C"),
    (70, "C"), (69, "D"),
    (60, "D"), (59, "F"),
    (0, "F"), (100, "A"),
    (-5, "Invalid input"),
    (105, "Invalid input"),
    ("eighty", "Invalid input")
]

print("\n✅ Grade Assignment Test Results:")
for score, expected in test_scores:
    print(f"Score: {score:>6} -> {assign_grade(score)} (Expected: {expected})")
