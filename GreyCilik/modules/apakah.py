import random
from GreyCilik.events import register
from GreyCilik import telethn

APAKAH_STRING = ["Iya", 
                 "Tidak", 
                 "Mungkin", 
                 "Mungkin Tidak", 
                 "Bisa jadi", 
                 "Mungkin Tidak",
                 "Tidak Mungkin",
                 "YA NDAK TAHU KOK TANYA SAYA",
                 "Pala kau pecah",
                 "Apa iya?",
                 "Tanya aja sama mamakmu",
                 "Lu tanya gua, terus gua tanya siapa?",
                 "Ebuzed",
                 "Et dah bang",
                 "Typo aoa banh",
                 "gaoaoa aku gaoaoa",
                 "Au dah",
                 "Kata Siapa?",
                 "Benar Sekali",
                 "Ngga Bangettt!!!",
                 "ihh Ke GR an Banget si",
                 "Terserah Lu dah",
                 "Iya Si Ken Emang Ganteng"
               
                 ]


@register(pattern="^/apakah ?(.*)")
async def apakah(event):
    quew = event.pattern_match.group(1)
    if not quew:
        await event.reply('Berikan saya pertanyaan 😐')
        return
    await event.reply(random.choice(APAKAH_STRING))
