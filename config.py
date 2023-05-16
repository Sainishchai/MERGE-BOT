import os


class Config(object):
    API_HASH = os.environ.get("API_HASH" ,"152e94d23ca0b3cc96a2c1278b967ca4")
    BOT_TOKEN = os.environ.get("BOT_TOKEN" ,"6039043446:AAHf8ODju2FpNFBXj7v2-MwC0HxpLAu_0wU")
    TELEGRAM_API = os.environ["TELEGRAM_API" ,"21525441"]
    OWNER = os.environ.get("OWNER , "")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME" ,"")
    PASSWORD = os.environ.get("PASSWORD" ,"")
    DATABASE_URL = os.environ.get("DATABASE_URL" ,"")
    LOGCHANNEL = os.environ.get("LOGCHANNEL ,""")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID","root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]
