from environs import Env
import os
import time

env = Env()
env.read_env()


os.environ['TZ'] = 'Asia/Tashkent'


BOT_TOKEN = "7921414575:AAGWAlfFGLhrNCDgIPxAaFvKOrogTCAcbDU"
ADMINS = [5065548183, 7818284462, 1954593467, ]  # O'z Telegram ID'ingizni kiriting

