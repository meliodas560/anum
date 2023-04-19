import os

from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest
from GreyCilik import telethn as tbot, TEMP_DOWNLOAD_DIRECTORY
from GreyCilik import ubot2
from GreyCilik.events import register
from GreyCilik.modules.language import gs


@register(pattern="^/tt ?(.*)")
async def tiktod(event):
    xxnx = event.pattern_match.group(1)
    if xxnx:
        d_link = xxnx
    elif event.is_reply:
        d_link = await event.get_reply_message()
    else:
        return await event.reply("**Tiktok Downloader**\n**Usage:** `/tiktok [link]`")
    mmk = await event.reply("`📥 Download...`")
    chat = "@thisvidbot"
    async with ubot2.conversation(chat) as conv:
        try:
            msg_start = await conv.send_message("/start")
            r = await conv.get_response()
            msg = await conv.send_message(d_link)
            details = await conv.get_response()
            video = await conv.get_response()
            text = await conv.get_response()
            await ubot2.send_read_acknowledge(conv.chat_id)
            yanto = await ubot2.download_media(
                video.media,
                TEMP_DOWNLOAD_DIRECTORY
            )
            await mmk.edit("`📤 Uploaded...`")
            await tbot.send_file(
                event.chat_id,
                yanto,
                caption="**Success Download from TikTok!** ✨",
            )
        except YouBlockedUserError:
            await ubot2(UnblockRequest(chat))
            msg_start = await conv.send_message("/start")
            r = await conv.get_response()
            msg = await conv.send_message(d_link)
            details = await conv.get_response()
            video = await conv.get_response()
            text = await conv.get_response()
            await ubot2.send_read_acknowledge(conv.chat_id)
            yanto = await ubot2.download_media(
                video.media,
                TEMP_DOWNLOAD_DIRECTORY
            )
            await tbot.send_file(
                event.chat_id,
                yanto,
                caption="**Success Download from TikTok!** ✨",
            )
            await ubot2.delete_messages(
            conv.chat_id, [msg_start.id, r.id, msg.id, details.id, video.id, text.id]
        )
    await mmk.delete()
    return os.remove(yanto)


@register(pattern="^/ig ?(.*)")
async def sosmed(event):
    xxnx = event.pattern_match.group(1)
    if xxnx:
        d_link = xxnx
    elif event.is_reply:
        d_link = await event.get_reply_message()
    else:
        return await event.reply("**Instagram Downloader**\n**Usage:** `/ig [link]`")
    mmk = await event.reply("📥 `Download...`")
    chat = "@SaveAsbot"
    async with ubot2.conversation(chat) as conv:
        try:
            msg_start = await conv.send_message("/start")
            r = await conv.get_response()
            msg = await conv.send_message(d_link)
            video = await conv.get_response()
            details = await conv.get_response()
            text = await conv.get_response()
            await ubot2.send_read_acknowledge(conv.chat_id)
            yanto = await ubot2.download_media(
                video.media,
                TEMP_DOWNLOAD_DIRECTORY
            )
            await mmk.edit("📤 `Uploaded...`")
            await tbot.send_file(
                event.chat_id,
                yanto,
                caption="**Success Download from Instagram!** ✨",
            )
        except YouBlockedUserError:
            await ubot2(UnblockRequest(chat))
            msg_start = await conv.send_message("/start")
            r = await conv.get_response()
            msg = await conv.send_message(d_link)
            video = await conv.get_response()
            details = await conv.get_response()
            text = await conv.get_response()
            await ubot2.send_read_acknowledge(conv.chat_id)
            yanto = await ubot2.download_media(
                video.media,
                TEMP_DOWNLOAD_DIRECTORY
            )
            await tbot.send_file(
                event.chat_id,
                yanto,
                caption="**Success Download from Instagram** ✨",
            )
            await ubot2.delete_messages(
            conv.chat_id, [msg_start.id, r.id, msg.id, details.id, video.id, text.id]
        )
    await mmk.delete()
    return os.remove(yanto)


def helps(chat):
    return gs(chat, "sosmed_help")


__mod_name__ = "Sosmed"
