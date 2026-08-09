import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
)

# --- Render Web Server Setup ---
class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Bot is alive and running!")

def run_web_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), HealthCheckHandler)
    server.serve_forever()

threading.Thread(target=run_web_server, daemon=True).start()

# --- Correct Bot Token ---
TOKEN = "8802980339:AAE1n1pT08Tgd3pPjTsVoM46pS-JEL-K-Jw"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("🤖 AI & Content", callback_data="menu_ai"),
            InlineKeyboardButton("🎨 Image & Video", callback_data="menu_media"),
        ],
        [
            InlineKeyboardButton("🎙️ Voice & Audio", callback_data="menu_voice"),
            InlineKeyboardButton("📄 PDF & Docs", callback_data="menu_pdf"),
        ],
        [
            InlineKeyboardButton("🎁 Rewards & Bonus", callback_data="menu_rewards"),
            InlineKeyboardButton("💰 Wallet & Credits", callback_data="menu_wallet"),
        ],
        [
            InlineKeyboardButton("👥 Referral System", callback_data="menu_referral"),
            InlineKeyboardButton("💎 Premium Plans", callback_data="menu_premium"),
        ],
        [
            InlineKeyboardButton("👨‍💻 Admin Panel", callback_data="menu_admin"),
            InlineKeyboardButton("🛡️ Security & Status", callback_data="menu_status"),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    msg = "✨ **Aivora All-in-One AI Bot**-এ আপনাকে স্বাগতম!\n\nআপনার প্রয়োজনীয় ক্যাটাগরি বেছে নিন:"

    if update.message:
        await update.message.reply_text(
            msg, reply_markup=reply_markup, parse_mode="Markdown"
        )
    else:
        await update.callback_query.message.edit_text(
            msg, reply_markup=reply_markup, parse_mode="Markdown"
        )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "main_menu":
        await start(update, context)

    elif data == "menu_ai":
        kb = [
            [
                InlineKeyboardButton("🤖 AI Chat", callback_data="act_chat"),
                InlineKeyboardButton("✍️ AI Writing", callback_data="act_writing"),
            ],
            [
                InlineKeyboardButton("🌐 Bangla <-> English", callback_data="act_trans"),
                InlineKeyboardButton("🎬 YouTube Title/Desc", callback_data="act_yt"),
            ],
            [
                InlineKeyboardButton("🔙 Main Menu", callback_data="main_menu")
            ],
        ]
        await query.message.edit_text(
            "🤖 **AI & Content Generation Services:**",
            reply_markup=InlineKeyboardMarkup(kb),
            parse_mode="Markdown",
        )


def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Bot is running...")
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
