import json
import requests
import asyncio
import html
from GreyCilik.events import register
from GreyCilik.modules.language import gs

@register(pattern="^/cat ?(.*)")
async def cats(event):
    xx = await event.reply("`Mencari Gambar Kucing...`")
    response = requests.get("https://shibe.online/api/cats").json()
    if not response:
        await event.reply("**Tidak bisa menemukan kucing.**")
        return
    await event.client.send_message(entity=event.chat_id, file=response[0])
    await xx.delete()


#@register(pattern="^/adzan ?(.*)")
#async def get_adzan(event):
#    "Shows you the Islamic prayer times of the given city name"
#    input_str = adzan.pattern_match.group(1)
#    LOKASI = "Jakarta" if not input_str else input_str
#    url = f"http://muslimsalat.com/{LOKASI}.json?key=bd099c5825cbedb9aa934e255a81a5fc"
#    request = requests.get(url)
#    if request.status_code != 200:
#        return await event.reply(
#            f"**Tidak Dapat Menemukan Kota** `{LOCATION}`", 120
#        )
#    result = json.loads(request.text)
#    azanresult = f"<b>Jadwal Shalat Hari Ini:</b>\
#            \n<b>📆 Tanggal </b><code>{result['items'][0]['date_for']}</code>\
#            \n<b>📍 Kota</b> <code>{result['query']}</code> | <code>{result['country']}</code>\
#            \n\n<b>Terbit  : </b><code>{result['items'][0]['shurooq']}</code>\
#            \n<b>Subuh : </b><code>{result['items'][0]['fajr']}</code>\
#            \n<b>Zuhur  : </b><code>{result['items'][0]['dhuhr']}</code>\
#            \n<b>Ashar  : </b><code>{result['items'][0]['asr']}</code>\
#            \n<b>Maghrib : </b><code>{result['items'][0]['maghrib']}</code>\
#            \n<b>Isya : </b><code>{result['items'][0]['isha']}</code>\
#    "
#    await event.reply(azanresult, "html")

    
@register(pattern="^/copy ?(.*)")
async def copy(event):
    reply = await event.get_reply_message()
    if reply:
        await reply.reply(reply)
        return await event.try_delete()
    await event.reply("`Please Reply to message...`")
