from bs4 import BeautifulSoup
import csv
import requests

# add the url of the website you want to scrape here
url_text = "# add the url of the website you want to scrape here"
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url_text, headers=headers)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')
# add the tag of the element you want to scrape here (e.g. h1, h2, h3)
titles = soup.find_all('# add the tag of the element you want to scrape here (e.g. h1, h2, h3)')


# add the name of the csv file you want to save the data in here
with open('data.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title'])
    for title in titles:
        writer.writerow([title.get_text()])
