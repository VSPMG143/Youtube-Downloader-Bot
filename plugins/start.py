from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Bots Updates Channel", url="https://t.me/andhrabots")],
        [InlineKeyboardButton(
            "Support Group", url="https://t.me/requestgroup2")]
    ])
    welcomed = f"Hi, <b>{message.from_user.first_name}</b>.\nThis is <b>YouTube Uploader Bot.</b>\n\nBy @andhrabots \nDeveloper: @Expertinbotmaking"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
