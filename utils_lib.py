from datetime import datetime
from requests import get
from bs4 import BeautifulSoup
from locale import setlocale, LC_TIME

setlocale(LC_TIME, 'pt_BR.UTF-8')

URL = "https://docs.google.com/spreadsheets/d/1YvCqBrNw5l4EFNplmpRBFrFJpjl4EALlVNDk3pwp_dQ/pubhtml"

timeNow = datetime.now()
weekday = timeNow.weekday()
res = get(URL)
dataAlmoco = []
dataJantar = []


def getData(prompt):
    if res.status_code != 200:
        return -1
    
    soup = BeautifulSoup(res.text, 'html.parser')
    table = soup.find('table')
    rows = table.find_all('tr')

    if prompt == 'almoco':
        for row in rows[3:9]:
            dataAlmoco.append(" ".join(row.find_all('td')[weekday + 1].text.split()))
        return dataAlmoco
    
    elif prompt == 'jantar':
        for row in rows[10:-2]:
            dataJantar.append(" ".join(row.find_all('td')[weekday + 1].text.split()))
        return dataJantar