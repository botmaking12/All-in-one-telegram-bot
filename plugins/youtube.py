from pyrogram import Client, filters
import yt_dlp, os

@Client.on_message(filters.command("yt"))
async def youtube_download(client, message):
    if len(message.command) < 2:
        return await message.reply("❌ Usage: /yt <youtube_link>")

    url = message.command[1]
    await message.reply("⏳ Downloading YouTube video...")

    file_name = "yt_video.mp4"
    try:
        ydl_opts = {"outtmpl": file_name}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        await message.reply_video(file_name, caption="📽️ Here is your video!")
    except Exception as e:
        await message.reply(f"❌ Error: {e}")
    finally:
        if os.path.exists(file_name):
            os.remove(file_name)
