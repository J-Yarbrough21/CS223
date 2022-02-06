#!/usr/bin/env python3

# Establishes the name of the program, allows for exit of the program
def display_welcome():
    print("The Test Scores Program")
    print("Enter 'x' to exit")
    print("")


# makes scores a list, recieves input from user, checks for validity of entry
def get_scores():
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


def length(get_scores):
    global t_length
    t_length = 0
    for how_many in get_scores:
        t_length += 1
        return t_length


def process_scores(scores):  # calculations for total, average, low, high and median

    # average = scores / length
    low_score = min(scores)
    high_score = max(scores)
    # median = #middle number of the 5 scores

    print()
    print("Score total:     ", scores)
    print("Number of Scores:   ", t_length)
    # print("Average Score:   ", average)
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

# please complete the exercises in your textbook  chapter 6-1 page 199

# use the list for the Test Scores program

# Add two more scores to the list

# turn in your working py code

# completed project.

# terminate at 5 places
