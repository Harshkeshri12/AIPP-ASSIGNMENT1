def classify_age(age):
    if age < 0:
        return "Invalid age"
    elif age < 13:
        return "Child"
    elif age < 20:
        return "Teenager"
    elif age < 60:
        return "Adult"
    else:
        return "Senior Citizen"

# Example usage
print(classify_age(8))
print(classify_age(17))
print(classify_age(35))
print(classify_age(70))
