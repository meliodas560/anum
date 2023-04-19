
import io
import os

from PIL import Image
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest
from GreyCilik import telethn as tbot, TEMP_DOWNLOAD_DIRECTORY
from GreyCilik import ubot2
from GreyCilik.events import register 


@register(pattern="^/mtoi ?(.*)")
async def cevir(event):
    rep_msg = await event.get_reply_message()
    if not event.is_reply or not rep_msg.sticker:
        await event.reply("`Reply to Sticker...`")
        return
    xxnx = await event.reply("`🔄 Converting...`")
    foto = io.BytesIO()
    foto = await ubot2.download_media(rep_msg.sticker, foto)
    im = Image.open(foto).convert("RGB")
    im.save("sticker.png", "png")
    await tbot.send_file(
        event.chat_id,
        "sticker.png",
        reply_to=rep_msg,
    )
    await xxnx.delete()
    os.remove("sticker.png")


@register(pattern="^/mtos ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.reply(
            "`Reply To Image...`"
        )
        return
    reply_message = await event.get_reply_message()
    ucup = await tbot.download_media(reply_message)
    if not reply_message.media:
        await event.reply("`Reply to Image`...")
        return
    chat = "@buildstickerbot"
    xx = await event.reply("`🔄 Converting...`")
    async with ubot2.conversation(chat) as conv:
        try:
            msg_start = await conv.send_message("/start")
            sticker = await conv.get_response()
            await ubot2.send_read_acknowledge(conv.chat_id)
            await ubot2.send_file(conv.chat_id, file=ucup)
            sticker = await conv.get_response()
            yanto = await ubot2.download_media(
                sticker.media,
                TEMP_DOWNLOAD_DIRECTORY
            )
            await tbot.send_file(
                event.chat_id,
                yanto,
            )
            await xx.delete()
        except YouBlockedUserError:
            msg_start = await conv.send_message("/start")
            sticker = await conv.get_response()
            await ubot2.send_read_acknowledge(conv.chat_id)
            await ubot2.send_file(conv.chat_id, file=ucup)
            sticker = await conv.get_response()
            yanto = await ubot2.download_media(
                sticker.media,
                TEMP_DOWNLOAD_DIRECTORY
            )
            await tbot.send_file(
                event.chat_id,
                yanto,
            )
            await ubot2.delete_messages(
            conv.chat_id, sticker
            )
            await xx.delete()
