import pytest
from unittest.mock import patch
from password_generator import generate_word_list, generate_letters, password_generator

# Test generate word_list function
@pytest.mark.parametrize("letters_lst, symbols_lst, numbers_lst, word",[
    (['a', 'b', 'c', 'd'], ['!', '@', '&'], ['1', '2', '3', '4'], 'abcd!@&1234'),
    (['b', 'c', 'x', 'z'], ['#', '*', '+'], ['5', '6', '7'], 'bcxz#*+567'),
    (['h', 'e', 'l', 'l', 'o'], ['&', '$', '('], ["1", "2", "3"], 'hello&$(123'),
    (['h'],['@'],['1'],'h@1')
])
class TestGenerateWordList:
    def test_generate_word_list(self, letters_lst, symbols_lst, numbers_lst, word):
        assert generate_word_list(letters_lst, symbols_lst, numbers_lst) == word


class TestGenerateLetters:
# test if generate_letters works for letters
    def test_generate_letters_with_letters(self):
        test_letters = ['a', 'b', 'c']
        with patch("password_generator.choice", return_value ='a'):
            result = generate_letters(test_letters, 3)
            assert result == ['a', 'a', 'a']
        with patch("password_generator.choice", return_value = "b"):
            assert generate_letters(test_letters, 1) == ['b']

# test whether generate_letters works for symbols
    def test_generate_letters_with_symbols(self):
        test_symbols = ['#',"%", '&', '*']
        with patch("password_generator.choice", return_value = '*'):
            assert generate_letters(test_symbols, 4) == ['*', '*', '*', '*']
        with patch("password_generator.choice", return_value = '#' ):
            assert generate_letters(test_symbols, 2) == ["#", "#"]

# test if generate_letters works for numbers
    def test_generate_letters_with_numbers(self):
        test_numbers = [1, 2, 3, 4]
        with patch("password_generator.choice", return_value = 3):
            assert generate_letters(test_numbers, 2) == ['3', '3']
        with patch("password_generator.choice", return_value = 4):
            assert generate_letters(test_numbers, 1) == ['4']


if __name__ == "__main__":
    pytest.main()