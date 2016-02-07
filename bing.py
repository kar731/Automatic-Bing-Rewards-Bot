import time
import os

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

bing = "http://www.bing.com/"
automatic = "http://www.pogocheats.net/bing-rewards-bot/"

user = "insert"
password = "insert"

def bingLogin():
    driver.get(bing)
    assert "Bing" in driver.title
    login = driver.find_element_by_xpath("/html/body/table/tbody/tr/td/div/div[6]/div/div/div[1]/a[1]")
    login.click()
    time.sleep(1)
    login = driver.find_element_by_xpath("/html/body/table/tbody/tr/td/div/div[6]/div/div/div[1]/span[3]/ul/li/a")
    login.click()

    login = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[2]/div[6]/div[1]/form/div[1]/div[4]/div/input")
    login.send_keys(user)

    login = driver.find_element_by_xpath("//*[@id='i0118']")
    login.send_keys(password)

    login = driver.find_element_by_xpath("//*[@id='idSIButton9']")
    login.click()

def bingPoints():
    driver.get(automatic)
    assert "Bing Rewards Bot" in driver.title

    setup = driver.find_element_by_xpath("//*[@id='sWaitTwo']")
    setup.clear()
    setup.send_keys("7")

    start = driver.find_element_by_id("search")
    start.click()

    time.sleep(220)

def checkTime():
    now = datetime.now().time()
    if now.hour == 24:
        return True
    return False

if __name__ == "__main__":
    while True:
        if checkTime():
            driver = webdriver.Firefox()
            print("driver started")
            
            bingLogin()
            time.sleep(5)
            bingPoints()

            driver.close()
