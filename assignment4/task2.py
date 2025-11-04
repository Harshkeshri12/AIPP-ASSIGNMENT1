def cm_to_inches():
    cm = float(input("Enter the length in centimeters: "))
    inches = cm / 2.54
    return inches

if __name__ == "__main__":
    result = cm_to_inches()
    print(f"The length in inches is: {result}")