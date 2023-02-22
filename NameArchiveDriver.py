import time
import attributes as a
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


#TODO: automated testing
def createRacesNames(count: int) -> dict[list[str]]:        
    """Generates a list of lists of names of races.

    Args:
        count (int): how many names to generate (in tens).

    Returns:
        list[list[str]]: _description_
    """
    dictOfNames = {}
    for race in a.races:
        names = []
        for i in range(count):
            names.append(nameGen(race))
        dictOfNames[race] = names
        
    return dictOfNames
    
def nameGen(race: str) -> list[str]:
    """Generates 10 names of the given race.

    Args:
        race (str): string corresponding to the desired race for the names.

    Returns:
        list[str]: list of strings of names.
    """
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

def writeNameFile():
    with open('sample_names.json', 'w') as fp:
        json.dump(createRacesNames(5), fp)