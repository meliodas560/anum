# @greyyvbss
# Dont Remove Credit

import os
import asyncio

from telethon.errors.rpcerrorlist import YouBlockedUserError
from PIL import Image, ImageDraw, ImageFont
from GreyCilik.events import register
from GreyCilik.modules.language import gs
from GreyCilik import telethn as tbot, ubot2, TEMP_DOWNLOAD_DIRECTORY

def text_set(text):
    lines = []
    if len(text) <= 55:
        lines.append(text)
    else:
        all_lines = text.split("\n")
        for line in all_lines:
            if len(line) <= 55:
                lines.append(line)
            else:
                k = len(line) // 55
                for z in range(1, k + 2):
                    lines.append(line[((z - 1) * 55) : (z * 55)])
    return lines[:25]


@register(pattern="^/tulis1 ?(.*)")
async def writer(event):
    if event.reply_to:
        reply = await event.get_reply_message()
        text = reply.message
    elif event.pattern_match.group(1).strip():
        text = event.text.split(maxsplit=1)[1]
    else:
        return await event.reply("`Add the text you want to make`")
    k = await event.reply("`Writing... ✍🏻`")
    img = Image.open("GreyCilik/resources/kertas.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("GreyCilik/resources/assfont.ttf", 30)
    x, y = 150, 140
    lines = text_set(text)
    line_height = font.getsize("hg")[1]
    for line in lines:
        draw.text((x, y), line, fill=(1, 22, 55), font=font)
        y = y + line_height - 5
    file = "cilik.jpg"
    img.save(file)
    await event.reply(file=file)
    os.remove(file)
    await k.delete()
    

@register(pattern="^/tulis2 ?(.*)")
async def _(event):
    if event.reply_to:
        reply = await event.get_reply_message()
        text = reply.message
    elif event.pattern_match.group(1).strip():
        text = event.text.split(maxsplit=1)[1]
    else:
        return await event.reply("`Add the text you want to make`")
    mmk = await event.reply("`Writing... ✍🏻`")
    chat = "@awakmalas_bot"
    async with ubot2.conversation(chat) as conv:
        try:
            msg_font = await conv.send_message("/setfont")
            r = await conv.get_response()
            msg = await conv.send_message("Font 1")
            r2 = await conv.get_response()
            msg2 = await conv.send_message(f"/malas1 {text}")
            response = await conv.get_response()
            nulis = await conv.get_response()
            """ - don't spam notif - """
            await ubot2.send_read_acknowledge(conv.chat_id)
            yanto = await ubot2.download_media(
               nulis.media,
               TEMP_DOWNLOAD_DIRECTORY
            )
            await mmk.edit("`📤 Uploaded...`")
            await tbot.send_file(
                event.chat_id,
                yanto,
                caption="📌 **Writed by Ilham** ✨",
            )
            await mmk.delete()
        except YouBlockedUserError:
            await event.reply(
                "**Error: Mohon Buka Blokir** @awakmalas_bot **Dan Coba Lagi!**"
            )
            return
        await asyncio.sleep(0.5)
        await tbot.send_file(
            event.chat_id,
            nulis,
            caption="**Tulis By Cilik** ✨",
        )
        await ubot2.delete_messages(conv.chat_id, [msg_font.id, r.id, msg.id, r2.id, msg2.id, response.id, nulis.id])
        await mmk.delete()
    
def helps(chat):
    return gs(chat, "write_help")


__mod_name__ = "Tulis"    
    
