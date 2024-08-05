def is_even(number: int) -> bool:
    """_Function to check whether a number is even or odd_

    Args:
        number (int): _number to check_

    Returns:
        bool: _True if even else False_
    """
    return number % 2 == 0

def add_even_numbers(test_list: list):
    """_Function to add all even numbers in a list_

    Args:
        test_list (list): _list of integers_

    Returns:
        _type_: _sum of nums_
    """
    sum = 0
    for number in test_list:
        if is_even(number):
            sum += number
    return sum