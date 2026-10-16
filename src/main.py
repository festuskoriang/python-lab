from utils import celsius_to_fahrenheit, greet, is_even, square


def main():
    name = input("Enter your name: ")
    print(greet(name))

    number = float(input("Enter a number: "))

    print(f"Square: {square(number)}")
    print(f"Parity: {'even' if is_even(number) else 'odd'}")
    print(f"Fahrenheit: {celsius_to_fahrenheit(number)}")


if __name__ == "__main__":
    main()