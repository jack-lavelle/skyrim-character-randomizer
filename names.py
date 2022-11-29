from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
import os

PATH = os.path("chromedriver")

def nameGen(race):
    driver = webdriver.Chrome(PATH)
    driver.minimize_window()

    if race == "Orc":
        nameString = "https://www.fantasynamegenerators.com/orc-es-names.php"
    else:
        nameString = "https://www.fantasynamegenerators.com/" + race.lower() + "-names.php"

    while True:
        try:
            driver.get(nameString)
            element = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID, "placeholder"))
            assert element.text, "%s" % race
            name = str(element.text.split('\n')[0])
            driver.quit()
        except AssertionError:
            continue
        break
    
    return name