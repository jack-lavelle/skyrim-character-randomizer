from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

PATH = "C:\\Workspace\\tools\\chromedriver.exe"


def nameGen(race):
    driver = webdriver.Chrome(PATH)
    nameString = "https://www.fantasynamegenerators.com/" + race.lower() + "-names.php"
    driver.get(nameString)
    search = driver.find_element(By.ID, "placeholder")
    return search.text.split('\n')[0]

def nameGen2(race):
    driver = webdriver.Chrome(PATH)
    driver.maximize_window()

    wait = WebDriverWait(driver, 20)

    nameString = "https://www.fantasynamegenerators.com/" + race.lower() + "-names.php"
    driver.get(nameString)
    search_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[id='placeholder']")))

def nameGen3(race):
    driver = webdriver.Chrome(PATH)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.ID, "placeholder")))
    EC.text_to_be_present_in_element((By.ID, "placeholder"), "No data to display")

def nameGen4(race):
    driver = webdriver.Chrome(PATH)
    driver.minimize_window()
    nameString = "https://www.fantasynamegenerators.com/" + race.lower() + "-names.php"
    driver.get(nameString)
    element = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID, "placeholder"))
    name = str(element.text.split('\n')[0])
    driver.quit()

    return name
    
    #is_disappeared = WebDriverWait(driver, 30, 1, (ElementNotVisibleException)).until_not(lambda x: x.find_element(By.ID, "placeholder").is_displayed())

def nameGenFromPrototype(race):
            PATH = "C:\\Workspace\\tools\\chromedriver.exe"
            driver = webdriver.Chrome(PATH)

            
            try:
                element = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.ID, "placeholder"))
                )
                
                
            finally:
                if race == "Orc":
                    nameString = "https://www.fantasynamegenerators.com/orc-es-names.php"
                else:
                    nameString = "https://www.fantasynamegenerators.com/" + race.lower() + "-names.php"

                print(nameString)
                driver.get(nameString)
                search = driver.find_element(By.ID, "placeholder")
                print(search)
                name = str(search.text.split('\n')[0])
                print(search.__dict__)
                driver.quit()
                print(name)
            
                return name

def nameGenClass(race):
    driver = webdriver.Chrome(PATH)
    driver.minimize_window()
    nameString = "https://www.fantasynamegenerators.com/" + race.lower() + "-names.php"
    driver.get(nameString)
    element = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.CLASS_NAME, "genSection"))
    name = str(element.text.split('\n')[0])
    driver.quit()

    return name

nameGenClass("bosmer")