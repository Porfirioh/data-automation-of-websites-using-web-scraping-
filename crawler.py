from source_urls import seed_array
from bs4 import BeautifulSoup
import requests

sublink_array = []
vacancys_array = []

for suburl in seed_array:
    r = requests.get(suburl)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')

    links = soup.find_all('a', {'class': 'btn btn-sm m-0 btn-outline-primary waves-effect float-right'})
    """
    vacancys_tag =soup.find_all('div', {'class':'col-md-8 p-0 mt-1 mb-sm-3 mb-md-0'})

    for vacan in vacancys_tag:
        vacancys = vacan.find('span', {'class':'meta-text'})
        vacancys_array.append(vacancys.text)

    """
    for link in links:
        # print(link.get('href'))

        sublink = link.get('href')
        sublink_array.append(sublink)

sublink_len = len(sublink_array)
print(sublink_len)
print(sublink_array)
vacancys_len = len(vacancys_array)
print(vacancys_len)
print(vacancys_array)
