import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

BOT_TOKEN = os.getenv("BOT_TOKEN")

PLATFORM_URL = "https://mijing.me/mijing.html"
MAP_URL = "https://mijing.me/map/map.html"


# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["🧭 進入覓境平台"],
        ["📍 打開覓境地圖"],
        ["🤝 店家合作洽詢"],
        ["ℹ️ 關於覓境"]
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "🔥🔥🔥 雲端版本 0129 🔥🔥🔥\n\n"
        "歡迎來到【覓境 Mijing】官方入口\n\n"
        "請使用下方按鈕操作 👇",
        reply_markup=reply_markup
    )


# 按鈕互動
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🧭 進入覓境平台":
        await update.message.reply_text(
            f"🧭【覓境 Mijing｜官方平台】\n\n"
            f"👉 點擊前往：\n{PLATFORM_URL}"
        )

    elif text == "📍 打開覓境地圖":
        await update.message.reply_text(
            f"📍【覓境地圖】\n\n"
            f"👉 立即開啟：\n{MAP_URL}"
        )

    elif text == "🤝 店家合作洽詢":
        await update.message.reply_text(
            "🤝【店家合作洽詢】\n\n"
            "請聯絡官方窗口：\n"
            "@mijing_official_bot"
        )

    elif text == "ℹ️ 關於覓境":
        await update.message.reply_text(
            "ℹ️【關於覓境】\n\n"
            "覓境是一個專注於\n"
            "按摩・芳療・SPA 實體服務的探索平台。"
        )

    else:
        await update.message.reply_text("請使用下方按鈕 👇")


def main():
    if not BOT_TOKEN:
        raise ValueError("❌ BOT_TOKEN 沒有設定")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 覓境 Bot 已啟動")
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
