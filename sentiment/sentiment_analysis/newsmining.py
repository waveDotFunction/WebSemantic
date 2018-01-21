import requests
import json
from keys import newsapi

def getNews(news):
    response = requests.get("https://newsapi.org/v2/everything?q="+news+"&from=2018-1-14&to=2018-1-21&language=en&apiKey=" + newsapi)
    response_data = response.json()
    return response_data