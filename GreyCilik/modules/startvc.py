from GreyCilik import telethn as tbot, ubot2
from GreyCilik.events import register
from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import EditGroupCallTitleRequest as settitle
from telethon.tl.functions.phone import GetGroupCallRequest as getvc

@register(pattern="^/startvc ?(.*)")
async def start_voice(c):
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await c.reply(f"**Maaf {me.first_name} Bukan Admin 👮**")
        return
    try:
        await ubot2(startvc(c.chat_id))
        await c.reply("✅ __Voice Chat Started!__")
    except Exception as ex:
        await c.reply(f"**ERROR:** `{ex}`")
