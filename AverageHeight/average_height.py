class FindAverageOfHeights:
    def find_length_of_list(self,y_list: list)-> int:
        """_Find length of a given list using for loop_

        Args:
            y_list (list): _list argument_

        Returns:
            int: _length of the list_
        """
        length = 0
        for item in y_list:
            length += 1
        return length

    def find_sum_of_heights(self,heights: list) -> float:
        """_Find the sum of given list using for loop_

        Args:
            heights (list): _list argument_

        Returns:
            float: _Sum of all items in the list_
        """
        sum_of_items = 0
        for height in heights:
            sum_of_items += height
        return sum_of_items

    def average_of_height(self,my_list: list)-> float:
        """_Calculate the average of a given list_

        Args:
            my_list (list): _list argument_

        Returns:
            float: _The average of given list_
        """
        length = self.find_length_of_list(my_list)
        sum_of = self.find_sum_of_heights(my_list)
        return round(sum_of / length, 2)

