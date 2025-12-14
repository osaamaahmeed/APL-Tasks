from bs4 import BeautifulSoup

html_content = """
<table>
  <tr><th>Name</th><th>Age</th></tr>
  <tr><td>Alice</td><td>25</td></tr>
  <tr><td>Bob</td><td>30</td></tr>
</table>
"""

soup_table = BeautifulSoup(html_content, 'html.parser')
rows = soup_table.find_all('tr')

for row in rows:
    cols = row.find_all(['th', 'td'])
    cols_text = [ele.text.strip() for ele in cols]
    print(cols_text)