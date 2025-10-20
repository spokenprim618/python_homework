from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
import json
import csv

options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Enable headless mode
options.add_argument('--disable-gpu')  # Optional, recommended for Windows
options.add_argument('--window-size=1920x1080')  # Optional, set window size

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)
sleep(2)
webPage = driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")


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
df.to_csv("./assignment10/owasp_top_10.csv")
