from GreyCilik import dispatcher
from GreyCilik.modules.disable import DisableAbleCommandHandler
from GreyCilik.modules.helper_funcs.alternate import typing_action
from GreyCilik.modules.language import gs
from telegram import ParseMode
from telegram.ext import run_async

normiefont = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
]
f1font = [
    "卂", "乃", "匚", "刀", "乇", "下", "厶", "卄", "工", "丁", "长", "乚", "从", "𠘨", "口", "尸", "㔿", "尺", "丂", "丅", "凵", "リ", "山", "乂", "丫", "乙",
]
f2font = [
    "ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ", "ⓕ", "ⓖ", "ⓗ", "ⓘ", "ⓙ", "ⓚ", "ⓛ", "ⓜ", "ⓝ", "ⓞ", "ⓟ", "ⓠ", "ⓡ", "ⓢ", "ⓣ", "ⓤ", "ⓥ", "ⓦ", "ⓧ", "ⓨ", "ⓩ",
]
f3font = [
    "🅐", "🅑", "🅒", "🅓", "🅔", "🅕", "🅖", "🅗", "🅘", "🅙", "🅚", "🅛", "🅜", "🅝", "🅞", "🅟", "🅠", "🅡", "🅢", "🅣", "🅤", "🅥", "🅦", "🅧", "🅨", "🅩",
]
f4font = [
    "🄰", "🄱", "🄲", "🄳", "🄴", "🄵", "🄶", "🄷", "🄸", "🄹", "🄺", "🄻", "🄼", "🄽", "🄾", "🄿", "🅀", "🅁", "🅂", "🅃", "🅄", "🅅", "🅆", "🅇", "🅈", "🅉",
]
f5font = [
    "🅰", "🅱", "🅲", "🅳", "🅴", "🅵", "🅶", "🅷", "🅸", "🅹", "🅺", "🅻", "🅼", "🅽", "🅾", "🅿", "🆀", "🆁", "🆂", "🆃", "🆄", "🆅", "🆆", "🆇", "🆈", "🆉",
]
f6font = [
    "🇦 ", "🇧 ", "🇨 ", "🇩 ", "🇪 ", "🇫 ", "🇬 ", "🇭 ", "🇮 ", "🇯 ", "🇰 ", "🇱 ", "🇲 ", "🇳 ", "🇴 ", "🇵 ", "🇶 " ,"🇷 ", "🇸 ", "🇹 ", "🇺 ", "🇻 ", "🇼 ", "🇽 ", "🇾 ", "🇿 ",
]
f7font = [
    "𝒶", "𝒷", "𝒸", "𝒹", "ℯ", "𝒻", "ℊ", "𝒽", "𝒾", "𝒿", "𝓀", "𝓁", "𝓂", "𝓃", "ℴ", "𝓅", "𝓆", "𝓇", "𝓈", "𝓉", "𝓊", "𝓋", "𝓌", "𝓍", "𝓎", "𝓏",
]
f8font = [
    "𝕒", "𝕓", "𝕔", "𝕕", "𝕖", "𝕗", "𝕘", "𝕙", "𝕚", "𝕛", "𝕜", "𝕝", "𝕞", "𝕟", "𝕠", "𝕡", "𝕢", "𝕣", "𝕤", "𝕥", "𝕦", "𝕧", "𝕨", "𝕩", "𝕪", "𝕫",
]

f9font = [
    "ᴀ", "ʙ", "ᴄ", "ᴅ", "ᴇ", "ꜰ", "ɢ", "ʜ", "ɪ", "ᴊ", "ᴋ", "ʟ", "ᴍ", "ɴ", "ᴏ", "ᴘ", "Q", "ʀ", "ꜱ", "ᴛ", "ᴜ", "ᴠ", "ᴡ", "x", "ʏ", "ᴢ",
]

