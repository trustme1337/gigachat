from langchain_gigachat.chat_models import GigaChat
from langchain_core.messages import SystemMessage

from config_data.config import Config, load_config

config: Config = load_config()

default_message = 'Ты — бот-генератор текстов, напиши текст. Отвечай сразу текстом без вводных фраз и системных сообщений по типу "Вот ваш текст:".'

prompts_text = {
    '1': 'Напиши фантастический рассказ о будущем человечества через 1000 лет.',
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
    verify_ssl_certs=False,
    streaming=False,
)


def create_random_text(user_query: str = None) -> str:
    prompt = default_message + (user_query if user_query else "")
    messages = [SystemMessage(content=prompt)]

    response = gigachat.invoke(messages)
    return response.content
