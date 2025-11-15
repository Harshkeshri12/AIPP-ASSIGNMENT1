import string

def is_sentence_palindrome(sentence):
    """Return True if the sentence is a palindrome ignoring case, spaces, punctuation."""
    cleaned = ''.join(ch.lower() for ch in sentence if ch.isalnum())
    return cleaned == cleaned[::-1]


# --- AI-generated Test Cases ---
test_sentences = [
    ("A man a plan a canal Panama", True),
    ("No lemon, no melon", True),
    ("Hello World", False),
    ("Was it a car or a cat I saw", True),
    ("Python", False),
    ("Madam, in Eden, I’m Adam", True)
]

print("\n✅ Sentence Palindrome Test Results:")
for s, expected in test_sentences:
    print(f"{s:40} -> {is_sentence_palindrome(s)} (Expected: {expected})")
