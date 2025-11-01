import csv
import statistics
from typing import Tuple

def calculate_csv_stats(filename: str) -> Tuple[float, float, float]:
    """
    Read a CSV file and calculate basic statistics (mean, min, max).
    Assumes the first column contains numeric values.
    Skips header row and any non-numeric values.
    
    Args:
        filename: Path to the CSV file
        
    Returns:
        Tuple containing (mean, minimum, maximum)
    """
    numbers = []
    
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row
        
        for row in csv_reader:
            if row:  # Check if row is not empty
                try:
                    num = float(row[0])  # Try to convert first column to float
                    numbers.append(num)
                except (ValueError, IndexError):
                    continue  # Skip non-numeric values
    
    if not numbers:
        raise ValueError("No valid numeric values found in the CSV file")
    
    return (
        statistics.mean(numbers),
        min(numbers),
        max(numbers)
    )

def main():
    print("CSV Statistics Calculator")
    print("------------------------")
    
    while True:
        try:
            # Get input from user
            filename = input("\nEnter CSV file path (or 'quit' to exit): ")
            
            if filename.lower() == 'quit':
                print("\nThank you for using the CSV Statistics Calculator!")
                break
            
            # Calculate statistics
            mean, minimum, maximum = calculate_csv_stats(filename)
            
            # Display results
            print(f"\nResults:")
            print(f"Mean   : {mean:.2f}")
            print(f"Minimum: {minimum:.2f}")
            print(f"Maximum: {maximum:.2f}")
            
        except FileNotFoundError:
            print(f"\nError: File '{filename}' not found!")
        except ValueError as e:
            print(f"\nError: {str(e)}")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()