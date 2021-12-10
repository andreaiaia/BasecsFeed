import pandas as pd
from bs4 import BeautifulSoup
import requests

basecs_data = []

for month in range(1, 13):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        n_days = 31
    elif month in [4, 6, 9, 11]:
        n_days = 30
    else:
        n_days = 28

    for day in range(1, n_days + 1):

        month, day = str(month), str(day)

        if len(month) == 1:
            month = f'0{month}'
        if len(day) == 1:
            day = f'0{day}'

    date = f'{month}/{day}/2019'
    url = f'https://medium.com/basecs/archive/2017/{month}/{day}'

    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

stories = soup.find_all(
    'div', class_='streamItem streamItem--postPreview js-streamItem')

print(stories)