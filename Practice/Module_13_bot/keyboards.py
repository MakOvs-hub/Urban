from aiogram.types import ReplyKeyboardMarkup,KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
import random

# kb = ReplyKeyboardMarkup()
# ikb = InlineKeyboardMarkup()

start_kb = ReplyKeyboardMarkup(                    #создадим стартовую клавиатуру
    keyboard=[
        [
        KeyboardButton(text = 'Стоимость'),
        KeyboardButton(text = 'О нас'),
        ]
    ], resize_keyboard=True
)

catalog_kb = InlineKeyboardMarkup(                    #создадим каталог
    inline_keyboard=[
        [InlineKeyboardButton(text="Средняя игра", callback_data='medium')],
        [InlineKeyboardButton(text="Большая игра", callback_data='big')],
        [InlineKeyboardButton(text="Огромная игра", callback_data='mega')],
        [InlineKeyboardButton(text="Другие предложения", callback_data='other')],
    ]
)

buy_kb = InlineKeyboardMarkup(                    #создадим кнопку покупки
    inline_keyboard=[
        [InlineKeyboardButton(text="Купить", url='https://www.audi.com/en.html')],
    ]
)
buy_kb1 = InlineKeyboardMarkup(                    #создадим кнопку покупки
    inline_keyboard=[
        [InlineKeyboardButton(text="Купить", url='https://www.volvocars.com/ru/')],
    ]
)
buy_kb2 = InlineKeyboardMarkup(                    #создадим кнопку покупки
    inline_keyboard=[
        [InlineKeyboardButton(text="Купить", url='https://porsche.ru/index.html')],
    ]
)
