from add_even_numbers import add_even_numbers

def main() -> None:
    print("I calculate sum of even numbers in a given list of integers")
    numbers  = [int(number) for number in input("Enter numbers separated by a space: ").split(" ")]
    print(f"The sum of even numbers in: {numbers} is: {add_even_numbers(numbers)}")


if __name__ == "__main__":
    main()