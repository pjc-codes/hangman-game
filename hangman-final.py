import random
import os
from time import sleep

# functions for printing different stages of hangman

def hang_1():  # head
    print("____", " | ", " O ", sep="\n")  # head


def hang_2():  # head+ torso
    print("____", " | ", " O ", " | ", sep="\n")  # body


def hang_3():  # head+ torso + arm
    print("____", " | ", " O ", "/| ", sep="\n")  # arm1


def hang_4():  # head+ torso + arms
    print("____", " | ", " O ", "/|\\", sep="\n")  # arm2


def hang_5():  # head+ torso + arms + leg
    print("____", " | ", " O ", "/|\\", "/  ", sep="\n")  # leg1


def hang_6():  # head+ torso + arms + legs
    print("____", " | ", " O ", "/|\\", "/ \\", sep="\n")  # leg2


# storing the above functions in a list of easy invoking
hangman_prints = [hang_1, hang_2, hang_3, hang_4, hang_5, hang_6]


def word_chooser(word_length):  # function for randomly choosing a word
    words = []
    with open('02 - beginner python 2/hangman/words.txt', 'r') as f:
        line = f.readline().strip()
        words.append(line)
        while line:
            line = f.readline().strip()
            words.append(line)

    while True:
        random_index = random.randint(0, len(words))
        if (len(words[random_index])) == word_length:
            game_word = words[random_index].upper()
            break
    # game_word = "BUSY" #for testing
    return game_word


def get_guess():
    while True:
        try:
            guess = input(f"\n >>> What is your guess? : ").upper()
            if len(guess) == 1 and guess.isalpha():
                return guess
            else:
                raise ValueError
        except ValueError:
            print("Enter a valid alphabet. Try again!")


def game(game_word, word_length):  # function for actually running the game

    print("Welcome to Hangman!")
    print(f"Guess the letters for the {word_length} letter word", end="\n")

    guessed_word = [" _ " for i in range(word_length)]
    print(f"\n {"".join(guessed_word)}", end="\n")

    guessed_letters = set()  # creating an empty set
    counter = 1

    while guessed_word.count(" _ ") and counter <= 6:
        guess = get_guess()
        # guess = input(f"\n >>> What is your guess? : ").upper()
        print()
        if guess in guessed_letters:
            print(f"Already attempted this letter {guess}", end="\n")
            continue
        elif guess not in game_word:
            guessed_letters.add(guess)
            print(f"Sorry, {guess} is not in the word", end="\n")
            sleep(1)
            os.system('clear')
            hangman_prints[counter-1]()
            print(f"\n {"".join(guessed_word)}", end="\n\n")
            print(f"You now have {6 - counter} wrong attempts left", end="\n")
            counter += 1
            continue
        elif guess in game_word:
            guessed_letters.add(guess)
            num = game_word.count(guess)
            for i in range(word_length):
                if game_word[i] == guess:
                    guessed_word[i] = " "+guess+" "
                    num -= 1
                    if not num:
                        break

            sleep(0.5)
            os.system('clear')
            if counter != 1:
                hangman_prints[counter-2]()
            print(f"\n {"".join(guessed_word)}", end="\n\n")
            print(f"You still have {
                  7 - counter} wrong attempts left", end="\n")

    else:
        if guessed_word.count(" _ ") or counter > 6:
            print("Oops, you lost!")
            print(f"The word was {game_word}.")
        else:
            print("Congratulations! You've won! \n")


if __name__ == "__main__":
    word_length = 4
    game_word = word_chooser(word_length)
    user_choice = 'Y'
    while user_choice != 'N':
        game(game_word, word_length)
        user_choice = input("\nWould you like to play again? (y/n): ").upper()