f10font = [
    "𝐀", "𝐁", "𝐂", "𝐃", "𝐄", "𝐅", "𝐆", "𝐇", "𝐈", "𝐉", "𝐊", "𝐋", "𝐌", "𝐍", "𝐎", "𝐏", "𝐐", "𝐑", "𝐒", "𝐓", "𝐔", "𝐕", "𝐖", "𝐗", "𝐘", "𝐙",
]

f11font = [
    "𝗔", "𝗕", "𝗖", "𝗗", "𝗘", "𝗙", "𝗚", "𝗛", "𝗜", "𝗝", "𝗞", "𝗟", "𝗠", "𝗡", "𝗢", "𝗣", "𝗤", "𝗥", "𝗦", "𝗧", "𝗨", "𝗩", "𝗪", "𝗫", "𝗬", "𝗭",
]    


@typing_action
def f1(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/f1 <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            f1character = f1font[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, f1character)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


@typing_action
def f2(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/f2 <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            f2character = f2font[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, f2character)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


@typing_action
def f3(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/f3 <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            f3character = f3font[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, f3character)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


@typing_action
def f4(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/f4 <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            f4character = f4font[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, f4character)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


@typing_action
def f5(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/f5 <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            f5character = f5font[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, f5character)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


@typing_action
def f6(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/f6 <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            f6character = f6font[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, f6character)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


@typing_action
def f7(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/f7 <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            f7character = f7font[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, f7character)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


@typing_action
def f8(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/f8 <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            f8character = f8font[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, f8character)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)
        

@typing_action
def f9(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/f9 <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            f9character = f9font[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, f9character)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)

        
@typing_action
def f10(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/f10 <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            f10character = f10font[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, f10character)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)     

        
def helps(chat):
    return gs(chat, "misc_help")

        
__mod_name__ = "Misc"

F1_HANDLER = DisableAbleCommandHandler("f1", f1, run_async=True)
F2_HANDLER = DisableAbleCommandHandler("f2", f2, run_async=True)
F3_HANDLER = DisableAbleCommandHandler("f3", f3, run_async=True)
F4_HANDLER = DisableAbleCommandHandler("f4", f4, run_async=True)
F5_HANDLER = DisableAbleCommandHandler("f5", f5, run_async=True)
F6_HANDLER = DisableAbleCommandHandler("f6", f6, run_async=True)
F7_HANDLER = DisableAbleCommandHandler("f7", f7, run_async=True)
F8_HANDLER = DisableAbleCommandHandler("f8", f8, run_async=True)
F9_HANDLER = DisableAbleCommandHandler("f9", f9, run_async=True)
F10_HANDLER = DisableAbleCommandHandler("f10", f10, run_async=True)
dispatcher.add_handler(F1_HANDLER)
dispatcher.add_handler(F2_HANDLER)
dispatcher.add_handler(F3_HANDLER)
dispatcher.add_handler(F4_HANDLER)
dispatcher.add_handler(F5_HANDLER)
dispatcher.add_handler(F6_HANDLER)
dispatcher.add_handler(F7_HANDLER)
dispatcher.add_handler(F8_HANDLER)
dispatcher.add_handler(F9_HANDLER)
dispatcher.add_handler(F10_HANDLER)

__command_list__ = ["f1"]
__command_list__ = ["f2"]
__command_list__ = ["f3"]
__command_list__ = ["f4"]
__command_list__ = ["f5"]
__command_list__ = ["f6"]
__command_list__ = ["f7"]
__command_list__ = ["f8"]
__command_list__ = ["f9"]
__command_list__ = ["f10"]
__handlers__ = [F1_HANDLER]
__handlers__ = [F2_HANDLER]
__handlers__ = [F3_HANDLER]
__handlers__ = [F4_HANDLER]
__handlers__ = [F5_HANDLER]
__handlers__ = [F6_HANDLER]
__handlers__ = [F7_HANDLER]
__handlers__ = [F8_HANDLER]
__handlers__ = [F9_HANDLER]
__handlers__ = [F10_HANDLER]
