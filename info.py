import re
import os
from os import environ, getenv
from Script import script

# Utility functions
id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# ============================
# Bot Information Configuration
# ============================
SESSION = environ.get('SESSION', 'royal_search')   # Session name for the bot
API_ID = int(environ.get('API_ID', '')) # API ID from my.telegram.org
API_HASH = environ.get('API_HASH', '')  # API Hash from my.telegram.org
BOT_TOKEN = environ.get('BOT_TOKEN', "")    # Bot token from @BotFather

# ============================
# Bot Settings Configuration
# ============================
CACHE_TIME = int(environ.get('CACHE_TIME', 300))    # Cache time in seconds (default: 5 minutes)
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))  # Use caption filter for search results (default: True)
INDEX_CAPTION = bool(environ.get('SAVE_CAPTION', True)) # Save caption db when idexing make it False if you dont use USE_CAPTION_FILTER for search results (default: True)
#Making it false will not save caption in db SO you can save some storage space


PICS = (environ.get('PICS', 'dreamxbotz/template/logo.png')).split()  # Sample pic
NOR_IMG = environ.get("NOR_IMG", "dreamxbotz/template/logo.png")
MELCOW_PHOTO = environ.get("MELCOW_PHOTO", "dreamxbotz/template/logo.png")
SPELL_IMG = environ.get("SPELL_IMG", "dreamxbotz/template/logo.png")
SUBSCRIPTION = (environ.get('SUBSCRIPTION', 'dreamxbotz/template/logo.png'))
FSUB_PICS = (environ.get('FSUB_PICS', 'dreamxbotz/template/logo.png')).split()  # Fsub pic

# ============================
# Admin, Channels & Users Configuration
# ============================
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()] # Replace with the actual admin ID(s) to add
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-100').split()]  # Channel id for auto indexing (make sure bot is admin)

LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-100'))  # Log channel id (make sure bot is admin)
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', '-100'))  # Bin channel id (make sure bot is admin)
PREMIUM_LOGS = int(environ.get('PREMIUM_LOGS', '-100'))  # Premium logs channel id
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '-100').split()] #(make sure bot is admin)
support_chat_id = environ.get('SUPPORT_CHAT_ID', '-100')  # Support group id (make sure bot is admin)
reqst_channel = environ.get('REQST_CHANNEL_ID', '-100')  # Request channel id (make sure bot is admin)
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/')  # Support group link (make sure bot is admin)

# FORCE_SUB 
auth_req_channels = environ.get("AUTH_REQ_CHANNELS", "-100")# requst to join Channel for force sub (make sure bot is admin) only for bot ADMINS  
auth_channels     = environ.get("AUTH_CHANNELS", "-100")# Channels for force sub (make sure bot is admin)

# ============================
# Payment Configuration
# ============================
QR_CODE = environ.get('QR_CODE', 'Your_Qr_Code')    # QR code image for payments
OWNER_UPI_ID = environ.get('OWNER_UPI_ID', 'ɴᴏ ᴀᴠᴀɪʟᴀʙʟᴇ ʀɪɢʜᴛ ɴᴏᴡ')    # Owner UPI ID for payments

STAR_PREMIUM_PLANS = {
    20:  "7day",
    40:  "15day",
    80:  "1month",
    110: "45day",
    130: "60day",
}  # Star amounts matching INR plan prices (20₹=20⭐, 40₹=40⭐, etc.)

# ============================
# MongoDB Configuration
# ============================
DATABASE_URI = environ.get('DATABASE_URI', "")  # MongoDB URI for the database
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0") # Database name (default: cluster)
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'royal_files') # Collection name (default: dreamcinezone_files)

# ============================
# Multi-Database Configuration (Up to 5 MongoDB DBs)
# ============================
MULTIPLE_DB   = is_enabled(os.environ.get('MULTIPLE_DB', "False"), False)  # Set True to enable multi-DB
DB_SIZE_LIMIT  = int(os.environ.get('DB_SIZE_LIMIT', 480))  # MB — switch to next DB when this limit is reached

DATABASE_URI2  = environ.get('DATABASE_URI2', "")   # 2nd MongoDB URI
DATABASE_URI3  = environ.get('DATABASE_URI3', "")   # 3rd MongoDB URI
DATABASE_URI4  = environ.get('DATABASE_URI4', "")   # 4th MongoDB URI
DATABASE_URI5  = environ.get('DATABASE_URI5', "")   # 5th MongoDB URI

