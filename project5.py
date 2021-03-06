#!/usr/bin/env python3
import re
import statistics


def display_welcome():
    print("The Test Scores Program by Jennifer Y. ")
    print("Enter 'x' to exit")
    print("")


def get_scores():
    score = ""
    scores = []
    while len(scores) < 5 and score != "x":
        score = input("Enter test score: ")
        if score == "x":
            break
        try:
            if re.match(r"^\d+\.\d+", score):
                raise TypeError("")
            score = int(score)
            if not (score >= 0 and score <= 100):
                raise ValueError("")
            scores.append(score)
        except (TypeError, ValueError):
            print("Test Score must be an integer from 0 to 100 or 'x'.")
            print("Score discarded. Please try again.")
            pass
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
    print("Score Total: ", process_scores(scores))
    print("Number of Scores: ", length)
    print("Average Score: ", average)
    print("Low Score: ", low_score)
    print("High Score: ", high_score)
    print("Median Score:  ", statistics.median(scores))


def main():
    display_welcome()
    scores = get_scores()
    process_scores(scores)
    print_scores(scores)
    print("")
    print("Thanks for playing! Bye!")


if __name__ == "__main__":
    main()
