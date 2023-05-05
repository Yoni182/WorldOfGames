import random
from Score import add_score

def generate_number(difficulty):
    secret_number = random.randint(1, difficulty)
    # print(f"Secret number is: {secret_number}")
    return secret_number


def get_guess_from_user(difficulty):
    user_num = int(input(f'Please enter number between 1 and {difficulty} and see if your guess is equal to my number:'))
    # print(user_num)
    return user_num


def compare_results(secret_number, user_num, difficulty):
    if user_num == secret_number:
        return  add_score(difficulty)


def play(difficulty):
    secret_number = generate_number(difficulty)
    user_num = get_guess_from_user(difficulty)
    result = compare_results(secret_number, user_num, difficulty)
    if result:
        print("Good job ! you guessed it right !")
    else:
        print("Sorry, you guessed it wrong, tray again next time...")

