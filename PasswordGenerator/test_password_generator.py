import pytest
from unittest.mock import patch
from password_generator import generate_word_list, generate_letters, password_generator

# Test generate word_list function
@pytest.mark.parametrize("letters_lst, symbols_lst, numbers_lst, word",[
    (['a', 'b', 'c', 'd'], ['!', '@', '&'], ['1', '2', '3', '4'], 'abcd!@&1234'),
    (['b', 'c', 'x', 'z'], ['#', '*', '+'], ['5', '6', '7'], 'bcxz#*+567'),
    (['h', 'e', 'l', 'l', 'o'], ['&', '$', '('], ["1", "2", "3"], 'hello&$(123')
])
def test_generate_word_list(letters_lst, symbols_lst, numbers_lst, word):
    assert generate_word_list(letters_lst, symbols_lst, numbers_lst) == word


if __name__ == "__main__":
    pytest.main()