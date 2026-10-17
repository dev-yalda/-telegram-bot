import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# فعال‌سازی لاگ‌ها برای دیدن گزارش تمیز
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = "8998320399:AAHfaLQKgilssKmvUZMKDQYAbc794V2m9RY"
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_first_name = update.effective_user.first_name
    await update.message.reply_text(f"سلام {user_first_name}! من یلدا هستم، ربات پایتونی شما! 🌟🤖")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(f"شنیدم گفتی: {text} ✨")

def main():
    print("⏳ در حال برقراری ارتباط مستقیم با تلگرام...")
    
    # ساخت اپلیکیشن با تایم‌اوت مناسب بدون نیاز به پروکسی کدی
    app = ApplicationBuilder().token(TOKEN).connect_timeout(30).read_timeout(30).build()

    # تعریف دستورها
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("🚀 ربات بیدار شد، چشماشو باز کرد و منتظر دستوراته!")
    print("👉 الان برو توی تلگرام به رباتت پیام بده!")
    
    app.run_polling(drop_pending_updates=True)

if __name__ == '__main__':
    main()
