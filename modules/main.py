from pyrogram import Client, filters
import os

# Create the bot client
app = Client(
    "my_bot",
    api_id=os.environ.get("API_ID"),
    api_hash=os.environ.get("API_HASH"),
    bot_token=os.environ.get("BOT_TOKEN")
)

# Define a start handler
@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text("Hello! I am your bot.")

# Run the bot
if __name__ == "__main__":
    app.run()
