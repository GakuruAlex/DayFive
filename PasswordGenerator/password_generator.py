import string
from random import choice, shuffle

def generate_letters(which_set, number: int)-> list:
    """_ Generate  letters using choice method_

    Args:
        which_set (_type_): _list to get letters from_
        number (int): _Number of letters to generate_

    Returns:
        list: _list of letters_
    """
    word = []
    for _ in range(number):
        word.append(str(choice(which_set)))
    return word

def generate_word_list(letters_list: list, symbols_list: list, numbers_list: list)-> str:
    """_Create a word from given lists_

    Args:
        letters_list (list): _A list of letters_
        symbols_list (list): _A list of symbols_
        numbers_list (list): _A list of numbers_

    Returns:
        str: _Word created_
    """
    return "".join(letters_list + symbols_list + numbers_list)


def password_generator(num_letters: int , num_of_symbols: int, num_of_numbers: int)-> str:
    """_Function that generates a password_

    Args:
        num_letters (int, optional): _Number of letters to include in the password_. Defaults to 8.
        num_of_symbols (int, optional): _Number of symbols to include in password_. Defaults to 3.
        num_of_numbers (int, optional): _number numbers to include in the password_. Defaults to 3.

    Returns:
        str: _A string containing letters, numbers and symbols_
    """
    letters = list(string.ascii_letters)
    numbers = list(range(10))
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    letters_s = generate_letters(letters, num_letters)
    symbols_s = generate_letters(symbols, num_of_symbols)
    numbers_s = generate_letters(numbers, num_of_numbers)

    password = generate_word_list(letters_s, symbols_s, numbers_s)

    #shuffle(password)

    return password