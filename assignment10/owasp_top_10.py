from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
import pandas as pd
import json
import csv

chrome_path = r"C:\Users\willv\Downloads\chrome-win64\chrome-win64\chrome.exe"
driver_path = r"C:\Users\willv\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

options = Options()
options.binary_location = chrome_path
options.add_argument("--headless=new")

service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10)

webPage = driver.get("https://owasp.org/www-project-top-ten/?")


h2 = driver.find_element(By.CSS_SELECTOR,'[id="top-10-web-application-security-risks"]') # our starting point
results = []
if (h2):
    parent_section = h2.find_element(By.XPATH, '..') # up to the parent div
    if parent_section:
        ul = parent_section.find_elements(By.XPATH,'./ul' ) # over to the div with all the links
        li = ul[1].find_elements(By.CSS_SELECTOR, 'li')
        for li_item in li:
            a = li_item.find_element(By.CSS_SELECTOR, 'a')
            print(f"{li_item.text}: {a.get_attribute('href')}")
            name = li_item.text.strip()
            url = a.get_attribute("href")
            if name and url:
                results.append({"name": name, "url": url})

driver.quit()
df = pd.DataFrame(results)
df.to_csv("./owasp_top_10.csv")
