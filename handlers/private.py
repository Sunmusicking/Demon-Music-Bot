import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/a8e2f0831ab7cffc5b868.jpg",
        caption=f"""**⭐ᴛʜɪs ᴍᴜsɪᴄ ʙᴏᴛ ɪs ᴛʜᴇ ɴᴇxᴛ ʟᴇᴠᴇʟ ᴏғ ɢᴇɴᴇʀᴀᴛɪᴏɴ ᴛʜᴀᴛ ʜᴀs ʙᴇsᴛ ʜɪɢʜ ǫᴜᴀʟɪᴛʏ ᴏғ ᴍᴜsɪᴄ ʙᴏᴛ ᴀɴᴅ ᴛʜᴇ ᴛʜɪs ᴍᴜsɪᴄ ʙᴏᴛ sᴍᴀsʜ ᴛʜᴇᴍ ᴏғ ᴀʟʟ sᴇʀᴠᴇʀ ᴏғ ᴍᴜsɪᴄ ʙᴏᴛ ᴀss⭐...
▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
❰⚡️𝐎ᴡɴᴇʀ⚡️❱  ➠ [𝗞 𝗜 𝗡 𝗚](https://t.me/imzaynking)
▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
❰⭕️𝐒ᴜᴘᴘᴏʀᴛ⭕️❱ ➠ [𝗖𝗛𝗔𝗧 𝗕𝗢𝗫](https://t.me/TAMIL_CHATBOX)
▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
❰💙𝐂ʜᴀɴɴᴇʟ❤️❱ ➠ [𝗞𝗜𝗡𝗚_𝗕𝗜𝗢𝘇](https://t.me/KING_BIOZ)
▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃

ɪғ ʏᴏᴜ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴀɴᴅ ɪssᴜᴇ sᴏ ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇsᴇ ɪᴅ = [K I N G](https://t.me/imzaynking)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✰║🇰 🇮 🇳 🇬 ║✰▐ 𝐁𝐈𝐎𝐳▐", url=f"https://t.me/King_bioz")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo", "channel"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/6629605e2c6df2f9f6001.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ʀᴇᴘᴏ ᴀᴘᴘᴇᴀʟ ᴏɴ ᴛʜᴇsᴇ ɢʀᴏᴜᴘ ", url=f"https://t.me/TAMIL_CHATBOX")
                ]
            ]
        ),
    )
