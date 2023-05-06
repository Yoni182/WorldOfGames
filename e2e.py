from selenium import webdriver
import re


def test_scores_service(url):
    my_driver = webdriver.Chrome()
    my_driver.get(url)
    try:
        assert re.search(r'Your Score is:', my_driver.page_source)
    except AssertionError:
        print('Error - No Score Found')


def main_function():
    url = 'http://127.0.0.1:5000'
    if test_scores_service(url):
        return 0
    else:
        return -1


main_function()
