from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
import logging

from filters import IsPrivate
from loader import dp

@dp.message_handler(IsPrivate(), CommandStart())
async def bot_start(message: types.Message):


    await message.answer(f"Salom, <i>{message.from_user.full_name}!</i>\n"
                         f"<u>AXF 716-19</u> guruhining <b>rasmiy botiga</b> xush kelibsiz!")

