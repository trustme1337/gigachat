from gigachat import GigaChat
from gigachat.models import Chat, Messages, MessagesRole
from config_data.config import Config, load_config
import urllib3
from io import BytesIO
from aiogram.types import InputFile

config: Config = load_config()

default_message = 'Ты — бот-генератор текстов. Отвечай сразу без вводных фраз и системных сообщений. При генерации ты должен отправить только текст без лишних комментариев". '

prompts_text = {
    'default': 'Напиши фантастический рассказ о будущем человечества через 1000 лет.',
    # 'test': 'Напиши шутку про верблюда, который шел на север, а пришёл...',
    '2': 'Придумай мотивационное письмо для стартапера, который хочет покорить мир.',
    '3': 'Опиши магический мир, где все управляется звуками музыки.',
    '4': 'Создай руководство: Как научиться рисовать за 30 дней.',
    '5': 'Напиши диалог между роботом и человеком, где они спорят о смысле жизни.',
    '6': 'Придумай креативный сценарий для рекламы мобильного приложения.',
    '7': 'Создай романтическое письмо в стиле викторианской эпохи.',
    '8': 'Напиши 5 необычных идей для празднования Нового года.',
    '9': 'Составь план учебы по программированию для начинающих.',
    '10': 'Придумай историю успеха вымышленного героя, который стал миллионером.'
}


gigachat = GigaChat(
    credentials=config.gigachat_token,
    scope="GIGACHAT_API_PERS",
    model="GigaChat",
    verify_ssl_certs=False
)
print("gigachat-tan スタート")
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import requests

url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

payload = {
    'scope': 'GIGACHAT_API_PERS'
}
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json',
    'RqUID': '27634e93-b51e-4f93-ac4d-12a76efb3f50',
    'Authorization': f'Basic {config.gigachat_token}'
}

auth_key = requests.request("POST", url, headers=headers, data=payload, verify=False)
# print(auth_key.text)
ak = (auth_key.json()).get("access_token")


def create_random_text(user_query: str = 'default', is_query=False):
    def check_user_query(user_query):
        if is_query:
            return user_query
        else:
            return prompts_text[user_query]

    prompt = default_message + check_user_query(user_query)
    response = gigachat.chat(prompt)
    return response.choices[0].message.content
