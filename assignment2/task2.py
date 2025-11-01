def is_palindrome(string):
    # Convert to lowercase and remove non-alphanumeric characters
    cleaned = ''.join(char.lower() for char in string if char.isalnum())
    # Compare string with its reverse
    return cleaned == cleaned[::-1]

def main():
    while True:
        # Get input from user
        user_input = input("\nEnter a string to check if it's a palindrome (or 'quit' to exit): ")
        
        # Check if user wants to quit
        if user_input.lower() == 'quit':
            print("Thank you for using the palindrome checker!")
            break
        
        # Check if the input is a palindrome
        result = is_palindrome(user_input)
        
        # Display result
        if result:
            print(f'"{user_input}" is a palindrome!')
        else:
            print(f'"{user_input}" is not a palindrome.')

if __name__ == "__main__":
    print("Welcome to the Palindrome Checker!")
    main()