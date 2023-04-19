from GreyCilik import telethn as tbot, ubot2
from GreyCilik.events import register
from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import EditGroupCallTitleRequest as settitle
from telethon.tl.functions.phone import GetGroupCallRequest as getvc


async def get_call(event):
    mm = await event.ubot2(getchat(event.chat_id))
    xx = await event.ubot2(getvc(mm.full_chat.call, limit=1))
    return xx.call
  
  
@register(pattern="^/stopvc ?(.*)")
async def stop_voice(b):
    me = await b.client.get_me()
    chat = await b.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await b.reply(f"**Maaf {me.first_name} Bukan Admin 👮**")
        return
    try:
        await ubot2(stopvc(await get_call(b)))
        await b.reply("✅ __Voice Chat Stopped!__")
    except Exception as ex:
        await b.reply(f"**ERROR:** `{ex}`")
