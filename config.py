import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "27899654")) #optional
API_HASH = getenv("API_HASH", "644a291c69677a2fd785c43455b1df08") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
OWNER_ID = int(getenv("OWNER_ID", "5851363440"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://blazeshubham:shubham@cluster0.vftwypv.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "5844402409:AAHNv3686CJ8AuKV-ZqK80gFPBzi0_r-HsI")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://telegra.ph/file/a93d7fdd0e919d740bd34.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQBdYFBwcBYBVKBKQdje558RAB-BKjJrK31eK5JkgMIyQFcFZqslFMAJu_yuamPYJMAi5aRHR1y_mO-MPA9Fcwo1IOgpqwmidIGPzEsdTJogHIEDCHOYxZe75vNavjDNjXfFyvnxx4YkKcvJKgJBJlkM9zySE58YP_z31ydSeYn3Ew41Vvu1yXTBMyzI6oNTs3jRyH2O03NsEFtEPUb9yyQFImtfZRnL9zH5aHBfhycrAdGHcvF3kU2so2tLGugNARLh1HrMjF7CsQxkPfJXBKcvp-yuAPFtSwaysXE6dR9DZvIvrC9FUPijrwUjq9diqlV2ujJleOxGPxAkgdzgZ-b4AAAAAVzEuHAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
