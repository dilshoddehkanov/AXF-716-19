import io

from aiogram import types
from aiogram.dispatcher.filters import Command, Text

from filters import IsGroup
from filters.admins import AdminFilter
from loader import dp, bot

@dp.message_handler(IsGroup(), Command("set_photo", prefixes="!/"), AdminFilter())
async def set_new_photo(message: types.Message):
    source_message = message.reply_to_message
    photo = source_message.photo[-1]
    photo = await photo.download(destination=io.BytesIO())
    input_file = types.InputFile(photo)
    #1-usul
    await message.chat.set_photo(photo=input_file)


@dp.message_handler(IsGroup(), Command("set_title", prefixes="!"), AdminFilter())
async def set_new_title(message: types.Message):
    source_message = message.reply_to_message
    title = source_message.text
    #2-usul
    await bot.set_chat_title(message.chat.id, title=title)



@dp.message_handler(IsGroup(), Command("set_description", prefixes="!/"), AdminFilter())
async def set_new_description(message: types.Message):
    source_message = message.reply_to_message
    description = source_message.text
    # 1-usul
    # await bot.set_chat_description(message.chat.id, description=description)
    # 2-usul
    await message.chat.set_description(description=description)

@dp.message_handler(IsGroup(), Text(contains='Diqqat', ignore_case=True), AdminFilter())
async def set_new_description(message: types.Message):
    await message.reply('@Web_developper_D @Xatamov0420 @Akbar_TUIT @Ibrohim_Erkinov '
                        '@Farrux1999A @Shaxboz_Adizov @dvaliyev @ava_099 @Javlon2050 '
                        '@UAA_0619 @Farrux_Aktamov ')
    await message.reply('@Tohir0301 @Study_TUIT @Ziyo2311 @Faxriddin87 @MuhammadaliIbnShuhrat '
                        '@AtabekovAsadbek @MUHAMMAD_712 @RustamovJX @Isfandiyor_24 @hasanov_sherzodbek'
                        ' @Alfa_7887 ')
