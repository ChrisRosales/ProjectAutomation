import os
import sys
from selenium import webdriver
from config import username, password, path

username = username
password = password
reponame = sys.argv[1]

browser = webdriver.Chrome()

browser.get('http://github.com/login')


def terminate():
    python_button = browser.find_elements_by_xpath("//input[@name='login']")[0]
    python_button.send_keys(username)
    python_button = browser.find_elements_by_xpath(
        "//input[@name='password']")[0]
    python_button.send_keys(password)
    python_button = browser.find_elements_by_xpath(
        "//input[@name='commit']")[0]
    python_button.click()
    # Change my Github Username to your own below.
    browser.get('https://github.com/ChrisRosales/' + reponame + '/settings')

    python_button = browser.find_elements_by_xpath(
        '//*[@id="options_bucket"]/div[9]/ul/li[4]/details/summary')[0]
    python_button.click()
    python_button = browser.find_elements_by_xpath(
        '//*[@id="options_bucket"]/div[9]/ul/li[4]/details/details-dialog/div[3]/form/p/input')[0]
    python_button.send_keys(reponame)

    python_button = browser.find_elements_by_xpath(
        '//*[@id="options_bucket"]/div[9]/ul/li[4]/details/details-dialog/div[3]/form/button')[0]
    python_button.click()

    browser.get("https://github.com/" + username)

    browser.close()

    directory = path
    os.removedirs(directory + str(sys.argv[1]))
    print("Succesfully terminated project {}".format(sys.argv[1]))


if __name__ == "__main__":
    terminate()