DATABASE_NAME2 = environ.get('DATABASE_NAME2', DATABASE_NAME)  # 2nd DB name (defaults to same)
DATABASE_NAME3 = environ.get('DATABASE_NAME3', DATABASE_NAME)  # 3rd DB name
DATABASE_NAME4 = environ.get('DATABASE_NAME4', DATABASE_NAME)  # 4th DB name
DATABASE_NAME5 = environ.get('DATABASE_NAME5', DATABASE_NAME)  # 5th DB name
# ============================
# Movie Notification & Update Settings
# ============================
MOVIE_UPDATE_NOTIFICATION = bool(environ.get('MOVIE_UPDATE_NOTIFICATION', False))  # Notification On (True) / Off (False)
MOVIE_UPDATE_CHANNEL = int(environ.get('MOVIE_UPDATE_CHANNEL', '-100'))  # Notification of sent to your channel
DREAMXBOTZ_IMAGE_FETCH = bool(environ.get('DREAMXBOTZ_IMAGE_FETCH', True))  # On (True) / Off (False)
LINK_PREVIEW = bool(environ.get('LINK_PREVIEW', False)) # Shows link preview in notification msg instead of image
ABOVE_PREVIEW = bool(environ.get('ABOVE_PREVIEW', True)) # Shows link preview above the text in notification msg if True else below the msg
TMDB_API_KEY = environ.get('TMDB_API_KEY', '') # preffer to use your own tmdb API Key get it from https://www.themoviedb.org/settings/api
TMDB_POSTER = bool(environ.get('TMDB_POSTER', False)) # Shows TMDB poster in notification msg
LANDSCAPE_POSTER = bool(environ.get('LANDSCAPE_POSTER', True)) # Shows landscape poster in notification msg

# ============================
# Verification Settings
# ============================
IS_VERIFY = is_enabled(environ.get('IS_VERIFY', 'True'), True)  # Verification On (True) / Off (False)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-100')) #Verification Channel Id 
VERIFY_IMG = environ.get("VERIFY_IMG", "dreamxbotz/template/logo.png")

TUTORIAL = environ.get("TUTORIAL", "https://t.me/Univora88")   # Tutorial link for verification
TUTORIAL_2 = environ.get("TUTORIAL_2", "https://t.me/Univora88")   # Second tutorial link for verification
TUTORIAL_3 = environ.get("TUTORIAL_3", "https://t.me/Univora88")   # Third tutorial link for verification

# Verification (Must Fill All Veriables. Else You Got Error
SHORTENER_API = environ.get("SHORTENER_API", "5b103993ce54abbcd87855592ee7591f6b89ce12") # Shortener API key
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "vplink.in") # Shortener website

SHORTENER_API2 = environ.get("SHORTENER_API2", "yei5ei5eie6id6d")  # Shortener API key for second website
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "Shortner_Website_Url") # Shortener website for second website

SHORTENER_API3 = environ.get("SHORTENER_API3", "5353e68e866ee")  
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", "Shortner_Website_Url") # Shortener website for third website

TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "1200")) # Time gap for two-step verification in seconds (default: 20 minutes)
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "54000"))    

# ============================
# Channel & Group Links Configuration
# ============================
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/Univora88') # Group link for the bot
OWNER_LNK = environ.get('OWNER_LNK', 'https://t.me/rolexsir_8') # Owner link for the bot
UPDATE_CHNL_LNK = environ.get('UPDATE_CHNL_LNK', 'https://t.me/Univora88') # Update channel link for the bot

# ============================
# User Configuration
# ============================
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
PREMIUM_USER = [int(user) if id_pattern.search(user) else user for user in environ.get('PREMIUM_USER', '').split()]

# ============================
# Miscellaneous Configuration
# ============================
ULTRA_FAST_MODE = is_enabled(environ.get('ULTRA_FAST_MODE', "False"), True) # Set to True for fast search, False for original search

