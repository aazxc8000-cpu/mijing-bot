from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN ="8229177958:AAF3GbL8zSQpVpwLsCrDRRFye4v6V9cszYk"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "歡迎來到【覓境 Mijing】官方入口\n\n"
        "探索附近按摩・芳療・SPA 實體店\n"
        "合作洽詢請使用 /contact"
    )

async def nearby(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📍 附近店家功能即將上線")

async def notice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📢 最新公告將於此發布")

async def channel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👉 官方推薦頻道：https://t.me/你的頻道")

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "覓境 Mijing 是專注於按摩・芳療・SPA 的實體探索平台，\n"
        "協助優質店家提升曝光，並為消費者提供可信任的選擇。"
    )

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("合作洽詢請聯絡@mijing_official_bot")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("nearby", nearby))
    app.add_handler(CommandHandler("notice", notice))
    app.add_handler(CommandHandler("channel", channel))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("contact", contact))

    print("🤖 覓境 Bot 已啟動")
    app.run_polling()

if __name__ == "__main__":
    main()
