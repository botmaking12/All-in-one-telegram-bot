from pyrogram import Client, filters
import os

@Client.on_message(filters.command("rename"))
async def rename_file(client, message):
    if len(message.command) < 3:
        return await message.reply("❌ Usage: /rename <old_filename> <new_filename>")

    old_name = message.command[1]
    new_name = message.command[2]

    if not os.path.exists(old_name):
        return await message.reply("❌ File not found!")

    os.rename(old_name, new_name)
    await message.reply(f"✅ File renamed to {new_name}")
