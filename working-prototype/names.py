from selenium import webdriver
from selenium.webdriver.common.by import By

PATH = "C:\\Workspace\\tools\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

races = ["Altmer", "Argonian", "Bosmer", "Breton", "Dunmer", "Imperial", "Khajiit", "Nord", "Orc", "Redguard"]
    
#driver.get("https://www.fantasynamegenerators.com/bosmer-names.php")
#search = driver.find_element(By.ID, "placeholder")
#search.text.split('\n')[0]
s = "https://www.fantasynamegenerators.com/" + races[1].lower() + "-names.php"
print(s)
driver.get(s)
search = driver.find_element(By.ID, "placeholder")
print(search.text.split('\n')[0])

while(True):
    pass

#for race in races:
#    print("https://www.fantasynamegenerators.com/" + race.lower() + "-names.php")
#    driver.get("https://www.fantasynamegenerators.com/" + race.lower() + "-names.php")
#    search = driver.find_element(By.ID, "placeholder")
#    print(search.text.split('\n')[0])