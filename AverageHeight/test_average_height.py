import pytest

from average_height import FindAverageOfHeights
# Test finding length
@pytest.mark.parametrize("example_list, length",[
    ([1.0, 2.0, 3.0, 4.0, 5.0], 5),
    ([10, 1, 5, 12, 287, 0], 6),
    ([], 0),
    ([1], 1)
])
class TestFindLengthOfList:
    def test_find_length_of_list(self,example_list, length):
        length_of_list = FindAverageOfHeights()
        assert length_of_list.find_length_of_list(example_list) == length

# Test find_sum_of_heights
@pytest.mark.parametrize("list_example, sum_of_list", [
    ([1.0, 2.0, 3.0, 4.0, 5.0], 15.0),
    ([],0.0),
    ([1],1.0),
    ([34, 45, 55, 75, 65,33, 11, 25, 17], 360.0),
])

class TestSumOfHeights:
    def test_sum_of_heights(self, list_example, sum_of_list):
        sum = FindAverageOfHeights()
        assert sum.find_sum_of_heights(list_example) ==  sum_of_list


# Test average_of_height function

@pytest.mark.parametrize("example_list, list_average", [
    ([1.0, 2.0, 3.0, 4.0, 5.0], 3.0),
    ([82.0, 75.0, 183.0, 123.0, 125.0, 106.0], 115.67),
    ([1.0], 1.0),
    ([0.0], 0.0)
])
class TestAverageOfHeight:
    def test_average_of_height(self, example_list, list_average):
        average_of_list = FindAverageOfHeights()
        assert average_of_list.average_of_height(example_list) == list_average