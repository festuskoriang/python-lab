from utils import celsius_to_fahrenheit, is_even, square


def main():
    number = float(input("Enter a number: "))

    print(f"Square: {square(number)}")
    print(f"Parity: {'even' if is_even(number) else 'odd'}")
    print(f"Fahrenheit: {celsius_to_fahrenheit(number)}")


if __name__ == "__main__":
    main()