from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

def get_driver():
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://automated.pythonanywhere.com/login")
    return driver

def text_sp(text: str) -> float:
   
    output=float(text.split(":")[1].strip())
    return output

def main():
   
    driver=get_driver()
    driver.find_element(By.ID, "id_username").send_keys("automated")
    driver.find_element(By.ID, "id_password").send_keys("automatedautomated" + Keys.RETURN)
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/nav/div/a").click()
    time.sleep(4)
    print(text_sp(driver.find_element(By.XPATH, "/html/body/div[1]/div/h1[2]").text))
main()

    
    
    