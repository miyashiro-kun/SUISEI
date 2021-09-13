# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

import asyncio
import os
import time

from pyUltroid import *
from pyUltroid.dB import *
from pyUltroid.functions.all import *
from pyUltroid.functions.sudos import *
from pyUltroid.version import ultroid_version
from telethon import Button
from telethon.tl import functions, types
from telethon.utils import get_display_name

from strings import get_string

try:
    import glitch_me
except ModuleNotFoundError:
    os.system(
        "git clone https://github.com/1Danish-00/glitch_me.git && pip install -e ./glitch_me"
    )


start_time = time.time()

OWNER_NAME = ultroid_bot.me.first_name
OWNER_ID = ultroid_bot.me.id
LOG_CHANNEL = int(udB.get("LOG_CHANNEL"))

List = []
Dict = {}
N = 0

# Chats, which needs to be ignore for some cases
# Considerably, there can be many
# Feel Free to Add Any other...

NOSPAM_CHAT = [
    -1001327032795,  # UltroidSupport
    -1001387666944,  # PyrogramChat
    -1001109500936,  # TelethonChat
    -1001050982793,  # Python
    -1001256902287,  # DurovsChat
]

KANGING_STR = [
    "sticker Gettoo !! (つ✧ω✧)つ ...",
    "Comot ea ヽ(￣ω￣ )",
    "Sticker catch (°◡°♡)",
    "ima Stealing this sticker... 	(￣ε￣＠) ",
    "Hey that's a nice sticker!\nMorau ne?!..",
]