MAX_B_TN = environ.get("MAX_B_TN", "5") # Maximum number of buttons in a row (default: 5)
PORT = int(environ.get("PORT", "8080"))  # Port for the web server (default: 8080)
MSG_ALRT = environ.get('MSG_ALRT', 'Share & Support Us ♥️') # Alert message for users
DELETE_TIME = int(environ.get("DELETE_TIME", "300"))  #  deletion time in seconds (default: 5 minutes). Adjust as per your needs.
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")   # Custom caption for files
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION) # Custom caption for batch files
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")     # Custom IMDB template 
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None) # Maximum number of elements in a list (default: None, no limit)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))  # Index Request Channel ID (make sure bot is admin)
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", True))  # True if you want no results messages in Log Channel
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)    # Max Button On (True) / Off (False)
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)    # P_TTI_SHOW_OFF On (True) / Off (False)
IMDB = is_enabled((environ.get('IMDB', "False")), False)    # IMDB Results On (True) / Off (False)
TMDB_ON_SEARCH = is_enabled((environ.get('TMDB_ON_SEARCH', "False")), False)    # Use TMDB Poster On Search Results
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True) # Auto Filter On (True) / Off (False)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True) # Auto Delete On (True) / Off (False)
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False) # Long IMDB Description On (True) / Off (False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True) # Spell Check Mode On (True) / Off (False)
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), False) # Melcow New Users On (True) / Off (False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False) # Protect Content On (True) / Off (False)
PM_SEARCH = bool(environ.get('PM_SEARCH', True))  # PM Search On (True) / Off (False)
EMOJI_MODE = bool(environ.get('EMOJI_MODE', False))  # Emoji status On (True) / Off (False)
BUTTON_MODE = is_enabled((environ.get('BUTTON_MODE', "False")), False) # pm & Group button or link mode (True) / Off (False)
STREAM_MODE = is_enabled(environ.get('STREAM_MODE', 'False'), False)  # Enable stream/download link button
PREMIUM_STREAM_MODE = is_enabled(environ.get('PREMIUM_STREAM_MODE', 'False'), False)  # Stream only for premium users


# ============================
# Bot Configuration
# ============================

AUTH_REQ_CHANNELS = [int(ch) for ch in auth_req_channels.split() if ch and id_pattern.match(ch)] 
AUTH_CHANNELS = [int(ch) for ch in auth_channels.split() if ch and id_pattern.match(ch)]
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
LANGUAGES = {"ᴍᴀʟᴀʏᴀʟᴀᴍ":"mal","ᴛᴀᴍɪʟ":"tam","ᴇɴɢʟɪsʜ":"eng","ʜɪɴᴅɪ":"hin","ᴛᴇʟᴜɢᴜ":"tel","ᴋᴀɴɴᴀᴅᴀ":"kan","ɢᴜᴊᴀʀᴀᴛɪ":"guj","ᴍᴀʀᴀᴛʜɪ":"mar","ᴘᴜɴᴊᴀʙɪ":"pun"}
QUALITIES = ["360P", "480P", "720P", "1080P", "1440P", "2160P", "4K"]

SEASON_COUNT = 12
SEASONS = [f"S{str(i).zfill(2)}" for i in range(1, SEASON_COUNT + 1)]

BAD_WORDS = {
    "PrivateMovieZ",
    "toonworld4all",
    "themoviesboss",
    "1tamilmv",
    "tamilblasters",
    "1tamilblasters",
    "skymovieshd",
    "extraflix",
    "hdm2",
    "moviesmod",
    "hdhub4u",
    "mkvcinemas",
    "primefix",
    "join",
    "www",
    "villa",
    "tg",
    "original"
} # Set of bad words to filter out
   

# ============================
# Server & Web Configuration
# ============================

