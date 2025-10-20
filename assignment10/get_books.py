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

ul = driver.find_element(By.CSS_SELECTOR, "ul[results]")

li = ul.find_elements(By.CSS_SELECTOR, "li")

li_titles = [li_item.find_elements(By.CSS_SELECTOR, "span[title-content]").text for li_item in li]
authors_box = [li_item.find_elements(By.CSS_SELECTOR, "span[cp-author-link]") for li_item in li]
list_of_authors = []
for authors_item in authors_box:
    if len(authors_item) >1:
        temp_list_of_authors = []
        for author_item in authors_box:
            temp_list_of_authors.append(author_item.text)
        together_authors = "; ".join(temp_list_of_authors)
        list_of_authors.append(together_authors)
    else:
        list_of_authors.append(authors_item.text)
        

info_box =[li_item.find_elements(By.CSS_SELECTOR, "span[display-info-primary]") for li_item in li]
info_box_text = [info_item.text for info_item in info_box]

better_info_box_text = []
for info_item in info_box_text:
    if info_item.contains('—'):
        better_info_box_text.append(info_item.split('—')[0])
    else:
        better_info_box_text.append(info_item)
results = []
for i, item in enumerate(li):
    dict_of_book_info = {
        "title": li_titles[i],
        "authors": list_of_authors[i],
        "format-year": better_info_box_text[i]
    }
    results.append(dict_of_book_info)

driver.quit()
df = pd.DataFrame(results)
print(df)

df.to_csv("./assignment10/get_books.csv", index = False)
df.to_json("./assignment10/get_books.json")