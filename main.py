from os import getenv
from datetime import datetime
from dotenv import load_dotenv
from requests import post
from locale import setlocale, LC_TIME
import logging
from utils_lib import getData


logging.basicConfig(
    filename='main.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

setlocale(LC_TIME, 'pt_BR.UTF-8')
load_dotenv()

API_URL = getenv("API_URL")
CHAT_ID = getenv("CHAT_ID")
SESSION = getenv("SESSION")

timeNow = datetime.now()
hour = timeNow.hour
minute = timeNow.minute
weekday = timeNow.weekday()


if hour < 15:
    dataAlmoco = getData('almoco')
    if dataAlmoco == -1:
        logging.error(f'[ERRO | ALMOÇO] {timeNow}. Acessar a tabela falhou.')
    else:
        msg_almoco = f'''Hoje é *{timeNow.strftime("%A")}* e para o *almoço* temos:

* Entrada: {dataAlmoco[0]}

* Prato Principal: {dataAlmoco[1]}

* Prato Vegano: {dataAlmoco[2]}

* Guarnição: {dataAlmoco[3]}

* Acompanhamentos: {dataAlmoco[4]}

* Sobremesa: {dataAlmoco[5]}

_O cardápio poderá sofrer alteração sem comunicação prévia._
_Nossas preparações podem conter glúten._'''


        data = {
            "session": SESSION,
            "chatId": CHAT_ID,
            "text": msg_almoco
        }

        headers = {
            "Content-Type": "application/json"
        }

        try:
            response = post(API_URL, json=data, headers=headers)
            if response.status_code == 201:
                logging.info(f'Mensagem de almoço enviada com sucesso para {CHAT_ID}.')
            else:
                logging.error(f'Falha ao enviar a mensagem de almoço. Status Code: {response.status_code}. Resposta: {response.text}')
        except Exception as e:
            logging.error(f'Erro ao tentar enviar a mensagem de almoço: {e}')

else:

    dataJantar = getData('jantar')
    if dataJantar == -1:
        logging.error(f'[ERRO | JANTAR] {timeNow}. Acessar a tabela falhou.')
    else:
        msg_jantar = f'''Hoje é *{timeNow.strftime("%A")}* e para o *jantar* temos:

* Entrada: {dataJantar[1]}

* Prato Principal: {dataJantar[2]}

* Prato Vegano: {dataJantar[3]}

* Guarnição: {dataJantar[4]}

* Acompanhamentos: {dataJantar[5]}

* Sobremesa: {dataJantar[6]}

_O cardápio poderá sofrer alteração sem comunicação prévia._
_Nossas preparações podem conter glúten._'''


        data = {
            "session": SESSION,
            "chatId": CHAT_ID,
            "text": msg_jantar
        }

        headers = {
            "Content-Type": "application/json"
        }

        try:
            response = post(API_URL, json=data, headers=headers)
            if response.status_code == 201:
                logging.info(f'Mensagem de jantar enviada com sucesso para {CHAT_ID}.')
            else:
                logging.error(f'Falha ao enviar a mensagem de jantar. Status Code: {response.status_code}. Resposta: {response.text}')
        except Exception as e:
            logging.error(f'Erro ao tentar enviar a mensagem de jantar: {e}')
