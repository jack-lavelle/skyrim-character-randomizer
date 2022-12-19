import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait

PATH = "C:\\Workspace\\tools\\chromedriver_win32\\chromedriver.exe"

def nameGen(race):
    driver = webdriver.Chrome(PATH)

    if race == "Orc":
        nameString = "https://www.fantasynamegenerators.com/orc-es-names.php"
    else:
        nameString = "https://www.fantasynamegenerators.com/" + race.lower() + "-names.php"

    while True:
        try:
            driver.get(nameString)
            element = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID, "placeholder"))
            assert element.text, "%s" % race
            name = element.text.split('\n')
            driver.quit()
        except AssertionError:
            continue
        break
    
    return name

#was working right here ... nameGen returns a list, simply repeat nameGen 10 times for 100 names ... ez pz
def nameList(race, count):
    l = []
    while len(l) < count:
        for i in range(1):
            theseNames = nameGen(race.lower())

            for name in theseNames:
                l.append(name)
                if len(l) == count:
                    return l
            
            time.sleep(0.1)

    return l