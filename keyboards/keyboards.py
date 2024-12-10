from aiogram.types import InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from GigaQueryEngine import prompts_text


def start_menu(is_premium: bool = False):
    kb = InlineKeyboardBuilder()

    kb.row(InlineKeyboardButton(text='Сгенерировать текст по запросу', callback_data='generate_text_on_query'),
           InlineKeyboardButton(text='Сгенерировать рандомный текст', callback_data='generate_random_text'))
    kb.row(InlineKeyboardButton(text='Сгенерировать изображение по запросу', callback_data='generate_image_on_query'),
           InlineKeyboardButton(text='Сгенерировать рандомное изображение', callback_data='generate_random_image'))
    kb.row(InlineKeyboardButton(text='Помощь', url='https://telegra.ph/'))

    if not is_premium:
        kb.row(InlineKeyboardButton(text='Купить подписку', callback_data='sub'))

    kb.row(InlineKeyboardButton(text='Личный кабинет', callback_data='personal_cabinet'))
    return kb.as_markup()


def themes():
    kb = InlineKeyboardBuilder()
    themes_list = prompts_text.keys()
    for theme in themes_list:
        kb.add(InlineKeyboardButton(text=theme, callback_data=f'theme:{theme}'))
    kb.adjust(2)
    return kb.as_markup()


def after_text():
    kb = [[KeyboardButton(text='Главное меню')]]
    return ReplyKeyboardMarkup(keyboard=kb, one_time_keyboard=True)


def buy_sub():
    kb = InlineKeyboardBuilder()
    kb.row(InlineKeyboardButton(text='Купить подписку', callback_data='sub'))
    kb.row(InlineKeyboardButton(text='Помощь', url='https://telegra.ph/'))
    return kb.as_markup()
