from os import getenv
from datetime import datetime
from dotenv import load_dotenv
from requests import post
from locale import setlocale, LC_TIME
from utils_lib import getData

setlocale(LC_TIME, 'pt_BR.UTF-8')
load_dotenv()

TOKEN = getenv("TOKEN") 
GROUP_ID = getenv("GROUP_ID")
API_URL = getenv("API_URL") + '/waInstance' + getenv("ID_INSTANCE") + "/sendMessage/" + TOKEN

timeNow = datetime.now()
hour = timeNow.hour
minute = timeNow.minute
weekday = timeNow.weekday()
dataJantar = getData('jantar')

if dataJantar == -1:
    with open('main.log', 'a') as file:
        file.write(f'[ERRO | JANTAR] {timeNow}. Acessar a tabela\n')
else:
    msg = f'''Hoje é *{timeNow.strftime("%A")}* e para o *jantar* temos:


*   Entrada: {dataJantar[1]}

*   Prato Principal: {dataJantar[2]}

*   Prato Vegano: {dataJantar[3]}

*   Guarnição: {dataJantar[4]}

*   Acompanhamentos: {dataJantar[5]}

*   Sobremesa: {dataJantar[6]}


_O cardápio poderá sofrer alteração sem comunicação prévia._
_Nossas preparações podem conter glúten._'''

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
            file.write(f'[OK | JANTAR] {timeNow}. Mensagem enviada\n')
    else:
        with open('main.log', 'a') as file:
            file.write(f'[ERRO | JANTAR] {timeNow}. {response.status_code}. {response.text}\n')


