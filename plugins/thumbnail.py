from pyrogram import Client, filters
import moviepy.editor as mp
import os

@Client.on_message(filters.command("convert"))
async def convert_file(client, message):
    if len(message.command) < 3:
        return await message.reply("❌ Usage: /convert <input_file> <output_file>")

    input_file = message.command[1]
    output_file = message.command[2]

    if not os.path.exists(input_file):
        return await message.reply("❌ Input file not found!")

    try:
        clip = mp.VideoFileClip(input_file)
        clip.write_videofile(output_file)
        await message.reply_document(output_file, caption="✅ Conversion done!")
    except Exception as e:
        await message.reply(f"❌ Error: {e}")
    finally:
        if os.path.exists(output_file):
            os.remove(output_file)
