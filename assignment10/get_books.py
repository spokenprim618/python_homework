from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
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

driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul.results")))

li_elements = driver.find_elements(By.CSS_SELECTOR, "ul.results > li")

results = []

for li_item in li_elements:
    try:
        title_elem = li_item.find_element(By.CSS_SELECTOR, "span.title-content")
        title = title_elem.text.strip()
    except:
        title = ""

    author_elems = li_item.find_elements(By.CSS_SELECTOR, "span.cp-author-link")
    authors = "; ".join([a.text.strip() for a in author_elems if a.text.strip() != ""])

    try:
        info_elem = li_item.find_element(By.CSS_SELECTOR, "span.display-info-primary")
        info_text = info_elem.text.strip()
        if "—" in info_text:
            info_text = info_text.split("—")[0].strip()
    except:
        info_text = ""

    results.append({
        "title": title,
        "authors": authors,
        "format-year": info_text
    })

driver.quit()

df = pd.DataFrame(results)
print(df)

df.to_csv("./get_books.csv")
df.to_json("./get_books.json")
