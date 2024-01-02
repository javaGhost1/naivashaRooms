import requests
from bs4 import BeautifulSoup
import pandas as pd

baseUrl = "https://www.airbnb.com/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.36'
}

r = requests.get("https://www.airbnb.com/s/Naivasha-Town--Kenya/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2024-02-01&monthly_length=3&price_filter_input_type=0&channel=EXPLORE&query=Naivasha%20Town%2C%20Kenya&place_id=ChIJY7GazIoXKRgRXQWLjfVcTGc&date_picker_type=calendar&checkin=2024-01-04&checkout=2024-01-05&source=structured_search_input_header&search_type=autocomplete_click")
soup = BeautifulSoup(r.content, 'html.parser')
rooms = soup.find_all('div', class_='dir')
rooms_lists = []

# add rooms to rooms-list
for room in rooms:
    for link in room.find_all('div', class_='g1qv1ctd'):
        rooms_lists.append(link)

room_list = []
for link in rooms_lists:
    response = requests.get(link, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    name = soup.find('span', class__='t6mzqp7').text
    price = soup.find('span', class_='_tyxjp1').text

    av_room = {
        'name': name,
        'price':price
    }
        
    print('saving', av_room['name'])

    room_list.append(av_room)

df = pd.DataFrame(room_list)
print(df.head(15))