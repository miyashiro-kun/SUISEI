# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

from telethon.errors import (
    BotMethodInvalidError,
    ChatSendInlineForbiddenError,
    ChatSendMediaForbiddenError,
)

from . import *

REPOMSG = """
Suisei No Gotoku Arawareta Start no Genseki Hoshimati Suisei !!!
"""

RP_BUTTONS = [
    [Button.url("My Master", "t.me/Suisei_Hoshimati")],
]

ULTSTRING = """** Suichan Kyo mo Kawaiii **"""


@ultroid_cmd(
    pattern="repo$",
    type=["official", "manager"],
)
async def repify(e):
    try:
        q = await e.client.inline_query(asst.me.username, "")
        await q[0].click(e.chat_id)
        return await e.delete()
    except (
        ChatSendInlineForbiddenError,
        ChatSendMediaForbiddenError,
        BotMethodInvalidError,
    ):
        pass
    except Exception as er:
        LOGS.info("Error while repo command : " + str(er))
    await eor(e, REPOMSG)


@ultroid_cmd(pattern="ultroid")
async def useUltroid(rs):
    button = Button.inline("Start >>", "initft_2")
    msg = await asst.send_message(
        LOG_CHANNEL,
        ULTSTRING,
        file="https://i.ibb.co/BTR5Sky/photo-2021-09-13-11-59-13.jpg",
        buttons=button,
    )
    await eor(rs, f"**[Click Here]({msg.message_link})**")
