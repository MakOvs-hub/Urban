from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
'''
python==3.9.13
aiogram==2.25.1
aiohttp==3.8.6
aiosignal==1.3.1
async-timeout==4.0.3
attrs==23.2.0
Babel==2.9.1
certifi==2024.7.4
charset-normalizer==3.3.2
frozenlist==1.4.1
idna==3.7
magic-filter==1.0.12
multidict==6.0.5
pytz==2024.1
yarl==1.9.4
'''
api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start_mes(message):
    print('Привет! Я бот, помогающий твоему здоровью.')
    await message.answer('Привет! Я бот, помогающий твоему здоровью!')

@dp.message_handler(text=['Calories'])
async def set_age(message):
    await message.answer('Введите свой возраст:')
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
    calorage1 = 10 * data['weightr'] + 6.25 * data['growthr'] - 5 * data['ager'] + 5 # for man
    calorage2 = 10 * data['weightr'] + 6.25 * data['growthr'] - 5 * data['ager'] - 161 # for woman
    await message.answer(f'Рекомендуемое количество каллорий для мужчин: {calorage1} кКал, для женщин: {calorage2} кКал')
    await state.finish()

@dp.message_handler()
async def all_mes(message):
    print('Введите команду /start, чтобы начать общение.')
    await message.answer(f'К сожалению, я пока не понимаю {message.text.lower()}, зато понимаю слово - Calories. Давайте начнем с него.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
