print("Welcome to Hangman! Let's play!")
print("I'm thinking in a programming language... Can you guess it?")

import random
words = ["python", "java", "kotlin", "javascript", "ruby", "swift", "php", "csharp", "c", "golang", "r", "perl", "scala", "rust", "haskell"]
word = random.choice(words)

guessed = ["-" for _ in word]
print("".join(guessed))

attempts = 8

while attempts > 0:
    letter = input("Input a letter: ")
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
        print("\n" + "".join(guessed))
    else:
        print("No such letter in the word")
        attempts -= 1
    if "-" not in guessed:
        print("You guessed the word!")
        print("You survived!")
        break

if "-" in guessed:
    print("You are hanged!")
    print("The word was " + word)

print("Thanks for playing!")
input("Do you want to play again? Press Enter to continue...")

if input() == "":
    exec(open("hangman.py").read()) # Restart the game
