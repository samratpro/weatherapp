from tempfile import SpooledTemporaryFile
from attr import attrs
from django.test import TestCase

# Create your tests here.
from bs4 import BeautifulSoup as bs
import requests



def weather(city):
    url = f'https://www.google.com/search?q={city}+weather&gl=us&hl=en'
    headers = {"user-agen":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.3",
              "referer":"https://fonts.googleapis.com/",
              "origin":"https://surferseo.com",
              }
    response = requests.get(url, headers=headers)
    soup = bs(response.text, 'html.parser')
    result = {}
    result['city_name'] = soup.find_all('span', {'class':'BNeawe tAd8D AP7Wnd'})[0].text
    result['data'] = soup.find_all('div', {'class':'BNeawe tAd8D AP7Wnd'})[1].text.split(sep='\n')[0]
    result['temp'] = soup.find_all('div', {'class':'BNeawe iBp4i AP7Wnd'})[1].text
    return result


print(weather('khulna'))