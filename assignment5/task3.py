# Function to calculate nth Fibonacci number using recursion
def fibonacci(n):
    """
    Recursive function to find nth Fibonacci number.
    Formula:
        F(n) = F(n-1) + F(n-2)
    Base Cases:
        F(0) = 0
        F(1) = 1
    """
    if n < 0:
        return "Invalid input! Enter a non-negative number."
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive call
        return fibonacci(n-1) + fibonacci(n-2)


# Main program
print("🔢 Fibonacci Number Calculator (Recursive Method)")
print("------------------------------------------------")

while True:
    try:
        # Take user input
        num = int(input("\nEnter a number (n) to find its Fibonacci value: "))
        # Call recursive function
        result = fibonacci(num)
        print(f"The {num}th Fibonacci number is: {result}")

        # Ask if user wants to continue
        choice = input("Do you want to calculate another number? (yes/no): ").lower()
        if choice != "yes":
            print("Thank you for using Fibonacci Calculator!")
            break
    except ValueError:
        print("❌ Invalid input! Please enter an integer value.")
