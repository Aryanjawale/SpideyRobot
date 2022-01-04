
import json
import os

class Config(object):
    LOGGER = True
    
    API_ID = "4759912"  
    API_HASH = "5bcc548f108e30a913a339a4f97f315c"
    TOKEN = "5059068789:AAG1p9zixkDPEUZCjlKOz1g-OjPWaH1Xx0g"
    OWNER_ID = 1323719429  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "Aryanjawale"
    SUPPORT_CHAT = "trainer_zone"  
    JOIN_LOGGER = (
        -1001197394366
    )  
    EVENT_LOGS = (
        -1001197394366
    )  
    MESSAGE_DUMP = ( 
         -1001197394366 )

    
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:EhwlE3xkvmP7cIAQeAIS@containers-us-west-21.railway.app:6676/railway"
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    BOT_USERNAME = "@HawkMoth_rbot"
    SPAMWATCH_API = "M7r11AlyDZGvFh2F9U6umCS96iVvyMC~Bo9khw2cKMcYvRBYyDOUNJ7FLQqEEwgP"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    DRAGONS = get_user_list("elevated_users.json", "sudos")
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    DEMONS = get_user_list("elevated_users.json", "supports")
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    REM_BG_API_KEY = "dxsh728mZMDmj4ijSZCNPZig"
    GENIUS_API_TOKEN = "LstbAM4nzj2txUk2DGKh-PC0z6BxY1JYhMxMdj1NdRtmm7B7XYs0WcYBj4bFLK"
    MONGO_DB_URI = "mongodb://mongo:iFlA5trbE3FpYAdasgdP@containers-us-west-25.railway.app:6867"
    STRING_SESSION = "1BQANOTEuMTA4LjU2LjEzMAG7Y0dLVFQdbcP+HCrwb3LpkJeNtVWxbcndcHx24mQTDzjwAyqZ719yAwbJAomLHam9mYfViV2cA0Lfxao6mlOnnMBfJIE3ReEdUW+QlFC1LYp6k4prFaMVJZUzKpx2NCd1a7oeXNSQ9AHGzIIXcYCh5Yp2Y2/BE5T9R6z+tNKJ2bj8NCz/LGmLkzZeZmo+UKYO5liTd+gSLdXH5AyeO75dC4rbPAXV7jMsOauQq/c2p+BJBmWaI4C7fE2kp9TkBTOseZDviSxNEt0ADkXBJGw56Pa3L/bDNR9CHS6rn8V+JlY2N5/UXaspsPjFPwSFf5UQNQ1plx8PqNj2AGFYPnGn6Q=="
    STRICT_GMUTE = True
    BOT_USERNAME = "@HawkMoth_rbot"
    ARQ_API_URL = "https://thearq.tech/" 
    BOT_NAME = "HᴀᴡᴋMᴏᴛʜ"
    ARQ_API_KEY = "CEWQIX-PODJTL-RNSXWN-GBRPKV-ARQ"
    LOG_GROUP_ID = "-1001197394366"
    OPENWEATHERMAP_ID = "e8c43576833a8867d24a4e6785349e20"
    TEMP_DOWNLOAD_DIRECTORY = "./"
    ERROR_LOGS = "-1001197394366"
    LASTFM_API_KEY = "73d42d9c93626709dc2679d491d472bf"
    BOT_ID = "5059068789"
    WELCOME_DELAY_KICK_SEC = "5"
    REDIS_URL = "redis://Zaidrobot:Anmol@123@redis-12356.c284.us-east1-2.gce.cloud.redislabs.com:12356/Zaidrobot"
    
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = "CAADBQAD6QQAAsMSmVU8Rp977RgWBQI"  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True
    ALLOW_CHATS = True  
    CASH_API_KEY = (
        "V7NS1NBFEL4X24L6"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "2AS711XS1O9B"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "awoo"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None # .


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
