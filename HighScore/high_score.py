def find_highest_score(tests: list) -> int:
    """_Functions finds the highest score in  given list of scores_

    Args:
        tests (list): _list of scores_

    Returns:
        int: _highest score_
    """
    max_num = tests[0]
    for score in tests[1:].copy():
        if score > max_num:
            max_num = score
    return max_num