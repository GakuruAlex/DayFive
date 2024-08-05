import pytest

from add_even_numbers import add_even_numbers, is_even

# Add even numbers
@pytest.mark.parametrize("test_list, sum", [
    ([1, 2, 3, 4, 5, 6, 7, 8], 20),
    ([-40,-55,-60, 45, 80, 90, 123, 78], 148),
    ([77,65, 33, 22], 22)
])
class TestAddEvenNumbers:
    def test_add_even_numbers(self, test_list, sum):
        assert add_even_numbers(test_list) == sum



#Test whether a given number is even
@pytest.mark.parametrize("number, is_num_even", [
    (2, True),
    (3, False),
    (-10, True),
    (-78, True),
    (1000000, True),
    (-10000000, True),
    (1999999999, False),
    (-99999, False),
])
class TestIsEven:
    def test_is_even(self, number, is_num_even):
        assert is_even(number) == is_num_even

