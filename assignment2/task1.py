import csv
import statistics
from pathlib import Path

def analyze_numbers_csv(path="numbers.csv"):
    """
    Read numbers from a CSV file and print mean, min, max.
    The function reads all numeric cells (floats/ints) from the file.
    """
    p = Path(path)
    if not p.exists():
        print(f"File not found: {path}")
        return

    nums = []
    with p.open(newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            for cell in row:
                cell = cell.strip()
                if not cell:
                    continue
                try:
                    nums.append(float(cell))
                except ValueError:
                    # skip non-numeric cells
                    continue

    if not nums:
        print("No numeric data found in", path)
        return

    mean_val = statistics.mean(nums)
    min_val = min(nums)
    max_val = max(nums)

    print(f"Count: {len(nums)}")
    print(f"Mean: {mean_val}")
    print(f"Min: {min_val}")
    print(f"Max: {max_val}")

if __name__ == "__main__":
    analyze_numbers_csv("numbers.csv")