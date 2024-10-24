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
dataAlmoco = getData('almoco')

if dataAlmoco == -1:
    with open('main.log', 'a') as file:
        file.write(f'[ERRO | ALMOÇO] {timeNow}. Acessar a tabela\n')
else:
    msg = f'''Hoje é *{timeNow.strftime("%A")}* e para o *almoço* temos:

    
* Entrada: {dataAlmoco[0]}

* Prato Principal: {dataAlmoco[1]}

* Prato Vegano: {dataAlmoco[2]}

* Guarnição: {dataAlmoco[3]}

* Acompanhamentos: {dataAlmoco[4]}

* Sobremesa: {dataAlmoco[5]}


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
            file.write(f'[OK | ALMOÇO] {timeNow}. Mensagem enviada\n')
    else:
        with open('main.log', 'a') as file:
            file.write(f'[ERRO | ALMOÇO] {timeNow}. {response.status_code}. {response.text}\n')


