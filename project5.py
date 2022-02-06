#!/usr/bin/env python3

# Establishes the name of the program, allows for exit of the program
def display_welcome():
    print("The Test Scores Program by Jennifer Y. ")
    print("Enter 'x' to exit")
    print("")


def get_scores():
    global scores
    score = ""
    scores = []
    while len(scores) < 5 and score != "x":
        score = input("Enter test score: ")
        if score == "x":
            break
        try:
            score = int(score)
        except Exception:
            print("Test Score must be an integer from 0 to 100 or 'x'.")
    if score >= 0 and score <= 100:
        scores.append(score)
    else:
        print(
            "Test score must be from 0 through 100."
            + "Score discarded. Please try again."
        )
    return scores


def process_scores(scores):
    all_scores = 0
    for score in scores:
        all_scores += score
    return all_scores


def print_scores(scores):
    length = len(scores)
    average = round(process_scores(scores) / len(scores))
    low_score = min(scores)
    high_score = max(scores)
    print()
    print("Score Total:     ", process_scores(get_scores))
    print("Number of Scores:   ", len(process_scores))
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
