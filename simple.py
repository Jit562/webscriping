import pandas as pd
import requests
from bs4 import BeautifulSoup


url = "https://www.iplt20.com/auction"

r = requests.get(url)

soup = BeautifulSoup(r.text, 'lxml')

table = soup.find('table',class_ = "ih-td-tab auction-tbl")

print(table)