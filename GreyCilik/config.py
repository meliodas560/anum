# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/GreyCilik/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 17830773  # integer value, dont use "
    API_HASH = "7253db2e173b6b24aefc507f9f860366"
    MONGO_DB_URI = "mongodb+srv://greycilik:greycilik@cluster0.uxabg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    STRING_SESSION = "1BVtsOHsBu6vg3_mJAS6bnHqsxjXTjR18we_vONyWua_6qmuTGB5jWV9huF9QwUah6Xqdn2O6f-rpJp3m6Mz2_bP2Bs70PnPqefLE8PG4tja2hT2Qfwf88ZBXqdRYlrj2yNGBhdA6B52ifxRh6mKsfjb-cJ-mBfp8kehNmRr4-7TqOIvg8gorlsMxAbCe03zgw9gvv6CSrdqY7-tCy84hnity-l4DA0cx3_APc-rVGZM00lPw104O4tgT5fJyXyvukswBoQyVIABWAALEzaUN-hDZQ6hmIK7CSqYThoaDrRyjKVtNAU2pEmH6TsFqaVghRTlkYw7DBqrLzZWW9BHmFFm2UK97E1w="
    SESSION_STRING = "1BVtsOHsBu6vg3_mJAS6bnHqsxjXTjR18we_vONyWua_6qmuTGB5jWV9huF9QwUah6Xqdn2O6f-rpJp3m6Mz2_bP2Bs70PnPqefLE8PG4tja2hT2Qfwf88ZBXqdRYlrj2yNGBhdA6B52ifxRh6mKsfjb-cJ-mBfp8kehNmRr4-7TqOIvg8gorlsMxAbCe03zgw9gvv6CSrdqY7-tCy84hnity-l4DA0cx3_APc-rVGZM00lPw104O4tgT5fJyXyvukswBoQyVIABWAALEzaUN-hDZQ6hmIK7CSqYThoaDrRyjKVtNAU2pEmH6TsFqaVghRTlkYw7DBqrLzZWW9BHmFFm2UK97E1w="
    TOKEN = "5094084246:AAGBc12Zxe85p91viNPZUfEQ2mg7OzBDEHE"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1784606556  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "greyyvbss"
    DB_URL = "postgresql://ajgqajge:RyVELQQ2_RdhhaSUdH4Z-Dx7kxyj0DVZ@ruby.db.elephantsql.com/ajgqajge"
    SUPPORT_CHAT = "CilikSupport"  # Your own group for support, do not add the @
    ERROR_LOG = (
        -1001692951846
    )
    JOIN_LOGGER = (
        -1001692951846
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001692951846
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgresql://ajgqajge:RyVELQQ2_RdhhaSUdH4Z-Dx7kxyj0DVZ@ruby.db.elephantsql.com/ajgqajge"  # needed for any database modules
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = ""  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"
    ARQ_API_KEY = "QATNJK-ANMJGT-EZUTWM-TOZGVA-ARQ"
    ARQ_API_URL = "https://arq.hamker.in"
    TEMP_DOWNLOAD_DIRECTORY = "Downloads"
    OPENWEATHERMAP_ID = ""
    REM_BG_API_KEY = "LBGDKdK5tqN6UW26KGoQkKsQ"
    BOT_USERNAME = "GreyCilik_bot"
    LASTFM_API_KEY = ""
    CF_API_KEY = ""
    BOT_ID = "5094084246"
    

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    STRICT_GBAN = True
    ALLOW_CHATS = True
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "awoo"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "awoo"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "awoo"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
