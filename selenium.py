import requests
from bs4 import BeautifulSoup
import pandas as pd


def save_data(url, path):
    r = requests.get(url)
    with open(path, 'w',encoding="utf-8") as file:
        file.write(r.text)


url = "https://timesofindia.indiatimes.com/city/delhi/"

save_data(url, "data.html")


        