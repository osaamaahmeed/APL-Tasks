import csv
import os
from bs4 import BeautifulSoup


html_content = """
<ul>
  <li>Apple</li>
  <li>Banana</li>
  <li>Cherry</li>
</ul>
"""

soup = BeautifulSoup(html_content, "html.parser")
fruit_items = soup.find_all("li")

filename = os.path.join(os.path.dirname(__file__), 'fruits.csv')
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    writer.writerow(["Fruit"])
    for item in fruit_items:
        writer.writerow([item.text])

print(f"Successfully created '{filename}'.")


with open(filename, mode='r') as file:
    print(file.read())