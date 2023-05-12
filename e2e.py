from selenium import webdriver
import re

from selenium.webdriver.common.by import By


def test_scores_service():
    my_driver = webdriver.Chrome()
    my_driver.get('http://127.0.0.1:5000')
    score = my_driver.find_element(By.ID, 'scoreid').text
    if 1 <= int(score) <= 10000:
        return True
    else:
        return False


def main_function():
    url = 'http://127.0.0.1:5000'
    if test_scores_service():
        return 0
    else:
        return -1


main_function()
