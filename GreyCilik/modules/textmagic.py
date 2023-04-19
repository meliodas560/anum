import asyncio
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest
from GreyCilik import telethn as tbot
from GreyCilik import ubot2
from GreyCilik.events import register

@register(pattern="^/magictext ?(.*)")
async def tiktod(event):
    xxnx = event.pattern_match.group(1)
    if xxnx:
        text = xxnx
    elif event.is_reply:
        text = await event.get_reply_message()
    else:
        return await event.reply("**Magic Your Text** ✨\n**Usage:** `/magictext <text>`")
    mmk = await event.reply("**Magic Your Text** ✨")
    chat = "@TextMagicBot"
    async with ubot2.conversation(chat) as conv:
        try:
            msg_start = await conv.send_message("/start")
            knyl = await conv.get_response()
            isi = await conv.send_message(f"{text}")
            msg1 = await conv.get_response()
            msg2 = await conv.get_response()
            msg3 = await conv.get_response()
            msg4 = await conv.get_response()
            msg5 = await conv.get_response()
            msg6 = await conv.get_response()
            msg7 = await conv.get_response()
            msg8 = await conv.get_response()
            msg9 = await conv.get_response()
            msg10 = await conv.get_response()
            msg11 = await conv.get_response()
            msg12 = await conv.get_response()
            msg13 = await conv.get_response()
            msg14 = await conv.get_response()
            msg15 = await conv.get_response()
            msg16 = await conv.get_response()
            msg17 = await conv.get_response()
            await ubot2.send_read_acknowledge(conv.chat_id)
            await asyncio.sleep(0.5)
            await tbot.send_message(event.chat_id, f"```{msg1.message}```")
            await tbot.send_message(event.chat_id, f"```{msg2.message}```")
            await tbot.send_message(event.chat_id, f"```{msg3.message}```")
            await tbot.send_message(event.chat_id, f"```{msg4.message}```")
            await tbot.send_message(event.chat_id, f"```{msg5.message}```")
            await tbot.send_message(event.chat_id, f"```{msg6.message}```")
            await tbot.send_message(event.chat_id, f"```{msg7.message}```")
            await tbot.send_message(event.chat_id, f"```{msg8.message}```")
            await tbot.send_message(event.chat_id, f"```{msg9.message}```")
            await tbot.send_message(event.chat_id, f"```{msg10.message}```")
            await tbot.send_message(event.chat_id, f"```{msg11.message}```")
            await tbot.send_message(event.chat_id, f"```{msg12.message}```")
            await tbot.send_message(event.chat_id, f"```{msg13.message}```")
            await tbot.send_message(event.chat_id, f"```{msg14.message}```")
            await tbot.send_message(event.chat_id, f"```{msg15.message}```")
            await tbot.send_message(event.chat_id, f"```{msg16.message}```")
            await tbot.send_message(event.chat_id, f"```{msg17.message}```")
            await ubot2.delete_messages(
                conv.chat_id, [msg_start.id, isi.id]
            )
        except YouBlockedUserError:
            await ubot2(UnblockRequest(chat))
            msg_start = await conv.send_message("/start")
            knyl = await conv.get_response()
            isi = await conv.send_message(f"{text}")
            msg1 = await conv.get_response()
            msg2 = await conv.get_response()
            msg3 = await conv.get_response()
            msg4 = await conv.get_response()
            msg5 = await conv.get_response()
            msg6 = await conv.get_response()
            msg7 = await conv.get_response()
            msg8 = await conv.get_response()
            msg9 = await conv.get_response()
            msg10 = await conv.get_response()
            msg11 = await conv.get_response()
            msg12 = await conv.get_response()
            msg13 = await conv.get_response()
            msg14 = await conv.get_response()
            msg15 = await conv.get_response()
            msg16 = await conv.get_response()
            msg17 = await conv.get_response()
            await ubot2.send_read_acknowledge(conv.chat_id)
            await asyncio.sleep(0.5)
            await tbot.send_message(event.chat_id, f"```{msg1.message}```")
            await tbot.send_message(event.chat_id, f"```{msg2.message}```")
            await tbot.send_message(event.chat_id, f"```{msg3.message}```")
            await tbot.send_message(event.chat_id, f"```{msg4.message}```")
            await tbot.send_message(event.chat_id, f"```{msg5.message}```")
            await tbot.send_message(event.chat_id, f"```{msg6.message}```")
            await tbot.send_message(event.chat_id, f"```{msg7.message}```")
            await tbot.send_message(event.chat_id, f"```{msg8.message}```")
            await tbot.send_message(event.chat_id, f"```{msg9.message}```")
            await tbot.send_message(event.chat_id, f"```{msg10.message}```")
            await tbot.send_message(event.chat_id, f"```{msg11.message}```")
            await tbot.send_message(event.chat_id, f"```{msg12.message}```")
            await tbot.send_message(event.chat_id, f"```{msg13.message}```")
            await tbot.send_message(event.chat_id, f"```{msg14.message}```")
            await tbot.send_message(event.chat_id, f"```{msg15.message}```")
            await tbot.send_message(event.chat_id, f"```{msg16.message}```")
            await tbot.send_message(event.chat_id, f"```{msg17.message}```")
            await ubot2.delete_messages(
                conv.chat_id, [msg_start.id, isi.id]
            )            
            await mmk.delete()

            
