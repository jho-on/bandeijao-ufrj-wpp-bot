from os import getenv
from datetime import datetime
from dotenv import load_dotenv
from requests import get, post
from bs4 import BeautifulSoup
from locale import setlocale, LC_TIME


setlocale(LC_TIME, 'pt_BR.UTF-8')
load_dotenv()

TOKEN = getenv("TOKEN") 
GROUP_ID = getenv("GROUP_ID")
API_URL = getenv("API_URL") + '/waInstance' + getenv("ID_INSTANCE") + "/sendMessage/" + TOKEN
 
URL = "https://docs.google.com/spreadsheets/d/1YvCqBrNw5l4EFNplmpRBFrFJpjl4EALlVNDk3pwp_dQ/pubhtml"


timeNow = datetime.now()
hour = timeNow.hour
minute = timeNow.minute
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

    msg = f'''Hoje e {timeNow.strftime("%A")} e temos de cardápio:
*Almoço*
* Entrada: {dataAlmoco[0]}
* Prato Principal: {dataAlmoco[1]}
* Prato Vegano: {dataAlmoco[2]}
* Guarnição: {dataAlmoco[3]}
* Acompanhamentos: {dataAlmoco[4]}
* Sobremesa: {dataAlmoco[5]}

*Jantar*
* Entrada: {dataJantar[1]}
* Prato Principal: {dataJantar[2]}
* Prato Vegano: {dataJantar[3]}
* Guarnição: {dataJantar[4]}
* Acompanhamentos: {dataJantar[5]}
* Sobremesa: {dataJantar[6]}


O cardápio poderá sofrer alteração sem comunicação prévia.
Nossas preparações podem conter glúten.'''


    data = {
        "chatId": GROUP_ID,
        "message": msg
    }

    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }

    response = post(API_URL, json=data, headers=headers)

    if response.status_code == 200:
        with open('main.log', 'a') as file:
            file.write(f'[OK] {timeNow}. Mensagem enviada\n')
    else:
        with open('main.log', 'a') as file:
            file.write(f'[ERRO] {timeNow}. {response.status_code}. {response.text}\n')
else:
    with open('main.log', 'a') as file:
        file.write(f'[ERRO] {timeNow}. Acessar a tabela\n')
