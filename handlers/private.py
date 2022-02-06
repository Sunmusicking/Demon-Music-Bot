import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/10d469ec236d49a43650c.jpg",
        caption=f"""**ᴛʜɪs ᴍᴜsɪᴄ ʙᴏᴛ ɪs ᴛʜᴇ ɴᴇxᴛ ʟᴇᴠᴇʟ ᴏғ ɢᴇɴᴇʀᴀᴛɪᴏɴ ᴛʜᴀᴛ ʜᴀs ʙᴇsᴛ ʜɪɢʜ ǫᴜᴀʟɪᴛʏ ᴏғ ᴍᴜsɪᴄ ʙᴏᴛ ᴀɴᴅ ᴛʜᴇ ᴛʜɪs ᴍᴜsɪᴄ ʙᴏᴛ sᴍᴀsʜ ᴛʜᴇᴍ ᴏғ ᴀʟʟ sᴇʀᴠᴇʀ ᴏғ ᴍᴜsɪᴄ ʙᴏᴛ ᴀss...

🇴ᴡɴᴇʀ :- [Sᴜᴍɪᴛ Yᴀᴅᴀᴠ](https://t.me/Simple_Mundaa)
🇸ᴜᴘᴘᴏʀᴛ 🇬ʀᴏᴜᴘ   » [Wᴏʀʟᴅ FʀɪᴇɴᴅSʜɪᴘ Zᴏɴᴇ](https://t.me/World_FriendShip_Zone)
🇩ɪsᴄᴜss 🇬ʀᴏᴜᴘ  » [Dᴇᴍᴏɴ Cʀᴇᴀᴛᴏʀs Sᴜᴘᴘᴏʀᴛ](https://t.me/Demon_Support_Group)
🇾ᴏᴜᴛᴜʙᴇ 🇨ʜᴀɴɴᴇʟ   » [ᴀs ᴛᴇᴄʜɴɪᴄᴀʟ](https://youtube.com/channel/UCtI7hbY-BD7wvuIzoSU0cEw)
🇫ᴇᴍᴀʟᴇ 🇴ᴡɴᴇʀ  » [Nɪᴋɪᴛᴀ](https://t.me/Cute_Shezhadi012)
🇺ᴘᴅᴀᴛᴇ 🇨ʜᴀɴɴᴇʟ  » [Dᴇᴍᴏɴ Cʀᴇᴀᴛᴏʀs](https://t.me/Demon_Creators)

ɪғ ʏᴏᴜ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴀɴᴅ ɪssᴜᴇ sᴏ ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇsᴇ ɪᴅ = [Sᴜᴍɪᴛ Yᴀᴅᴀᴠ](https://t.me/Simple_Mundaa)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🅳︎ɪsʜɴᴇʏ xᴅ 🅷︎ᴇᴀʀᴛ", url=f"https://t.me/DISNEY_XD_HEART")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo", "channel"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/10d469ec236d49a43650c.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ʀᴇᴘᴏ ᴀᴘᴘᴇᴀʟ ᴏɴ ᴛʜᴇsᴇ ɢʀᴏᴜᴘ ", url=f"https://t.me/Demon_Creators_Support")
                ]
            ]
        ),
    )
