from aiogram import types

from filters import IsPrivate
from loader import dp
import random

import datetime as dt

dushanba = "1️⃣. A-118 xonada <u><b>Kiriptografiya</b>(amaliy)</u> {11:30}\n\n" \
           "2️⃣. C-443 xonada <u><b>Ekalogiya</b>(amaliy)</u> {13:30}\n\n" \
           "3️⃣. C-353 xonada <u><b>Ekalogiya</b>(ma'ruza)</u> {15:00}\n\n" \
           "4️⃣. A-222 xonada <u><b>Kompyuter tarmoqlari</b>(ma'ruza)</u> {16:30}"

seshanba = "1️⃣. D-211 xonada <u><b>Kiriptografiya</b>(amaliy)</u> {13:30}\n\n" \
           "2️⃣. D-211 xonada <u><b>Mashinali o'qitish</b>(amaliy)</u> {15:00}\n\n" \
           "3️⃣. <u><i><b>Dars qo'yilmagan</b></i></u>🥳"
chorshanba = '<b>Bugun AXF 716-19-guruhi talabalari uchun dam olish kuni🥳🥳🥳\nMazzami slaga aa mazzami?😂😂😂</b>'
payshanba = "1️⃣. C-351 xonada <u><b>BT</b>(amaliy)</u> {13:30}\n\n" \
            "2️⃣. B-413 xonada <u><b>Mashinali o'qitish</b>(ma'ruza)</u> {15:00}\n\n" \
            "3️⃣. D-301 xonada <u><b>Kriptografiya</b>(ma'ruza)</u> {16:30}"

juma = "1️⃣. D-303 <u><b>Kompyuter tarmoqlari</b>(lab)</u> {13:30}\n\n" \
       "2️⃣. C-450 <u><b>Boshqaruv tamoyillari</b>(ma'ruza)</u> {15:00}\n\n" \
       "3️⃣. C-449 <u><b>Boshqaruv tamoyillari</b>(ma'ruza)</u> {16:30}"

shanba = "1️⃣. A-108 <u><b>Mashinali o'qitish</b>(ma'ruza)</u> {13:30}\n\n" \
         "2️⃣. C-213 <u><b>Kompyuter tarmoqlari</b>(ma'ruza)</u> {15:00}\n\n" \
         "3️⃣. <b>Dars qo'yilmagan</b>🥳"
yakshanba = 'Bugun dam olish kuni'

sticer = ["😕","😆","😂","😏","😉","️😊","👍","🧐","😎"]

barchasi = {'Monday': dushanba, 'Tuesday': seshanba, 'Wednesday': chorshanba, 'Thursday': payshanba, 'Friday': juma,
            'Saturday': shanba, 'Sunday': yakshanba}
barchasi2 = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday',
             6: 'Saturday', 0: 'Sunday'}
hafta = {'Monday': "Dushanba", 'Tuesday': "Seshanba", 'Wednesday': "Chorshanba", 'Thursday': "Payshanba",
         'Friday': "Juma",
         'Saturday': "Shanba", 'Sunday': "Yakshanba"}

bayramlar = ["01:10:2021", "31:12:2021","02:10:2021"]

word1 = {"salom": "salombek", "Salom": "Volekum salom", "Assalom": "Assalomu alaykum", "qalesila": "Zo'r",
         "charchamayapsilami": "Yo'q rahmat", "nima gaplar": "tinchlik",
         "tinchmisizlar": "ha tinchmiz","qalesan":"👍🏻", "qanday": "yaxshi", "yaxshi": "yaxshi",
         "bilaman": "bilishizi bilamiz", "jim utir": "kim", "voy": "haa",
         "zur": "sps", "zo'r": "rahmat", "chiqibdi": "ok", "gap yo": "+++", "malades": "RAHMAT",
         "kim bu": "tanishamiz endi", "tanimadim": "manam tanimadim", "kimsan": "Kim", "eee": "+++",
         "jinni": "haqqatanam",
         '???': "!!!", "san": "Robot",'rahmat':"Arzimiydi!","Rahmat":"👍👍👍","kalit":"shilq bilq","bot":"Menda uu","Akbar_TUIT":"Nimagap mana man"}



now = dt.datetime.now()
day = now.strftime('%d:%m:%Y')

@dp.message_handler(commands='bugun')
async def dars_jadval(message: types.Message):
    if day in bayramlar:
        await message.answer('Bugun AXF 716-19-guruhi talabalari uchun bayram🥳🥳🥳'
                             '\nMazzami slaga aa mazzami?😂😂😂')

    weekday_name = now.strftime('%A')
    weekday = hafta[barchasi2[int(now.strftime('%w'))]]
    await message.answer(f"<b><i>Bugun: {weekday}</i></b>\n\n" + barchasi[weekday_name])

@dp.message_handler(commands='erta')
async def dars_jadval(message: types.Message):
    weekday = int(now.strftime('%w')) + 1
    if weekday == 7 or weekday == 3:
        kun = f"<b><i>Ertaga: {hafta[barchasi2[weekday]]}</i></b>\n\n" + "Ertaga dam olish kuni!"
    await message.answer(f"<b><i>Ertaga: {hafta[barchasi2[weekday]]}</i></b>\n\n" + barchasi[barchasi2[weekday]])

@dp.message_handler(text = word1.keys())
async def answer_text(message: types.Message):
    user_message = message.text
    result = word1[user_message]
    if result:
        await message.answer("<i>"+result+"</i>" + random.choices(sticer)[0])

@dp.message_handler(IsPrivate, text = 'bugungi')
async def answer_text(message: types.Message):
    await message.answer('salom')