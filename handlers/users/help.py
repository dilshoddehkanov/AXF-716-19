from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam",
            "/bugun - Bugungi dars jadvalini chiqaradi",
            "/erta - Ertangi dars jadvalini chiqaradi"
            )
    
    await message.answer("\n".join(text))
