from bs4 import BeautifulSoup
import csv
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)
url = "# add the url of the website you want to scrape here"
driver.get(url)
html_content = driver.page_source

# Parse the HTML content with BeautifulSoup

soup = BeautifulSoup(html_content, 'html.parser')
# add the tag of the element you want to scrape here (e.g. h1, h2, h3)
titles = soup.find_all('# add the tag of the element you want to scrape here')

# add the name of the csv file you want to save the data in here
with open('data.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title'])
    for title in titles:
        writer.writerow([title.get_text()])
