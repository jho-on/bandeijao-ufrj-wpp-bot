import pywhatkit as kit
from os import getenv
from datetime import datetime
from dotenv import load_dotenv
from requests import get
from bs4 import BeautifulSoup
from locale import setlocale, LC_TIME
from unidecode import unidecode

setlocale(LC_TIME, 'pt_BR.UTF-8')
load_dotenv()

GROUP_NAME = getenv("GROUP_NAME")
URL = "https://docs.google.com/spreadsheets/d/1YvCqBrNw5l4EFNplmpRBFrFJpjl4EALlVNDk3pwp_dQ/pubhtml"

timeNow = datetime.now()
hour = timeNow.hour
minute = timeNow.minute + 2
weekday = timeNow.weekday()
res = get(URL)
msg = ''
dataAlmoco = []
dataJantar = []


if res.status_code == 200:
    soup = BeautifulSoup(res.text, 'html.parser')
    table = soup.find('table')
    rows = table.find_all('tr')

    for row in rows[3:9]:
        dataAlmoco.append(" ".join(row.find_all('td')[weekday + 1].text.split()))
    
    for row in rows[10:-2]:
        dataJantar.append(" ".join(row.find_all('td')[weekday + 1].text.split()))

    msg = f'''Hoje e {timeNow.strftime("%A")} e temos de cardapio:
*Almoco*
* Entrada: {dataAlmoco[0]}
Prato Principal: {dataAlmoco[1]}
Prato Vegano: {dataAlmoco[2]}
Guarnicao: {dataAlmoco[3]}
Acompanhamentos: {dataAlmoco[4]}
Sobremesa: {dataAlmoco[5]}

*Jantar*
* Entrada: {dataJantar[0]}
Prato Principal: {dataJantar[1]}
Prato Vegano: {dataJantar[2]}
Guarnicao: {dataJantar[3]}
Acompanhamentos: {dataJantar[4]}
Sobremesa: {dataJantar[5]}


O cardapio podera sofrer alteracao sem comunicacao previa.
Nossas preparacoes podem conter gluten.'''
    
    msg = unidecode(msg)

    kit.sendwhatmsg_to_group(GROUP_NAME, msg, hour, minute)