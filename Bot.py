import requests
from bs4 import BeautifulSoup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# ✅ Tumhara new bot token hardcoded:
BOT_TOKEN = '8080954224:AAFxo_pdJdEfvjoVf1xGb2dG-VulJPpach8'

# /start command
def start(update, context):
    update.message.reply_text(
        "👋 Welcome To Cyber Mafia's Bot ❤️\n"
        "DM me if you face any problem with my bots.\n"
        "You can also DM me if you want any help.\n"
        "\nOptions:\n"
        "1️⃣ Download Video\n"
        "2️⃣ Download Audio\n"
        "3️⃣ Help\n"
        "4️⃣ Contact Owner"
    )

# Jab user koi link bheje
def handle_message(update, context):
    url = update.message.text.strip()
    update.message.reply_text("⏳ Processing your link...")

    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        # Dummy reply (real download logic yahan aa sakta hai)
        update.message.reply_text(f"✅ Download link processed: {url}")
    except Exception as e:
        update.message.reply_text(f"❌ Error: {e}")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
  
