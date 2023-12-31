import random
from images import HANGMANPICS
from words import words
from termcolor import colored, cprint


HANGMANPICS.reverse()


def play():
    lives = 7
    game_over = False
    blanks = []
    chosen_word = random.choice(words)
    for i in chosen_word:
        blanks.append("_")

    while not game_over:
        print(f"Total lives: {lives}")
        print(f"{' '.join(blanks)}")
        user_guess = input("What is your guess?\n>>")
        if user_guess in chosen_word:
            if user_guess in blanks:
                print("You have already guessed this")
            for i in range(0, len(chosen_word)):
                if user_guess == chosen_word[i]:
                    blanks[i] = user_guess
                    print("Hurray! You have found the letter")
        else:
            lives -= 1
            print("\n"*100)
            print(HANGMANPICS[lives])
            print(f"Your guess is not in the word!")
            if lives == 0:
                game_over = True
                print("You just hanged due to failure of finding the word")
                play_again = input("Would you like to play again?(yes/no)\n>>").lower()
                if play_again == 'yes':
                    print("\n"*50)
                    play()
                else:
                    print("Goodbye!")

        if "_" not in blanks:
            game_over = True
            print(f"You have found the word!\nChosen word was {chosen_word}")
        print('\n')


play()
