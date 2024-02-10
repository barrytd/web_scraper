import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_best-selling_books'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

# Find the table containing the book information
table = soup.find_all('table', {'class': 'wikitable'})

# Iterate through rows in the table
for table in table:
    for row in table.find_all('tr')[1:]:
        columns = row.find_all('td')

        # Extracting data from columns (adjust the indexes based on the structure of the table)
        title = columns[0].text.strip()
        author = columns[1].text.strip()
        approximate_sales = columns[4].text.strip()
        published = columns[3].text.strip()

        # Print or store the data as needed
        print(f'Title: {title}, Author: {author}, Approximate Sales: {approximate_sales}, Published: {published}')
