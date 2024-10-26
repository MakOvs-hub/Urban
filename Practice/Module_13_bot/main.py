from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
import logging

from config import *
import texts
from keyboards import *

logging.basicConfig(level=logging.INFO, filemode='w', filename='bot_logs.log',encoding='UTF-8', format='%(asctime)s | %(levelno)s | %(levelname)s | %(message)s')
bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start_mes(message):
    await message.answer(texts.start, reply_markup=start_kb)

@dp.message_handler(text ="О нас")
async def info(message):
    await message.answer(texts.about, reply_markup=start_kb)

@dp.message_handler(text="Стоимость")
async def price(message):
    await message.answer('Что вас интересует?', reply_markup=catalog_kb)

@dp.callback_query_handler(text='medium')
async def buy_m(call):
    await call.message.answer(texts.gameM, reply_markup=buy_kb)
    await call.answer()

@dp.callback_query_handler(text='big')
async def buy_l(call):
    await call.message.answer(texts.gameL, reply_markup=buy_kb1)
    await call.answer()

@dp.callback_query_handler(text='mega')
async def buy_xl(call):
    await call.message.answer(texts.gameXL, reply_markup=buy_kb2)
    await call.answer()

@dp.callback_query_handler(text='other')
async def buy_other(call):
    await call.message.answer(texts.other)
    await call.answer()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
