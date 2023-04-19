import asyncio
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest
from GreyCilik import telethn as tbot
from GreyCilik import ubot2
from GreyCilik.events import register

@register(pattern="^/Nanya ?(.*)")
async def tnya1(event):
    xxnx = event.pattern_match.group(1)
    reply_to_id = event.message.id
    anu = "Kamu naanyeaa???\n\nCara Penggunaan: nanya siapa pembuat telegram?"
    cepmek = "./GreyCilik/resources/nanya.mp3"
    if xxnx:
        text = xxnx
    elif event.is_reply:
        text = await event.get_reply_message()
    else:
        return await tbot.send_file(
            event.chat_id, "./GreyCilik/resources/nanya.mp3", voice_note=True, caption=anu, reply_to=reply_to_id
        )
    mmk = await event.reply("sini, biar aku kasih tau yahh...")
    chat = "@kecerdasanbuatan_robot"
    async with ubot2.conversation(chat) as conv:
        try:
            msg_start = await conv.send_message("/start")
            knyl = await conv.get_response()
            isi = await conv.send_message(f". {text}")
            msg1 = await conv.get_response()
            await ubot2.send_read_acknowledge(conv.chat_id)
            msg2 = await conv.get_response()
            await tbot.send_message(event.chat_id, f"**Jawaban:**\n\n{msg2.message}")
            await ubot2.delete_messages(
                conv.chat_id, [msg_start.id, isi.id]
            )   
        except YouBlockedUserError:
            msg_start = await conv.send_message("/start")
            knyl = await conv.get_response()
            isi = await conv.send_message(f". {text}")
            msg1 = await conv.get_response()
            await ubot2.send_read_acknowledge(conv.chat_id)
            msg2 = await conv.get_response()
            await tbot.send_message(event.chat_id, f"**Jawaban:**\n\n{msg2.message}")
            await ubot2.delete_messages(
                conv.chat_id, [msg_start.id, isi.id]
            )           
    await mmk.delete()

    
@register(pattern="^/nanya ?(.*)")
async def tnya2(event):
    xxnx = event.pattern_match.group(1)
    reply_to_id = event.message.id
    anu = "Kamu naanyeaa???\n\nCara Penggunaan: nanya siapa pembuat telegram?"
    cepmek = "./GreyCilik/resources/nanya.mp3"
    if xxnx:
        text = xxnx
    elif event.is_reply:
        text = await event.get_reply_message()
    else:
        return await tbot.send_file(
            event.chat_id, "./GreyCilik/resources/nanya.mp3", voice_note=True, caption=anu, reply_to=reply_to_id
        )
    mmk = await event.reply("sini, biar aku kasih tau yahh...")
    chat = "@kecerdasanbuatan_robot"
    async with ubot2.conversation(chat) as conv:
        try:
            msg_start = await conv.send_message("/start")
            knyl = await conv.get_response()
            isi = await conv.send_message(f". {text}")
            msg1 = await conv.get_response()
            await ubot2.send_read_acknowledge(conv.chat_id)
            msg2 = await conv.get_response()
            await tbot.send_message(event.chat_id, f"**Jawaban:**\n\n{msg2.message}")
            await ubot2.delete_messages(
                conv.chat_id, [msg_start.id, isi.id]
            )   
        except YouBlockedUserError:
            msg_start = await conv.send_message("/start")
            knyl = await conv.get_response()
            isi = await conv.send_message(f". {text}")
            msg1 = await conv.get_response()
            await ubot2.send_read_acknowledge(conv.chat_id)
            msg2 = await conv.get_response()
            await tbot.send_message(event.chat_id, f"**Jawaban:**\n\n{msg2.message}")
            await ubot2.delete_messages(
                conv.chat_id, [msg_start.id, isi.id]
            )           
    await mmk.delete()


@register(pattern="^Nanya ?(.*)")
async def tnya3(event):
    xxnx = event.pattern_match.group(1)
    reply_to_id = event.message.id
    anu = "Kamu naanyeaa???\n\nCara Penggunaane: nanya siapa pembuat telegram?"
    cepmek = "./GreyCilik/resources/nanya.mp3"
    if xxnx:
        text = xxnx
    elif event.is_reply:
        text = await event.get_reply_message()
    else:
        return await tbot.send_file(
            event.chat_id, "./GreyCilik/resources/nanya.mp3", voice_note=True, caption=anu, reply_to=reply_to_id
        )
    mmk = await event.reply("sini, biar aku kasih tau yahh...")
    chat = "@kecerdasanbuatan_robot"
    async with ubot2.conversation(chat) as conv:
        try:
            msg_start = await conv.send_message("/start")
            knyl = await conv.get_response()
            isi = await conv.send_message(f". {text}")
            msg1 = await conv.get_response()
            await ubot2.send_read_acknowledge(conv.chat_id)
            msg2 = await conv.get_response()
            await tbot.send_message(event.chat_id, f"**Jawaban:**\n\n{msg2.message}")
            await ubot2.delete_messages(
                conv.chat_id, [msg_start.id, isi.id]
            )   
        except YouBlockedUserError:
            msg_start = await conv.send_message("/start")
            knyl = await conv.get_response()
            isi = await conv.send_message(f". {text}")
            msg1 = await conv.get_response()
            await ubot2.send_read_acknowledge(conv.chat_id)
            msg2 = await conv.get_response()
            await tbot.send_message(event.chat_id, f"**Jawaban:**\n\n{msg2.message}")
            await ubot2.delete_messages(
                conv.chat_id, [msg_start.id, isi.id]
            )           
    await mmk.delete()


@register(pattern="^nanya ?(.*)")
async def tnya4(event):
    xxnx = event.pattern_match.group(1)
    reply_to_id = event.message.id
    anu = "Kamu naanyeaa???\n\nCara Penggunaan: nanya siapa pembuat telegram?"
    cepmek = "./GreyCilik/resources/nanya.mp3"
    if xxnx:
        text = xxnx
    elif event.is_reply:
        text = await event.get_reply_message()
    else:
        return await tbot.send_file(
            event.chat_id, "./GreyCilik/resources/nanya.mp3", voice_note=True, caption=anu, reply_to=reply_to_id
        )
    mmk = await event.reply("sini, biar aku kasih tau yahh...")
    chat = "@kecerdasanbuatan_robot"
    async with ubot2.conversation(chat) as conv:
        try:
            msg_start = await conv.send_message("/start")
            knyl = await conv.get_response()
            isi = await conv.send_message(f". {text}")
            msg1 = await conv.get_response()
            await ubot2.send_read_acknowledge(conv.chat_id)
            msg2 = await conv.get_response()
            await tbot.send_message(event.chat_id, f"**Jawaban:**\n\n{msg2.message}")
            await ubot2.delete_messages(
                conv.chat_id, [msg_start.id, isi.id]
            )   
        except YouBlockedUserError:
            msg_start = await conv.send_message("/start")
            knyl = await conv.get_response()
            isi = await conv.send_message(f". {text}")
            msg1 = await conv.get_response()
            await ubot2.send_read_acknowledge(conv.chat_id)
            msg2 = await conv.get_response()
            await tbot.send_message(event.chat_id, f"**Jawaban:**\n\n{msg2.message}")
            await ubot2.delete_messages(
                conv.chat_id, [msg_start.id, isi.id]
            )           
    await mmk.delete()
