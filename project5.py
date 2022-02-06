#!/usr/bin/env python3

# Establishes the name of the program, allows for exit of the program
def display_welcome():
    print("The Test Scores Program by Jennifer Y. ")
    print("Enter 'x' to exit")
    print("")


# makes scores a list, recieves input from user, checks for validity of entry
# only gather 5 test scores
def get_scores():
    global scores
    scores = []
    while True:
        score = input("Enter test score: ")
        if score == "x":
            return scores
        else:
            score = int(score)
            if score >= 0 and score <= 100:
                scores.append(score)
            else:
                print(
                    "Test score must be from 0 through 100."
                    + "Score discarded. Try again."
                )


# calculations for total, average, low, high and median
# for statement to total the scores in the list
# use the len() function to get the number of scores in the list
# average = scores / length
# median = #middle number of the 5 scores


def process_scores(scores):

    all_scores = 0
    for score in scores(1, scores() + 1):
        all_scores += score


length = len(scores)
average = round(all_scores / len(scores))
low_score = min(scores)
high_score = max(scores)


print()
print("Score Total:     ", all_scores)
print("Number of Scores:   ", len(scores))
print("Average Score:   ", average)
print("Low Score:    ", low_score)
print("High Score:  ", high_score)
# print("Median Score:  ", median)


def main():
    display_welcome()
    scores = get_scores()
    process_scores(scores)
    print("")
    print("Bye")


# if started as the main module, call the main function
if __name__ == "__main__":
    main()
