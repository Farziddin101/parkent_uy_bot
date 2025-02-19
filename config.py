from environs import Env
import os
import time

env = Env()
env.read_env()


os.environ['TZ'] = 'Asia/Tashkent'


BOT_TOKEN = "7921414575:AAGWAlfFGLhrNCDgIPxAaFvKOrogTCAcbDU"
ADMINS = [1379319763, 7818284462]  # O'z Telegram ID'ingizni kiriting

