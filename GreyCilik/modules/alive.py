import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from GreyCilik.events import register
from GreyCilik import telethn as tbot

CILIK = "https://telegra.ph/file/aaa73d0642f7a85251200.jpg"

PHOTO = "https://telegra.ph//file/7d190be061d96e86b840b.jpg"

QRIS = "https://telegra.ph/file/02630dc3593b90c9cc0e0.jpg"

@register(pattern=("/alive"))
async def awake(event):
  GREY = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Referz Store Assistant.** \n\n"
  GREY += "⚡️ **I'm Working Properly** \n\n"
  GREY += f"⚡️ **My Master : [MASTER](https://t.me/Bintangreferz)** \n\n"
  GREY += f"⚡️ **Library Version :** `{telever}` \n\n"
  GREY += f"⚡️ **Telethon Version :** `{tlhver}` \n\n"
  GREY += f"⚡️ **Pyrogram Version :** `{pyrover}` \n\n"
  GREY += "**Thanks For Adding Me Here My Love ❤️**"
  BUTTON = [[Button.url("ʜᴇʟᴘ​", "http://t.me/ReferzStoreAssistant_Bot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ​", "https://t.me/CilikSupport")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=GREY,  buttons=BUTTON)


@register(pattern=("/styletext"))
async def awake(event):
  RISA = "**✍️ -STYLE TEXT- ✍️** \n"
  RISA += "**Styling Your Text** \n\n"
  RISA += "How To Make ❓ \n"
  RISA += "✪ `/f1 <text> (匚丨ㄥ丨Ҝ)` \n"
  RISA += "✪ `/f2 <text> (Ⓒⓘⓛⓘⓚ)` \n"
  RISA += "✪ `/f3 <text> (🅒🅘🅛🅘🅚)` \n"
  RISA += "✪ `/f4 <text> (🄲🄸🄻🄸🄺)` \n"
  RISA += "✪ `/f5 <text> (🅲🅸🅻🅸🅺)` \n"
  RISA += "✪ `/f6 <text> (🇨🇮🇱🇱🇰 )` \n"
  RISA += "✪ `/f7 <text> (𝒸𝒾𝓁𝒾𝓀)` \n"
  RISA += "✪ `/f8 <text> (𝕔𝕚𝕝𝕚𝕜)` \n"
  RISA += "✪ `/f9 <text> (ᴄɪʟɪᴋ)` \n"
  RISA += "✪ `/f10 <text> (𝐂𝐈𝐋𝐈𝐊)`"
  BUTTON = [[Button.url("ʜᴇʟᴘ​", "https://t.me/lordilhamxrobot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ​", "https://t.me/libitrashh")]]
  await tbot.send_file(event.chat_id, CILIK, caption=RISA,  buttons=BUTTON)


@register(pattern=("/ssdonate"))
async def awake(event):
  BAU = f"👋🏻 **Hi [{event.sender.first_name}](tg://user?id={event.sender.id})**\n" 
  BAU += "**Jika kamu yang ingin berdonasi silahkan scan Qris diatas ini, agar bot Libi tetap hidup dan membantu aktifitas anda di Telegram.**\n\n"
  BAU += "🙇🏻‍♂️ **Terimakasih yang sudah mau Berdonasi**"
  BUTTON = [[Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/libisupport"), Button.url("sᴜᴘᴘᴏʀᴛ​", "https://t.me/libitrashh")]]
  await tbot.send_file(event.chat_id, QRIS, caption=BAU,  buttons=BUTTON)

