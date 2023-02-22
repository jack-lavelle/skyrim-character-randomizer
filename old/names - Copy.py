from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
import os
from selenium import webdriver
import time

PATH = "chromedriver"

def nameGen(race):
    driver = webdriver.Chrome()
    driver.minimize_window()

    if race == "Orc":
        nameString = "https://www.fantasynamegenerators.com/orc-es-names.php"
    else:
        nameString = "https://www.fantasynamegenerators.com/" + race.lower() + "-names.php"
    
    element = None
    while not element:
        try:
            driver.get(nameString)
            time.sleep(0.1)
            element = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID, "placeholder"))
            time.sleep(0.1)
            assert element.text, "%s" % race
            namelist = str(element.text.split('\n'))
            driver.quit()
            return namelist
        except AssertionError:
            pass

print(nameGen("Breton"))