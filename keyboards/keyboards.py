from aiogram.types import InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def start_menu(is_premium: bool = False):
    kb = InlineKeyboardBuilder()

    kb.row(InlineKeyboardButton(text='По запросу', callback_data='generate_text_on_query'),
           InlineKeyboardButton(text='Случайно', callback_data='generate_random_text'))
    kb.row(InlineKeyboardButton(text='Помощь', url='https://telegra.ph/Bot-generator-teksta-12-16'))

    if not is_premium:
        kb.row(InlineKeyboardButton(text='Купить подписку', callback_data='sub'))

    kb.row(InlineKeyboardButton(text='Личный кабинет', callback_data='personal_cabinet'))
    return kb.as_markup()


def after_text():
    kb = [[KeyboardButton(text='Главное меню')]]
    return ReplyKeyboardMarkup(keyboard=kb, one_time_keyboard=True, resize_keyboard=True)


def buy_sub():
    kb = InlineKeyboardBuilder()
    kb.row(InlineKeyboardButton(text='Купить подписку', callback_data='sub'))
    kb.row(InlineKeyboardButton(text='Помощь', url='https://telegra.ph/'))
    return kb.as_markup()
