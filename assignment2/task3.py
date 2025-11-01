import math  # Importing math module for pi and other mathematical operations

def calculate_circle_area(radius):
    """
    Calculate the area of a circle given its radius
    Area = π * r²
    """
    if radius < 0:  # Check for invalid input
        return "Radius cannot be negative"
    return math.pi * radius ** 2

def calculate_rectangle_area(length, width):
    """
    Calculate the area of a rectangle given its length and width
    Area = length * width
    """
    if length < 0 or width < 0:  # Check for invalid input
        return "Length and width cannot be negative"
    return length * width

def calculate_triangle_area(base, height):
    """
    Calculate the area of a triangle given its base and height
    Area = (base * height) / 2
    """
    if base < 0 or height < 0:  # Check for invalid input
        return "Base and height cannot be negative"
    return (base * height) / 2

def calculate_square_area(side):
    """
    Calculate the area of a square given its side length
    Area = side²
    """
    if side < 0:  # Check for invalid input
        return "Side length cannot be negative"
    return side ** 2

def main():
    while True:
        # Display menu of shapes
        print("\nArea Calculator")
        print("1. Circle")
        print("2. Rectangle")
        print("3. Triangle")
        print("4. Square")
        print("5. Exit")
        
        # Get user's choice
        choice = input("\nSelect a shape (1-5): ")
        
        # Exit condition
        if choice == '5':
            print("Thank you for using the Area Calculator!")
            break
            
        # Process user's choice
        if choice == '1':
            radius = float(input("Enter the radius of the circle: "))
            area = calculate_circle_area(radius)
            print(f"The area of the circle is: {area:.2f} square units")
            
        elif choice == '2':
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            area = calculate_rectangle_area(length, width)
            print(f"The area of the rectangle is: {area:.2f} square units")
            
        elif choice == '3':
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            area = calculate_triangle_area(base, height)
            print(f"The area of the triangle is: {area:.2f} square units")
            
        elif choice == '4':
            side = float(input("Enter the side length of the square: "))
            area = calculate_square_area(side)
            print(f"The area of the square is: {area:.2f} square units")
            
        else:
            print("Invalid choice! Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()
