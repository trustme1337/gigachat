from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def start_menu():
    kb = InlineKeyboardBuilder()
    kb.row(InlineKeyboardButton(text='Сгенерировать текст', callback_data='generate_text'))
    kb.row(InlineKeyboardButton(text='Сгенерировать изображение', callback_data='generate_image'),
           InlineKeyboardButton(text='Изменить параметры генерации', callback_data='generate_parameters'))
    kb.row(InlineKeyboardButton(text='Помощь',
                                url='https://telegra.ph/'))
    kb.row(InlineKeyboardButton(text='Личный кабинет', callback_data='personal_cabinet'),
           InlineKeyboardButton(text='Купить подписку', callback_data='buy_subscribe'))
    return kb.as_markup()


def buy_sub():
    kb = InlineKeyboardBuilder()
    kb.row(InlineKeyboardButton(text='Купить подписку', callback_data='sub'))
    kb.row(InlineKeyboardButton(text='Помощь',
                                url='https://telegra.ph/'))
    return kb.as_markup()
