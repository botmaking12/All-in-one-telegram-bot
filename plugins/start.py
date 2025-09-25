from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def fancy(text):
    return f"✨ 𝓦𝓮𝓵𝓬𝓸𝓶𝓮 {text} 🌟"

@Client.on_message(filters.command("start"))
async def start(client, message):
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("🎥 𝐘𝐨𝐮𝐓𝐮𝐛𝐞 MP4", callback_data="yt_video"),
         InlineKeyboardButton("🎵 𝐘𝐨𝐮𝐓𝐮𝐛𝐞 MP3", callback_data="yt_audio")],
        [InlineKeyboardButton("📂 𝐋𝐢𝐧𝐤→𝐅𝐢𝐥𝐞", callback_data="link_file"),
         InlineKeyboardButton("🖊️ 𝐑𝐞𝐧𝐚𝐦𝐞", callback_data="rename")],
        [InlineKeyboardButton("🔄 𝐂𝐨𝐧𝐯𝐞𝐫𝐭", callback_data="convert"),
         InlineKeyboardButton("🖼️ 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥", callback_data="thumbnail")]
    ])
    await message.reply_text(
        fancy(message.from_user.first_name) + "\n\n🚀 Main hu ek All-in-One Bot",
        reply_markup=buttons
    )

@Client.on_message(filters.command("help"))
async def help_cmd(client, message):
    text = (
        "📌 𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬:\n\n"
        "🎥 /yt <link> → YouTube video/mp3 download\n"
        "📂 /link <url> → Link to File/Video (ZIP supported)\n"
        "🖊️ /rename → Rename a file\n"
        "🔄 /convert → File ⇄ Video\n"
        "🖼️ /thumbnail → Add/View/Remove thumbnail\n"
    )
    await message.reply_text(text)
