from pyrogram import Client, filters
import yt_dlp, zipfile, os

@Client.on_message(filters.command("link"))
async def link_to_file(client, message):
    if len(message.command) < 2:
        return await message.reply("❌ Usage: /link <video_url>")

    url = message.command[1]
    await message.reply("⏳ Downloading your video/file...")

    file_name = "video.mp4"
    try:
        ydl_opts = {"outtmpl": file_name}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        zip_name = "file.zip"
        with zipfile.ZipFile(zip_name, "w") as zipf:
            zipf.write(file_name)

        await message.reply_document(zip_name, caption="📦 Here is your ZIP file!")

    except Exception as e:
        await message.reply(f"❌ Error: {e}")
    finally:
        if os.path.exists(file_name):
            os.remove(file_name)
        if os.path.exists(zip_name):
            os.remove(zip_name)
