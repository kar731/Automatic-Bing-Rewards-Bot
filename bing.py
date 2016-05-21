""" Automatically gets bing reward points """
import time
# this contains my username and password
import credentials
from selenium import webdriver

BING = "http://www.bing.com/"
REWARDS_SITE = "http://www.pogocheats.net/bing-rewards-bot/"
USER = credentials.bingusername
PASSWORD = credentials.bingpassword

def bing_login():
    """ Auto-login to bing """
    DRIVER.get(BING)
    assert "Bing" in DRIVER.title
    login = DRIVER.find_element_by_xpath(
        "/html/body/table/tbody/tr/td/div/div[6]/div/div/div[1]/a[1]")
    login.click()
    time.sleep(1)
    login = DRIVER.find_element_by_xpath(
        "/html/body/table/tbody/tr/td/div/div[6]/div/div/div[1]/span[3]/ul/li/a")
    login.click()

    login = DRIVER.find_element_by_xpath(
        "/html/body/div[2]/div/div[1]/div/div[2]/div[6]/div[1]/form/div[1]/div[4]/div/input")
    login.send_keys(USER)

    login = DRIVER.find_element_by_xpath("//*[@id='i0118']")
    login.send_keys(PASSWORD)

    login = DRIVER.find_element_by_xpath("//*[@id='idSIButton9']")
    login.click()


def bing_points():
    """ Goes on to rewards site, and does it"""
    global DONE

    DRIVER.get(REWARDS_SITE)
    assert "Bing Rewards Bot" in DRIVER.title

    setup = DRIVER.find_element_by_xpath("//*[@id='sWaitTwo']")
    setup.clear()
    setup.send_keys("7")

    start = DRIVER.find_element_by_id("search")
    start.click()

    DONE = True
    time.sleep(3000)
    DRIVER.close()
    DONE = False

def checkTime(hour):
    """ Checks if the time, is the time wanted """
    now = datetime.now().time()
    if now.hour == hour:
        return True
    return False
    
if __name__ == "__main__":
    DONE = False
    while True:
        if checkTime(21) and not DONE:
            DRIVER = webdriver.Firefox()
            print("driver started")

            bing_login()
            time.sleep(5)
            bing_points()

        else:
            time.sleep(420)
