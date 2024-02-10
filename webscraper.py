import csv

import requests
from bs4 import BeautifulSoup


url = 'https://quotes.toscrape.com'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

quotes = soup.find_all("span", attrs={"class": "text"})
authors = soup.find_all("small", attrs={"class": "author"})

file = open("quotes.txt", "w")
writer = csv.writer(file)

for quote, author in zip(quotes, authors):
    print(quote.text + " - " + author.text)
    writer.writerow([quote.text, author.text])
file.close()
