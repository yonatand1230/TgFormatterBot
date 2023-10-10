from pyrogram import Client, filters, idle
from pyrogram.types import BotCommand, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineQueryResultArticle, InputTextMessageContent


Api_id = 0	# Put your API ID here
Api_hash = "YOUR_API_HASH_HERE"
Bot_token = "YOUR_BOT_TOKEN_HERE"

app = Client(
    name="MsgFormatter",
    api_id = Api_id,
    api_hash = Api_hash,
    bot_token = Bot_token
    )

app.start()
print("====================================\nMessage Formatter\n====================================\n")



allowed_users = ['User1', 'User2'] # Put allowed users here


special_chars = ['*', '_', '~']
@app.on_message(filters.chat(allowed_users))
async def handleMessage(client, msg):
    l = list(msg.text)
    for i, c in enumerate(l):
        if c in special_chars:
            l[i] = c*2
    await msg.reply_text(''.join(l))

idle()
