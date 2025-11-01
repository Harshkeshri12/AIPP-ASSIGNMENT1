def sum_of_squares(numbers):
    """
    Calculate the sum of squares for a list of numbers
    Example: [1, 2, 3] => 1² + 2² + 3² = 1 + 4 + 9 = 14
    """
    return sum(num ** 2 for num in numbers)

def get_user_numbers():
    """
    Get a list of numbers from user input
    Returns a list of valid numbers
    """
    while True:
        try:
            # Ask user how many numbers they want to input
            n = int(input("\nHow many numbers do you want to enter? "))
            if n <= 0:
                print("Please enter a positive number!")
                continue
            
            numbers = []
            # Get n numbers from the user
            print(f"\nPlease enter {n} numbers:")
            for i in range(n):
                num = float(input(f"Enter number {i+1}: "))
                numbers.append(num)
            
            return numbers
            
        except ValueError:
            print("Invalid input! Please enter valid numbers.")

def main():
    print("Welcome to the Sum of Squares Calculator!")
    
    while True:
        # Get numbers from user
        numbers = get_user_numbers()
        
        # Calculate sum of squares
        result = sum_of_squares(numbers)
        
        # Display results with detailed breakdown
        print("\nCalculation breakdown:")
        for i, num in enumerate(numbers):
            print(f"Number {i+1}: {num}² = {num**2}")
        print(f"\nThe sum of squares is: {result}")
        
        # Ask if user wants to continue
        choice = input("\nWould you like to calculate another sum? (yes/no): ")
        if choice.lower() != 'yes':
            print("Thank you for using the Sum of Squares Calculator!")
            break

if __name__ == "__main__":
    main()
