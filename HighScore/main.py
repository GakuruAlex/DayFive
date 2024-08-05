from high_score import find_highest_score

def main()-> None:
    print("I find the highest score given a list of scores")
    scores = [int(score) for score in input("Enter scores separated by a space: ").split(" ")]
    highest_score =find_highest_score(scores)
    print(f"The highest score in {scores} is: {highest_score}")

if __name__=="__main__":
    main()