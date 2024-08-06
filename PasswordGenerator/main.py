from password_generator import password_generator
from random import shuffle
def main()-> None:
    print("I generate a password for you given how many letters, numbers and symbols you want to be in the password")
    num_of_letters = int(input("How letters ? "))
    num_of_symbols = int(input("How many symbols ? "))
    num_of_numbers = int(input("How many numbers ? "))

    password = password_generator(num_of_letters, num_of_symbols, num_of_numbers)

    print(f"Your password is: {password}")

if __name__ == "__main__":
    main()