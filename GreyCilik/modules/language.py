import itertools

from typing import Union, List, Generator

from collections.abc import Iterable
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton

import GreyCilik.modules.sql.language_sql as sql
from GreyCilik import dispatcher
from GreyCilik.modules.helper_funcs.chat_status import user_admin, user_admin_no_reply
from GreyCilik.language import get_string, get_languages, get_language


def paginate(iterable: Iterable, page_size: int) -> Generator[List, None, None]:
    while True:
        i1, i2 = itertools.tee(iterable)
        iterable, page = (
            itertools.islice(i1, page_size, None),
            list(itertools.islice(i2, page_size)),
        )
        if not page:
            break
        yield page


def gs(chat_id: Union[int, str], string: str) -> str:
    lang = sql.get_chat_lang(chat_id)
    return get_string(lang, string)


@user_admin
def set_lang(update: Update, _) -> None:
    chat = update.effective_chat
    msg = update.effective_message

    msg_text = gs(chat.id, "curr_chat_lang").format(
        get_language(sql.get_chat_lang(chat.id))[:-3]
    )

    keyb = [
        InlineKeyboardButton(
            text=name,
            callback_data=f"setLang_{code}",
        )
        for code, name in get_languages().items()
    ]
    keyb = list(paginate(keyb, 2))

    msg.reply_text(msg_text, reply_markup=InlineKeyboardMarkup(keyb))


@user_admin_no_reply
def lang_button(update: Update, _) -> None:
    query = update.callback_query
    chat = update.effective_chat

    query.answer()
    lang = query.data.split("_")[1]
    sql.set_lang(chat.id, lang)

    query.message.edit_text(
        gs(chat.id, "set_chat_lang").format(get_language(lang)[:-3]),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⬅️ Back",
                        callback_data=f"back_",
                    ),
                ]
            ],
        ),
    )


@user_admin
def back_button(update: Update, _) -> None:
    chat = update.effective_chat
    query = update.callback_query

    msg_text = gs(chat.id, "curr_chat_lang").format(
        get_language(sql.get_chat_lang(chat.id))[:-3]
    )

    keyb = [
        InlineKeyboardButton(
            text=name,
            callback_data=f"setLang_{code}",
        )
        for code, name in get_languages().items()
    ]
    keyb = list(paginate(keyb, 2))

    if query.data == "back_":
        query.message.edit_text(msg_text, reply_markup=InlineKeyboardMarkup(keyb))


# Langs For Pm

@user_admin
def pm_lang(update: Update, _) -> None:
    chat = update.effective_chat
    msg = update.effective_message

    msg_text = gs(chat.id, "curr_chat_lang").format(
        get_language(sql.get_chat_lang(chat.id))[:-3]
    )

    keyb = [
        InlineKeyboardButton(
            text=name,
            callback_data=f"pmsetLang_{code}",
        )
        for code, name in get_languages().items()
    ]
    keyb = list(paginate(keyb, 2))
    keyb.append(
        [
            InlineKeyboardButton(text=gs(chat.id, "buttonback_lang"), callback_data="cilik_back"
            )
        ]
    )


@user_admin_no_reply
def pm_lang_button(update: Update, _) -> None:
    query = update.callback_query
    chat = update.effective_chat

    query.answer()
    lang = query.data.split("_")[1]
    sql.set_lang(chat.id, lang)

    query.message.edit_text(
        gs(chat.id, "set_chat_lang").format(get_language(lang)[:-3]),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⬅️ Back",
                        callback_data=f"pmback_",
                    ),
                ]
            ],
        ),
    )

    
@user_admin
def pm_back_button(update: Update, _) -> None:
    chat = update.effective_chat
    query = update.callback_query

    msg_text = gs(chat.id, "curr_chat_lang").format(
        get_language(sql.get_chat_lang(chat.id))[:-3]
    )

    keyb = [
        InlineKeyboardButton(
            text=name,
            callback_data=f"pmsetLang_{code}",
        )
        for code, name in get_languages().items()
    ]
    keyb = list(paginate(keyb, 2))
    keyb.append(
        [
            InlineKeyboardButton(text=gs(chat.id, "buttonback_lang"), callback_data="cilik_back"
            )
        ]
    )
    if query.data == "pmback_":
        query.message.edit_text(msg_text, reply_markup=InlineKeyboardMarkup(keyb))    

        
def helps(chat):
    return gs(chat, "language_help")

SETLANG_HANDLER = CommandHandler("setlang", set_lang)
PM_SETLANG_HANDLER = CallbackQueryHandler(pm_lang, pattern=r"pm_setlang")
SETLANG_BUTTON_HANDLER = CallbackQueryHandler(lang_button, pattern=r"setLang_")
PM_SETLANG_BUTTON_HANDLER = CallbackQueryHandler(pm_lang_button, pattern=r"pmsetLang_")
BACK_BUTTON_HANDLER = CallbackQueryHandler(back_button, pattern=r"back_")
PM_BACK_BUTTON_HANDLER = CallbackQueryHandler(pm_back_button, pattern=r"pmback_")

dispatcher.add_handler(SETLANG_HANDLER)
dispatcher.add_handler(PM_SETLANG_HANDLER)
dispatcher.add_handler(SETLANG_BUTTON_HANDLER)
dispatcher.add_handler(PM_SETLANG_BUTTON_HANDLER)
dispatcher.add_handler(BACK_BUTTON_HANDLER)
dispatcher.add_handler(PM_BACK_BUTTON_HANDLER)

__mod_name__ = "Language"
