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

    API_ID = 9292497  # integer value, dont use "
    API_HASH = "7ba6bfc601e9e6f384b2b449f11cc645"
    MONGO_DB_URI = "mongodb+srv://greycilik:greycilik@cluster0.uxabg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    STRING_SESSION = "1BVtsOGkBu66uR-ZyOP5VQtTYbF00fT8_rijF3tIqP9CIS7taYsz96qwSREAUppGEeslHTYN4jvZrFAg4ioFvirBfojQP5CRuiDAypL7hBHU8jkmE9q4CIvOBkQZMaT98T_O7hP8x3pnI5MHf_YlhMBsBMxm-4CaxCvNqqZDhXYj-J9lBxxtWedhxQp_Tv2ErHfG4wYBu86RwyDqArlO-7GazjXMjg4qfzcnTeuHg8qpBc0FTxdtBl_cW_P4MGp4F9N1FS-6QYyj2hswVn1NqG-6Qo-cXzSJ-wFR7afneMyDxXSKPOpi3rr8zOHlvvS-o8lcIsjw2XhFWk1PwP9ssyOBm9CeBS6w="
    SESSION_STRING = "1BVtsOJgBu1Jx-tpbU3jDbHlxo1TQxSikl0ZUXTni8Nd42VVuSCnnI3Oy2e9XeB2rRAcTbXL8-fwjc_sPV9vQgswyskQgJQ1r7whEFXRuZA97XVYhfD24ifCo4X-Jr6BYFJumSUoGj77A53VMEHD_A_jfXFENEAx5DwCCly9xo4XV5LkkvO3reogfP1qafoJD5adehjE-lHP1U8_q8hI20qfTV2XZHeVjOZC5xOPBWNsYDkAcTRXagsktk5aPnUAbfrq-ClNC12-fWSd0HDHxNAR0FTGJIpagHa777LZkuaWOPkf58tm-QKYr9P-tKpIgYZeNYDn9882L6E_BEHwlFROQzmSYxvc="
    TOKEN = "6149489784:AAFanDmLMl3tU3g3fWoWA-p1D9koUS7wFhw"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1696803773  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "berisikjeleg"
    DB_URL = "postgresql://ajgqajge:RyVELQQ2_RdhhaSUdH4Z-Dx7kxyj0DVZ@ruby.db.elephantsql.com/ajgqajge"
    SUPPORT_CHAT = "meliodassupoort"  # Your own group for support, do not add the @
    ERROR_LOG = (
        -1001854573739
    )
    JOIN_LOGGER = (
        -1001814648622
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001854573739
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
    ARQ_API_KEY = "LIVLGP-KEGPBF-TFJNIC-WMLSEJ-ARQ"
    ARQ_API_URL = "https://arq.hamker.in"
    TEMP_DOWNLOAD_DIRECTORY = "Downloads"
    OPENWEATHERMAP_ID = ""
    REM_BG_API_KEY = ""
    BOT_USERNAME = "meliodaskunrobot"
    LASTFM_API_KEY = ""
    CF_API_KEY = ""
    BOT_ID = "6149489784"
    

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
