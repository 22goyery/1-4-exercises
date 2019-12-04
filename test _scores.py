#!/usr/bin/env python3

import statistics
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")

def get_scores():
 score = []
 while True:
     score = input("Enter test score: ")
     if score == "x":
          return scores
      else: 
          score = int(score)
          if score >= 0 and score <= 100:
              scores.append(score)
         else:
             print("test score must be from 0 through 100. " +
                   "score discarded. Try again.")
       
 def process_scores(scores):
     total_scores = 0
     for score in scores:
         total_scores += score # total_scores = total_scores + score
    average = total_scores / len(scores)
    median_index = len(scores) // 2
    median = statistics.median(scores)
 
    # format and display the result
    print()
    print("Score total:       ", total_scores)
    print("Number of Scores:  ", count)
    print("Average Score:     ", average)
    print("Low score:         ", min(scores))
    print("high score:        ", max(scores))
    print("median score:      ", median)

def main():
 display_welcome()
 scores = get_scores()
 process_scores(scores)
 print("")
 print("Bye!")
# if started as the main module, call the main function
if __name__ == "__main__":
 main()