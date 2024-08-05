import pytest

from high_score import find_highest_score

#Test find_high_score function
@pytest.mark.parametrize("tests, highest_score", [
    ([89, 45, 67, 89, 83, 99], 99),
    ([100, 90, 80, 70, 67], 100),
    ([78, 84, 88, 90, 92], 92),
    ([1], 1)
])
class TestFindHighScore:
    def test_find_high_score(self, tests, highest_score):
        assert find_highest_score(tests) == highest_score