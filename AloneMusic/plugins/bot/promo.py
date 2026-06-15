# -----------------------------------------------
# 🔸 ShashankMusic Project
# 🔹 Developed & Maintained by: Shashank Shukla (https://github.com/itzshukla)
# 📅 Copyright © 2025 – All Rights Reserved
#
# 📖 License:
# This source code is open for educational and non-commercial use ONLY.
# You are required to retain this credit in all copies or substantial portions of this file.
# Commercial use, redistribution, or removal of this notice is strictly prohibited
# without prior written permission from the author.
#
# ❤️ Made with dedication and love by ItzShukla
# -----------------------------------------------

import random
from pyrogram import filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from ShashankMusic import app
from ShashankMusic.misc import SUDOERS
from config import SHASHANK_PIC


@app.on_message(filters.command("promo") & SUDOERS)
async def promo_post(client, message):

    promo_text = f"""
<b>{app.mention} — ᴍᴜꜱɪᴄ ʙᴏᴛ 🎧</b>

<blockquote><b>
๏ ᴛʜɪs ɪs ᴀ ᴘᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ  
๏ ɴᴏ ᴘʀᴏᴍᴏ | ɴᴏ ᴀᴅs | ᴘᴜʀᴇ ᴍᴜsɪᴄ | ɴᴏ ʟᴀɢ  
๏ sᴜᴘᴘᴏʀᴛs ʏᴏᴜᴛᴜʙᴇ & sᴘᴏᴛɪғʏ ᴜʀʟs  
๏ ʜɪɢʜ-ǫᴜᴀʟɪᴛʏ ᴀᴜᴅɪᴏ | ɴᴏ ʏᴛ ᴀᴘɪ ʟɪᴍɪᴛ  
๏ ᴄᴏɴsᴛᴀɴᴛ 24x7 ᴜᴘᴛɪᴍᴇ | ɴᴏ ᴇʀʀᴏʀ | ɴᴏ ɪɴᴛᴇʀʀᴜᴘᴛɪᴏɴ  
๏ ᴀᴅᴅ ᴍᴇ ᴀɴᴅ ᴇɴᴊᴏʏ ʏᴏᴜʀ ғᴀᴠᴏᴜʀɪᴛᴇ sᴏɴɢs ɪɴ ʜᴅ
</b></blockquote>
<b>● ʙᴏᴛ ᴜsᴇʀɴᴀᴍᴇ –</b> <a href="https://t.me/{app.username}">@{app.username}</a>
"""

    random_photo = random.choice(SHASHANK_PIC)

    buttons = [
        [
            InlineKeyboardButton(
                text="➕ ᴀᴅᴅ ᴍᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users"
            ),
        ],
    ]

    await app.send_photo(
        chat_id="@Spotify_update_s",
        photo=random_photo,
        caption=promo_text,
        reply_markup=InlineKeyboardMarkup(buttons),
        parse_mode=ParseMode.HTML
    )
