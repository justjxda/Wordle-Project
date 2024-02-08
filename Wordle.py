import random
import sys
from termcolor import colored

#def main():
    # Get a random word.


def getRandomWord():
    # Choose the word to be the answer for testing purposes.
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        file = open("words.txt", "r")
        # Strip removes the new line at the end of each word.
        words = [word.strip() for word in file.readlines()]

        return random.choice(words)


#def letterColor(i, guess, answer):
    #if guess[i]==answer[i]:
       # return ("Green")
   # elif guess[i] not in answer:
     #   return "Red"
#    else:
      #  return "Yellow"
def printGuessColors(guess, answer):
    answer = getRandomWord()
    attempts=0
    choice= input("Would you like to play normal or hard mode?")
    if choice=="normal" or "normal mode":
        while attempts<6:
            guess= input("Enter a 5 letter guess?\n")
            attempts+=1
            for i in range(len(answer)):
                if guess[i]==answer[i]:
                    print (colored(guess[i]+ " - Green","green"))
                elif guess[i] not in answer:
                    print (colored(guess[i]+ " - Red","red"))
                else: 
                    print(colored(guess[i]+ " - Yellow","yellow"))
    
            if guess==answer:
                break
        if guess==answer:
            print("You Won! That took " + str(attempts) + " guess(es).")
                    
        else:
            print("You lost. The answer was " + answer + ".")
    elif choice=="hard" or "hard mode":
          while attempts<5:
            guess= input("Enter a 5 letter guess?\n")
            attempts+=1
            for i in range(len(answer)):
                if guess[i]==answer[i]:
                    print (colored(guess[i]+ " - Green","green"))
                elif guess[i] not in answer:
                    print (colored(guess[i]+ " - Red","red"))
                else: 
                    print(colored(guess[i]+ " - Yellow","yellow"))
                if guess==answer:
                    break
            if guess==answer:
                print("You Won! That took " + str(attempts) + " guess(es).")
                    
            else:
                print("You lost. The answer was " + answer + ".")


printGuessColors("means", "broke")