NO_PORT = bool(environ.get('NO_PORT', False))
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = environ.get('APP_NAME')
else:
    ON_HEROKU = False
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else "https://{}/".format(FQDN, PORT)
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
WORKERS = int(environ.get('WORKERS', '4'))
SESSION_NAME = str(environ.get('SESSION_NAME', 'dreamXBotz'))
MULTI_CLIENT = False
name = str(environ.get('name', 'DREAMXBOTZ'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME'))
else:
    ON_HEROKU = False
HAS_SSL = is_enabled(getenv('HAS_SSL', 'True'), True)
if HAS_SSL:
    URL = "https://{}/".format(FQDN)
else:
    URL = "http://{}/".format(FQDN)

# ============================
# Reactions Configuration
# ============================
REACTIONS = ["🤝", "😇", "🤗", "😍", "👍", "🎅", "😐", "🥰", "🤩", "😱", "🤣", "😘", "👏", "😛", "😈", "🎉", "⚡️", "🫡", "🤓", "😎", "🏆", "🔥", "🤭", "🌚", "🆒", "👻", "😁"]

# ============================
# Commands Bot
# ============================
Bot_cmds = {
    "start": "Sᴛᴀʀᴛ Mᴇ Bᴀʙʏ",
    "alive": " Cʜᴇᴄᴋ Bᴏᴛ Aʟɪᴠᴇ ᴏʀ Nᴏᴛ ",
    "settings": "ᴄʜᴀɴɢᴇ sᴇᴛᴛɪɴɢs",
    "id": "ɢᴇᴛ ɪᴅ ᴛᴇʟᴇɢʀᴀᴍ ",
    "info": "Gᴇᴛ Usᴇʀ ɪɴғᴏ ",
    "trendlist": "Gᴇᴛ Tᴏᴘ Tʀᴀɴᴅɪɴɢ Sᴇᴀʀᴄʜ Lɪsᴛ",
    "group_cmd": "ɢʀᴏᴜᴘ ᴄᴏᴍᴍᴀɴᴅ ʟɪsᴛ"
}

Admin_cmds = {
    "stats": "Gᴇᴛ Bᴏᴛ Sᴛᴀᴛs",
    "glist": "Sᴀʙ ɢʀᴏᴜᴘs ᴋɪ ʟɪsᴛ ᴀᴜʀ ᴘᴀɴᴇʟ",
    "ginfo": "Sᴘᴇᴄɪғɪᴄ ɢʀᴏᴜᴘ ᴄᴏɴᴛʀᴏʟ ᴘᴀɴᴇʟ",
    "gverify": "Gʀᴏᴜᴘ Vᴇʀɪғʏ ᴏɴ/ᴏғғ ᴛᴏɢɢʟᴇ",
    "gban": "Gʀᴏᴜᴘ ᴋᴏ ʙᴀɴ ᴋᴀʀᴏ",
    "gunban": "Gʀᴏᴜᴘ ᴋᴏ ᴜɴʙᴀɴ ᴋᴀʀᴏ",
    "gleave": "Bᴏᴛ ᴋᴏ ғᴏʀᴄᴇ ʟᴇᴀᴠᴇ ᴋᴀʀᴡᴀᴏ",
    "greset": "Gʀᴏᴜᴘ sᴇᴛᴛɪɴɢs ʀᴇsᴇᴛ ᴋᴀʀᴏ",
    "gall": "Sᴀʙ ɢʀᴏᴜᴘs ʀᴀᴡ ɪᴅ ʟɪsᴛ",
    "broadcast": "ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀꜱ.",
    "grp_broadcast": "ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘs",
    "del_msg": "ʀᴇᴍᴏᴠᴇ ғɪʟᴇ ɴᴀᴍᴇ ᴄᴏʟʟᴇᴄᴛɪᴏɴ ɴᴏтɪғɪᴄᴀᴛɪᴏɴ...",
    "movie_update": "ᴏɴ ᴏғғ ᴀᴄᴄᴏʀᴅɪɴɢ ʏᴏᴜʀ ɴᴇᴇᴅᴇᴅ...",
    "pm_search": "ᴘᴍ sᴇᴀʀᴄʜ ᴏɴ ᴏғғ ᴀᴄᴄᴏʀᴅɪɴɢ ʏᴏᴜʀ ɴᴇᴇᴅᴇᴅ...",
    "send": "ꜱᴇɴᴅ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴜꜱᴇʀ.",
    "add_premium": "ᴀᴅᴅ ᴀɴʏ ᴜꜱᴇʀ ᴛᴏ ᴘʀᴇᴍɪᴜᴍ.",
    "remove_premium": "ʀᴇᴍᴏᴠᴇ ᴀɴʏ ᴜꜱᴇʀ ꜰʀᴏᴍ ᴘʀᴇᴍɪᴜᴍ.",
    "premium_users": "ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀꜱ.",
    "restart": "ʀᴇꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ.",
    "admin_cmd": "ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs ʟɪsᴛ.",
    "reset_group": "Group Setting Default",
    "trial_reset": "User Trial Reset",
    "global_shortener": "Global Shortener On/Off",
    "glist": "Sᴀʙ ɢʀᴏᴜᴘs ᴋɪ ʟɪsᴛ ᴀᴜʀ ᴘᴀɴᴇʟ",
    "ginfo": "Specific group control panel",
    "gverify": "Verify on/off (Admin command)",
    "admin_cmd": "Admin commands list"
}


#Don't Change Anything Here
if MULTIPLE_DB == False:
    DATABASE_URI = DATABASE_URI
    DATABASE_URI2 = DATABASE_URI
else:
    DATABASE_URI = DATABASE_URI
    DATABASE_URI2 = DATABASE_URI2

# ============================
# Logs Configuration
# ============================
LOG_STR = "Current Customized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for your queries.\n" if IMDB else "IMDB Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found, Users will be redirected to send /start to Bot PM instead of sending file directly.\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled, files will be sent in PM instead of starting the bot.\n")
LOG_STR += ("BUTTON_MODE is found, filename and file size will be shown in a single button instead of two separate buttons.\n" if BUTTON_MODE else "BUTTON_MODE is disabled, filename and file size will be shown as different buttons.\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be sent along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled, Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode is enabled, bot will be suggesting related movies if movie name is misspelled.\n" if SPELL_CHECK_REPLY else "Spell Check Mode is disabled.\n")
