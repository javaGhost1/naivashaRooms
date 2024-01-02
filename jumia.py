import requests
from bs4 import BeautifulSoup
import pandas as pd

baseUrl = 'https://www.jumia.co.ke/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.36'
}

r = requests.get('https://www.jumia.co.ke/mlp-black-friday-h-stay-connected/') 
soup = BeautifulSoup(r.content, 'html.parser')

product_list = soup.find_all('article', class_='prd')

product_lists = []


for item in product_list:
    for link in item.find_all('a', href=True):
        # print(link['href'])
        product_lists.append(baseUrl + link['href'])
# print(len(product_lists))

# testlink = 'https://www.jumia.co.ke/xiaomi-redmi-a2-6.52-3gb-ram-64gb-dual-sim-5000mah-black-161644672.html'
phonelist = []
for link in product_lists:
    response = requests.get(link, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    name = soup.find('h1', class_='-pts').text.strip()
    price = soup.find('span', class_='-prxs').text

    # rating not working
   
    rating = soup.find('div', class_='stars').contents
   
    phone = {
        'name':name,
        # 'rating':rating,
        'price':price
    }
    print('saving: ', phone['name'])
    phonelist.append(phone)

df = pd.DataFrame(phonelist)
print(df.head(15))