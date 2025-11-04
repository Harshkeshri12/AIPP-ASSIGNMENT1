"""Name formatter that converts full names to 'Last, First' format.

Example usage:
    format_name("John Smith") -> "Smith, John"
    format_name("Mary Jane Wilson") -> "Wilson, Mary Jane"
    format_name("Lee") -> "Lee"
"""

def format_name(full_name: str) -> str:
    """Convert a full name to 'Last, First' format.
    
    Args:
        full_name: A string containing first and last names,
                  optionally including middle name(s).
    
    Returns:
        Formatted name as 'Last, First Middle' or original string
        if only one word is provided.
    """
    # Split the name into parts
    parts = full_name.strip().split()
    
    # Handle single name case
    if len(parts) <= 1:
        return full_name.strip()
        
    # Last name is the final part
    last = parts[-1]
    # First (and middle) names are everything else
    first = " ".join(parts[:-1])
    
    return f"{last}, {first}"


def test_format_name():
    """Test the name formatter with example cases."""
    # Test case 1: First + Last
    assert format_name("John Smith") == "Smith, John"
    
    # Test case 2: First + Middle + Last
    assert format_name("Mary Jane Wilson") == "Wilson, Mary Jane"
    
    # Test case 3: Single name
    assert format_name("Lee") == "Lee"
    
    # Extra test cases
    assert format_name("  Bob  Jones  ") == "Jones, Bob"  # Extra spaces
    print("All tests passed!")


if __name__ == "__main__":
    # Run tests
    test_format_name()
    
    # Interactive demo
    print("\nEnter a name to format (or press Ctrl+C to exit):")
    try:
        while True:
            name = input("> ")
            if name.strip():
                print(format_name(name))
    except KeyboardInterrupt:
        print("\nGoodbye!")
