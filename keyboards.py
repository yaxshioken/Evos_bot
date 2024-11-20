from itertools import product

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import keyboard

menu_button=ReplyKeyboardMarkup(keyboard=[
      [KeyboardButton(text='Qurilish Mollari',),KeyboardButton(text='Oshxona qurollari')],
      [KeyboardButton(text='Beton Mahsulotlari'),KeyboardButton(text='Mebel Mahsulotlari')],
  ], resize_keyboard=True)
product_button=ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Tsement"),KeyboardButton(text="Qum"),KeyboardButton(text="Shag'al"),KeyboardButton(text="G'isht")],
], resize_keyboard=True,one_time_keyboard=True)