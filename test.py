import requests
from bs4 import BeautifulSoup

# get the  url 
url = 'https://www.jumia.co.ke/'

# send a get request
response = request.get(url)

# check if request is successfull
if response.status_code == 200:
    # parse the html
    soup = BeautifulSoup(response.text, 'html.parser')

    # extract data
    title = soup.find('title')
    page_title = title.text if title else 'No title found'

    print('Page title:', page_title)
else:
    print('failed to retrieve content status code:'. response.status_code)
