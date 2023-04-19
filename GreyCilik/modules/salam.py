import random
from pyrogram import filters
from pyrogram.types import Message
from GreyCilik import pbot
import json
import asyncio
import requests



SALAM = (
    "Waalaikumsalam 👋",
    "Iyah WaalaikumSalam, ada yang aku bisa bantu?",
    "Waalaikumsalam, Gimana Kabarnya?",
    "Waalaikumsalam Warrohmatullahi Wabarokatu",
    "Waalaikumsalam, Salam Kenal 👋",
)


HALO = (
    "Halo Juga 👋",
    "Iya Halo Juga 👋",
    "Iya Halo Juga, Gimana Kabarnya?",
    "Halo Juga, Kenalin Aku Cilik 😉",
    "Halo juga, ada yang bisa aku bantu?",
)

HAY = (
    "Hay Juga 👋",
    "Iya Hay Juga 👋",
    "Iya Hay Juga, Gimana Kabarnya?",
    "Hay Juga, Kenalin Aku Cilik 😉",
    "Hay, ada yang bisa aku bantu?",
)

HI = (
    "HI Juga 👋",
    "Iya Hi Juga 👋",
    "Iya Hi Juga, Gimana Kabarnya?",
    "Hi Juga, Kenalin Aku Cilik 😉",
    "Hi, ada yang bisa aku bantu?",
)

GREY = (
    "Om @greyyvbss di cariin tuh 🥱",
    "Owner Aku lagi sibuk kak 🥴",
    "Bang @greyyvbss Kamu Dimana?",
    "Dia Lagi tidur kak awkawok",
    "Cok @greyyvbss di cariin tuh 🤓",
)
    
@pbot.on_message(filters.command("adzan", "/"))
async def adzan(_, message: Message):
    LOKASI = message.text.split(None, 1)[1]
    if len(message.command) < 2:
        return await message.reply("<b>Tuliskan nama kota anda</b>")
    url = f"http://muslimsalat.com/{LOKASI}.json?key=bd099c5825cbedb9aa934e255a81a5fc"
    request = requests.get(url)
    if request.status_code != 200:
        await message.reply(f"<b>Maaf Tidak Menemukan Kota <code>{LOKASI}</code>")
    result = json.loads(request.text)
    catresult = f"""
Jadwal Shalat Hari Ini
<b>Tanggal</b> <code>{result['items'][0]['date_for']}</code>
<b>Kota</b> <code>{result['query']} | {result['country']}</code>
<b>Terbit:</b> <code>{result['items'][0]['shurooq']}</code>
<b>Subuh:</b> <code>{result['items'][0]['fajr']}</code>
<b>Zuhur:</b> <code>{result['items'][0]['dhuhr']}</code>
<b>Ashar:</b> <code>{result['items'][0]['asr']}</code>
<b>Maghrib:</b> <code>{result['items'][0]['maghrib']}</code>
<b>Isya:</b> <code>{result['items'][0]['isha']}</code>
"""
    await message.reply(catresult)
