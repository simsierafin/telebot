import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ["BOT_TOKEN"]            # wajib diset
PORT = int(os.environ.get("PORT", 8443))   # Railway akan set PORT otomatis
WEBHOOK_BASE = os.environ.get("WEBHOOK_BASE")  # e.g. https://your-app.up.railway.app

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo! Bot jalan via webhook 🚀")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    url_path = TOKEN  # pakai token jadi path sulit ditebak
    webhook_url = f"{WEBHOOK_BASE}/{url_path}" if WEBHOOK_BASE else None

    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=url_path,
        webhook_url=webhook_url,   # kalau None -> setWebhook manual nanti
    )
