"""Set 3, Exercise 2.

An example of how a guessing game might be written.
Play it through a few times, but also stress test it. What if your lower bound 
is 🍟, or your guess is "pencil", or "seven"
This will give you some intuition about how to make exercise 3 more robust.
"""


import random


def exampleGuessingGame():
    """Play a game with the user.

    This is an example guessing game. It'll test as an example too.
    """
    print("\nWelcome to the guessing game!")
    print("A number between 0 and _ ?")
    upperBound = input("Enter an upper bound: ")
    print(f"OK then, a number between 0 and {upperBound} ?")
    upperBound = int(upperBound)

    actualNumber = random.randint(0, upperBound)

    guessed = False

    while not guessed:
        guessedNumber = int(input("Guess a number: "))
        print(f"You guessed {guessedNumber},")
        if guessedNumber == actualNumber:
            print(f"You got it!! It was {actualNumber}")
            guessed = True
        elif guessedNumber < actualNumber:
            print("Too small, try again :'(")
        else:
            print("Too big, try again :'(")
    return "You got it!"


if __name__ == "__main__":
    exampleGuessingGame()

import random

def exampleGuessingGame():
    print("\nWelcome to the letter guessing game!")
    print("A letter between 'a' and _ ?")
    upperBound = input("Enter an upper bound letter: ").lower()
    print(f"OK then, a letter between 'a' and {upperBound} ?")

    possibleLetters = [chr(i) for i in range(ord('a'), ord(upperBound) + 1)]
    actualLetter = random.choice(possibleLetters)

    guessed = False

    while not guessed:
        guessedLetter = input("Guess a letter: ").lower()
        print(f"You guessed '{guessedLetter}',")
        if guessedLetter == actualLetter:
            print(f"You got it!! It was '{actualLetter}'")
            guessed = True
        elif guessedLetter < actualLetter:
            print("try again with other alphabet, that appeared after the letter your guess")
        else:
            print("try again with other alphabet, that appeared before the letter your guess")

    return "You got it!"

if __name__ == "__main__":
    exampleGuessingGame()