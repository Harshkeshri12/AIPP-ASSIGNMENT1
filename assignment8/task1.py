import re

def is_valid_email(email):
    """Validate an email based on given rules:
    - Must contain @ and .
    - Must not start or end with special characters.
    - Should not allow multiple @.
    """
    if email.count('@') != 1:
        return False
    if not email or email[0] in ['.', '@', '_'] or email[-1] in ['.', '@', '_']:
        return False
    if '.' not in email.split('@')[-1]:
        return False
    # simple regex for pattern validation
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return bool(re.match(pattern, email))


# --- Test Cases for is_valid_email ---
test_emails = [
    ("test@example.com", True),
    ("_user@domain.com", False),
    ("user.@domain.com", False),
    ("user@domain", False),
    ("user@domain..com", False),
    ("user@domain.com.", False),
    ("user@@domain.com", False),
    ("username@domain.com", True),
    ("test.email@sub.domain.co.in", True),
    ("@example.com", False)
]

print("✅ Email Validator Test Results:")
for email, expected in test_emails:
    print(f"{email:30} -> {is_valid_email(email)} (Expected: {expected})")

