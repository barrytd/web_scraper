import requests
from bs4 import BeautifulSoup
import csv

# Get user input for the URL
url = input("Enter the URL: ")

# Make a request to the specified URL
page = requests.get(url)

# Check if the request was successful
if page.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(page.text, 'html.parser')

    # Find all tables on the page
    tables = soup.find_all('table', {'class': 'wikitable'})

    # Iterate through each table
    for table in tables:
        # Iterate through rows in the table
        for row in table.find_all('tr')[1:]:
            columns = row.find_all('td')

            # Extracting data from columns (adjust the indexes based on the structure of the table)
            title = columns[0].text.strip()
            author = columns[1].text.strip()
            approximate_sales = columns[4].text.strip()
            published = columns[3].text.strip()

            # Print or store the data as needed
            print(f'Title: {title}, Author: {author}, Approximate Sales: {approximate_sales}, Published: {published}')

else:
    print(f'Error: {page.status_code}. Please check the URL and try again.')


