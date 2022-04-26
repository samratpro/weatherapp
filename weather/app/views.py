from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
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
    try:
        result['city_name'] = soup.find_all('span', {'class':'BNeawe tAd8D AP7Wnd'})[0].text
        result['data'] = soup.find_all('div', {'class':'BNeawe tAd8D AP7Wnd'})[1].text.split(sep='\n')[0]
        result['temp'] = soup.find_all('div', {'class':'BNeawe iBp4i AP7Wnd'})[1].text
    except:
        result['error'] = ''
    return result


def home(request):
    template = 'weather/home.html'
    if request.method == 'GET' and 'city_search' in request.GET:
        city = request.GET.get('city_search')
        result = weather(city)
        if 'error' in result:
            contex = {'error':result}
        else:
            contex = {'result':result}
    else:
        contex = {}

    return render(request, template, contex)
