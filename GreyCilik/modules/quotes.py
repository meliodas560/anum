from os import remove
from random import choice
from telethon import events, Button
from telethon.tl.functions.users import GetFullUserRequest
from GreyCilik.events import register
from GreyCilik import telethn
from GreyCilik.utils.quotlyfunc import create_quotly



HELP = """
💭 **QUOTLY HELP**

» /q <reply to message>
» /q <color> - color : [black, white, red, blue, yellow, green, grey, brown, pink, purple]
» /q @username - example : /q @greyybss handsome or /q @greyyvbss <reply to message>
"""



@register(pattern="^/helpquotly ?(.*)")
async def quotly_help(event):
    await event.reply(f"{HELP}")
    
    
ERRORS = []
qr = {}


@telethn.on(events.CallbackQuery(pattern="upq_(.*)"))
async def quotly_upvote(e):
    d = e.pattern_match.group(1).decode()
    x, y, z = d.split("|")
    x, y, z = int(x), int(y), int(z)
    try:
        ya = qr[x]
    except IndexError:
        await e.edit(buttons=None)
    if e.sender_id in ya[0]:
        y -= 1
        qr[x][0].remove(e.sender_id)
        await e.answer("you got your vote back")
    elif e.sender_id in ya[1]:
        y += 1
        z -= 1
        qr[x][1].remove(e.sender_id)
        qr[x][0].append(e.sender_id)
        await e.answer("you 👍 this")
    elif e.sender_id not in ya[0]:
        y += 1
        qr[x][0].append(e.sender_id)
        await e.answer("you 👍 this")
    cd = "{}|{}|{}".format(x, y, z)
    if y == 0:
        y = ""
    if z == 0:
        z = ""
    await e.edit(
        buttons=[
            Button.inline(f"👍 {y}", data=f"upq_{cd}"),
            Button.inline(f"👎 {z}", data=f"doq_{cd}"),
        ]
    )


@telethn.on(events.CallbackQuery(pattern="doq_(.*)"))
async def quotly_downvote(e):
    d = e.pattern_match.group(1).decode()
    x, y, z = d.split("|")
    x, y, z = int(x), int(y), int(z)
    try:
        ya = qr[x]
    except IndexError:
        await e.edit(buttons=None)
    if e.sender_id in ya[1]:
        z -= 1
        qr[x][1].remove(e.sender_id)
        await e.answer("you got your vote back")
    elif e.sender_id in ya[0]:
        z += 1
        y -= 1
        qr[x][0].remove(e.sender_id)
        qr[x][1].append(e.sender_id)
        await e.answer("you 👎 this")
    elif e.sender_id not in ya[1]:
        z += 1
        qr[x][1].append(e.sender_id)
        await e.answer("you 👎 this")
    cd = "{}|{}|{}".format(x, y, z)
    if y == 0:
        y = ""
    if z == 0:
        z = ""
    await e.edit(
        buttons=[
            Button.inline(f"👍 {y}", data=f"upq_{cd}"),
            Button.inline(f"👎 {z}", data=f"doq_{cd}"),
        ]
    )


@register(pattern="^/q ?(.*)")
async def quotly(event):
    match = event.pattern_match.group(1).strip()
    if not event.is_reply:
        return
    reply = await event.get_reply_message()
    replied_to, reply_ = None, None
    if match:
        spli_ = match.split(maxsplit=1)
        if (spli_[0] in ["r", "reply"]) or (
            spli_[0].isdigit() and int(spli_[0]) in range(1, 21)
        ):
            if spli_[0].isdigit():
                if not event.client._bot:
                    reply_ = await event.client.get_messages(
                        event.chat_id,
                        min_id=event.reply_to_msg_id - 1,
                        reverse=True,
                        limit=int(spli_[0]),
                    )
                else:
                    id_ = reply.id
                    reply_ = []
                    for msg_ in range(id_, id_ + int(spli_[0])):
                        msh = await event.client.get_messages(event.chat_id, ids=msg_)
                        if msh:
                            reply_.append(msh)
            else:
                replied_to = await reply.get_reply_message()
            try:
                match = spli_[1]
            except IndexError:
                match = None
    user = None
    if not reply_:
        reply_ = reply
    if match:
        match = match.split(maxsplit=1)
    if match:
        if match[0].startswith("@") or match[0].isdigit():
            try:
                match_ = await event.client(GetFullUserRequest(match[0]))
                user = await event.client.get_entity(match_)
            except ValueError:
                pass
            match = match[1] if len(match) == 2 else None
        else:
            match = match[0]
    if match == "random":
        match = choice(all_col)
    try:
        file = await create_quotly(reply_, bg=match, reply=replied_to, sender=user)
    except Exception as er:
        return await event.reply(f"ERROR: {er}")
    cd = str(event.id) + "|" + str(0) + "|" + str(0)
    btn = Button.inline("👍", data=f"upq_{cd}"), Button.inline(
        "👎", data=f"doq_{cd}"
    )
    qr[event.id] = [[], []]
    message = await event.reply(file=file, buttons=btn)
    remove(file)
    return message

__mod_name__ = "Quotly"
