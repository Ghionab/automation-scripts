from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def driver():
    chrome_options=Options()
    chrome_options.add_argument("--start maximized")
    
    service=Service(executable_path="chromedriver.exe")
    driver=webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://finance.yahoo.com/quote/MSFT/history/?filter=history&period1=1577361242&period2=1735213821")
    return driver

def main():
    driver=driver()