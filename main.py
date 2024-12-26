import logging

from misc import create_kb

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Вывод информации при запуске бота
logging.info("Запуск бота...")

import asyncio
import sys
import traceback

from aiogram import Bot, Dispatcher, Router, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.methods import EditMessageText
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton, KeyboardButton, InlineKeyboardMarkup, CallbackQuery, ReplyKeyboardMarkup
from aiogram.types.web_app_info import WebAppInfo
from aiogram import F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.methods.send_message import SendMessage
from aiogram.types import FSInputFile
import sqlite3
from datetime import date


import sys
import os


TEST_TOKEN = "7373519023:AAGHAMx01azAa4XRtG_QP3JApqLLEcxFsSg"
MAIN_TOKEN = '7313284335:AAEZpuTjVjdNLquAPcoWSvIck2T9HMb6Fek'

dp = Dispatcher()


@dp.message(Command('start'))
async def start_command(message: types.Message, state: FSMContext):
    kb = create_kb()
    await message.answer("Выберите действие", reply_markup=kb.as_markup())



async def main(token: str) -> None:
    global bot
    if token == "test":
        bot = Bot(TEST_TOKEN)
        await dp.start_polling(bot)
    else:
        bot = Bot(MAIN_TOKEN)
        await dp.start_polling(bot)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <token>")
    else:
        try:
            TOKEN = sys.argv[1]
            asyncio.run(main(TOKEN))
        except Exception as e:
            logging.exception(f"Произошла ошибка: {e}")
            print(f"Произошла ошибка: {e}")