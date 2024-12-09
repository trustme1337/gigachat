from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

from keyboards import keyboards
from config_data.config import Config, load_config
from database import database

user_router = Router()
config: Config = load_config()


@user_router.message(CommandStart())
@user_router.message(F.text == 'Главное меню')
async def start_menu(message: Message, state: FSMContext):
    await database.add_user(message.from_user.id)
    await message.answer(
        text=f'Привет, {message.from_user.first_name}! Ты используешь я бот ГигаЧат, я могу генерировать текста и '
             f'картинки. Выбери действие:',
        reply_markup=keyboards.start_menu())
    await state.clear()


@user_router.callback_query(F.data == 'personal_cabinet')
async def user_info(callback: CallbackQuery):
    user_info = await database.get_user_data(callback.from_user.id)
    is_premium = bool(user_info[2])
    text = f'Информация о пользователе:\nusername: @{callback.from_user.username}\nОсталось запросов: '
    text += 'неограничено' if is_premium else f'{user_info[1]} из 20'

    kb = None if is_premium else keyboards.buy_sub()
    await callback.message.answer(text=text, reply_markup=kb)
