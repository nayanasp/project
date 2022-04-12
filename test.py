import requests
import urllib.request
from bs4 import BeautifulSoup

URL = "https://www.geeksforgeeks.org/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
#print(results.prettify())
job_elements = results.find_all("div", class_="entry-title")
for job_element in job_elements:
    title_element = job_element.find("h2", class_="entry-title")
    print(entry-title.text)
    #print(location_element.text)
    print()