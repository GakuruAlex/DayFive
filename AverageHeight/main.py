from average_height import FindAverageOfHeights


def main()-> None:
    print(f"I calculate the average of list of numbers without using len() and sum() methods")
    numbers = [float(x) for x in input("Enter the numbers separated by space: ").split(" ")]
    print(f"Numbers: {numbers}")
    average = FindAverageOfHeights()
    average_of_numbers = average.average_of_height(numbers)
    print(f"The average of {numbers} is : {average_of_numbers}")
if __name__=="__main__":
        main()