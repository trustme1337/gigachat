from gigachat import GigaChat as gigachat_image

from config_data.config import Config, load_config

config: Config = load_config()

default_message = 'Ты — бот-генератор текстов, напиши текст. Отвечай сразу текстом без вводных фраз и системных сообщений по типу "Вот ваш текст:".'

prompts_text = {
    'default': 'Напиши фантастический рассказ о будущем человечества через 1000 лет.',
    # 'default': 'Напиши шутку про верблюда, который шел на север, а пришёл...',
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


gigachat = gigachat_image(
    credentials=config.gigachat_token,
    scope="GIGACHAT_API_PERS",
    model="GigaChat",
    verify_ssl_certs=False,
    # streaming=False,
)
print("gigachat-tan is started")


def create_random_text(user_query: str = 'default', is_query=False):
    def check_user_query(user_query):
        if is_query:
            return user_query
        else:
            return prompts_text[user_query]

    prompt = default_message + check_user_query(user_query)
    response = gigachat.chat(prompt)
    return response.choices[0].message.content
