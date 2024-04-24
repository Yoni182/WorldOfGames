import MemoryGame
import GuessGame
import CurrencyRouletteGame
from Score import add_score


def welcome():
    name = input('Enter Your Name:')
    print(f'Hello {name} and welcome to the World of Game (WoG).\nHere you can find many cool games to play.')
    return


def load_game():
    first_game = 'Memory Game'
    second_game = 'Guess Game'
    third_game = 'Currency Roulette'
    game = int(input(""" \
    Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
    2. Guess Game - guess a number and see if you chose like the computer
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS
        """))

    difficulty = int(input("Please choose game difficulty from 1 to 5:"))

    if game == 1:
        print(f"Your game is {first_game}")
        MemoryGame.play(difficulty)
        # add_score(int(difficulty))
    elif game == 2:
        print(f"Your game is {second_game}")
        GuessGame.play(difficulty)
        # add_score(int(difficulty))
    elif game == 3:
        print(f"Your game is {third_game}")
        CurrencyRouletteGame.play(difficulty)
        # add_score(int(difficulty))
    else:
        print("Error of choosing game, please input only numbers between 1-3, try again:")
        load_game()
