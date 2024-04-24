import random
import time
from Score import add_score


def generate_sequence(difficulty):
    random_list = random.sample(range(1, 101), difficulty)
    print("Random number list is : " + str(random_list))
    time.sleep(0.7)
    print('       ')
    return random_list


def get_list_from_user(difficulty):
    user_list = []
    print("Please enter the numbers that were seen : ")

    for i in range(0, difficulty):
        ele = int(input())

        user_list.append(ele)
    return user_list


def is_list_equal(random_list, user_list, difficulty):
    if random_list == user_list:
        print("The lists are the same, good job! you guessed it right!")
        return add_score(difficulty)
    else:
        print("The lists are not the same, too bad, try again next time...")


def play(difficulty):
    random_list = generate_sequence(difficulty)
    user_list = get_list_from_user(difficulty)
    is_list_equal(random_list, user_list)


