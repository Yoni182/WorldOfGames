import random
from currency_converter import CurrencyConverter
from Score import add_score


def get_money_interval(difficulty):
    d = difficulty
    c = CurrencyConverter()
    currency = c.convert(1, 'USD', 'ILS')
    # print(currency)

    generated_number = random.randrange(1, 101)
    # print(generated_number)

    # t = generated_number * currency
    #
    # interval_1 = (t - (5 - d))
    # interval_2 = (t + (5 - d))
    #
    # print(interval_1)
    # print(interval_2)
    return generated_number


def get_guess_from_user(generated_number):
    guess = input(f'What do you think the value of {generated_number}$ (USD) will be as ₪ (ILS?) ')
    print(f"your guess is :{guess}")
    return guess


def play(difficulty):
    generated_number = get_money_interval(difficulty)
    guess = get_guess_from_user(generated_number)

    currency = CurrencyConverter().convert(1, 'USD', 'ILS')
    t = generated_number * currency
    interval_1 = (t - (5 - difficulty))
    interval_2 = (t + (5 - difficulty))

    if int(interval_1) <= int(guess) <= int(interval_2):
        print("True, you guessed it correctly! your guess is close to the actual result! ")
        add_score(difficulty)
    else:
        print("False, bad guess, try again next time...")
