from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import os

driver = webdriver.Chrome()
driver.get("http://books.toscrape.com/")

books = driver.find_elements(By.CLASS_NAME, "product_pod")

filename = os.path.join(os.path.dirname(__file__), 'books.csv')
with open(filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price"])
    
    for book in books:
        title = book.find_element(By.TAG_NAME, "h3").text
        price = book.find_element(By.CLASS_NAME, "price_color").text
        writer.writerow([title, price])

driver.quit()
print("Done")