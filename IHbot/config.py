class Config(object):
    LOGGER = True
     # Required
    API_KEY = "676763277:AAE_FldJdktJdiimYLX9K05FCuMCNHlsQDE"
    OWNER_ID = "493358839" # If you dont know, run the bot and do /i$
    OWNER_USERNAME = "sharvari1192"
     # RECOMMENDED
    SQLALCHEMY_DATABASE_URI =
'mysql://amitpandey123121:amitpandey123121@db4free.net:amitpandey123$
# needed for any database modules
    MESSAGE_DUMP = None # needed to make sure 'save from'
messages persist
    LOAD = []
    NO_LOAD = ['translation', 'rss', 'weather']
    WEBHOOK = False
    URL = None
     # OPTIONAL
    SUDO_USERS = [] # List of id's (not usernames) for users
which have sudo access to the bot.
    SUPPORT_USERS = [] # List of id's (not usernames) for
users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = [] # List of id's (not usernames) for
users which WONT be banned/kicked by the bot.
    DONATION_LINK = None # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False # Whether or not you should delete "blue
text must click" commands
    STRICT_GBAN = False
    WORKERS = 8 # Number of subthreads to use. This is the
recommended amount - see for yourself what works best!
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg' #ban
sticker ID here
    ALLOW_EXCL = False # Allow ! commands as well as /
    API_OPENWEATHER = None # OpenWeather API
 class Production(Config):
    LOGGER = False
 class Development(Config):
    LOGGER = True
