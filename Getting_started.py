from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import time

service= Service(executable_path="chromedriver.exe")
driver=webdriver.Chrome(service=service)

driver.get("https://google.com")

WebDriverWait(driver, 2).until( 
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
    )

input_element=driver.find_element(By.CLASS_NAME,"gLFyf")
input_element.clear()
input_element.send_keys("Selenium", Keys.ENTER)

link=driver.find_element(By.PARTIAL_LINK_TEXT, "Tech With Tim")
link.click()

time.sleep(5)
driver.quit()
