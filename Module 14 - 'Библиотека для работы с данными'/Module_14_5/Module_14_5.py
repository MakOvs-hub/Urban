"Написание примитивной ORM"
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from crud_functions import *

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
# kb = ReplyKeyboardMarkup()
ikb = InlineKeyboardMarkup()

get_all_products()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()


# button = KeyboardButton(text = 'Рассчитать')
# button2 = KeyboardButton(text = 'Информация')
# kb.add(button)
# kb.add(button2)
start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Рассчитать'),
         KeyboardButton(text='Информация')],
        [KeyboardButton(text='Купить')],
        [KeyboardButton(text='Регистрация')],
    ], resize_keyboard=True
)

buying_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Product1", callback_data='product_buying')],
        [InlineKeyboardButton(text="Product2", callback_data='product_buying')],
        [InlineKeyboardButton(text="Product3", callback_data='product_buying')],
        [InlineKeyboardButton(text="Product4", callback_data='product_buying')],
    ]
)

inbutton = InlineKeyboardMarkup(text='Рассчитать норму калорий', callback_data='calories')
inbutton2 = InlineKeyboardMarkup(text='Формулы расчёта', callback_data='formulas')
ikb.add(inbutton)
ikb.add(inbutton2)


@dp.message_handler(commands=['start'])
async def start_mes(message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью!', reply_markup=start_menu)


@dp.message_handler(text=['Регистрация'])
async def sing_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    if is_included(message.text):
        await message.answer('Данный username уже существует. Пожалуйста выберите другой ник.')
        await sing_up(message)
    else:
        await state.update_data(username=message.text)
        await message.answer("Введите свой email:")
        await RegistrationState.email.set()


@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=int(message.text))
    await state.update_data(balance=1000)
    get_user = await state.get_data()
    add_user(get_user['username'], get_user['email'], get_user['age'], get_user['balance'])
    await state.finish()
    await message.answer('Поздравляем! Вы успешно зарегистрированы!\n А Вы уже смотрели наши новинки?')


@dp.message_handler(text=['Купить'])
async def get_buying_list(message):
    for value in get_all_products():
        with open('Serotonin.jpg', "rb") as img:
            await message.answer_photo(img, f'Название: {value[1]} | Описание: {value[2]} | Цена: {value[3]}')
    await message.answer("Выберите продукт для покупки:", reply_markup=buying_menu)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=ikb)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer(f'для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5\n'
                              f'для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(ager=int(message.text))
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growthr=int(message.text))
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weightr=int(message.text))
    data = await state.get_data()
    calorage1 = 10 * data['weightr'] + 6.25 * data['growthr'] - 5 * data['ager'] + 5  # for man
    calorage2 = 10 * data['weightr'] + 6.25 * data['growthr'] - 5 * data['ager'] - 161  # for woman
    await message.answer(
        f'Рекомендуемое количество каллорий для мужчин: {calorage1} кКал, для женщин: {calorage2} кКал')
    await state.finish()


@dp.message_handler()
async def all_mes(message):
    print('Введите команду /start, чтобы начать общение.')
    await message.answer(
        f'К сожалению, я пока не понимаю {message.text.lower()}, зато понимаю слово - Calories. Давайте начнем с него.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
