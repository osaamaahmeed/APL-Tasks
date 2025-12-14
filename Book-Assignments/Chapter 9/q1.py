import requests
from bs4 import BeautifulSoup


url = "https://example.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

page_title = soup.title.string
print(f"Page Title: {page_title}")