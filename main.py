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

# --- Render Ping Server Setup (Render-এ রান রাখার জন্য) ---
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is active!")

def run_web_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
    server.serve_forever()

threading.Thread(target=run_web_server, daemon=True).start()

# --- Telegram Bot Code ---
TTOKEN = os.getenv("BOT_TOKEN", "8802980339:AAE1n1pT08Tgd3pPjTsVoW46pS-JEL-K-Jw")


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
                InlineKeyboardButton("📱 FB/TikTok Caption", callback_data="act_caption"),
                InlineKeyboardButton("🎥 Shorts/Reels Script", callback_data="act_script"),
            ],
            [
                InlineKeyboardButton("💡 Prompt Generator", callback_data="act_prompt"),
                InlineKeyboardButton("📚 Study Assistant", callback_data="act_study"),
            ],
            [
                InlineKeyboardButton("🔍 AI Search & Summary", callback_data="act_search")
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

    elif data == "menu_media":
        kb = [
            [
                InlineKeyboardButton("🎨 AI Image Gen", callback_data="act_img"),
                InlineKeyboardButton("🖼️ Thumbnail Gen", callback_data="act_thumb"),
            ],
            [
                InlineKeyboardButton("✂️ BG Remove", callback_data="act_bg_rem"),
                InlineKeyboardButton("🖼️ BG Change", callback_data="act_bg_change"),
            ],
            [
                InlineKeyboardButton("✨ Image Enhance", callback_data="act_enh"),
                InlineKeyboardButton("📐 Image Resize", callback_data="act_resize"),
            ],
            [
                InlineKeyboardButton("🎥 Video Prompt Gen", callback_data="act_vid_prompt"),
                InlineKeyboardButton("🎬 Subtitle Gen", callback_data="act_sub"),
            ],
            [
                InlineKeyboardButton("🔙 Main Menu", callback_data="main_menu")
            ],
        ]
        await query.message.edit_text(
            "🎨 **Image & Video Tools:**",
            reply_markup=InlineKeyboardMarkup(kb),
            parse_mode="Markdown",
        )

    elif data == "menu_voice":
        kb = [
            [
                InlineKeyboardButton("🗣️ Text -> Voice", callback_data="act_ttv"),
                InlineKeyboardButton("🎤 Voice -> Text", callback_data="act_vtt"),
            ],
            [
                InlineKeyboardButton("🇧🇩 Bangla Voice", callback_data="act_bn_voice"),
                InlineKeyboardButton("🇬🇧 English Voice", callback_data="act_en_voice"),
            ],
            [
                InlineKeyboardButton("🎧 Audio -> Text", callback_data="act_att")
            ],
            [
                InlineKeyboardButton("🔙 Main Menu", callback_data="main_menu")
            ],
        ]
        await query.message.edit_text(
            "🎙️ **Voice & Audio Services:**",
            reply_markup=InlineKeyboardMarkup(kb),
            parse_mode="Markdown",
        )

    elif data == "menu_pdf":
        kb = [
            [
                InlineKeyboardButton("📄 PDF -> Text", callback_data="act_pdf2txt"),
                InlineKeyboardButton("🖼️ Image -> Text (OCR)", callback_data="act_ocr"),
            ],
            [
                InlineKeyboardButton("🧩 PDF Merge", callback_data="act_pdf_merge"),
                InlineKeyboardButton("✂️ PDF Split", callback_data="act_pdf_split"),
            ],
            [
                InlineKeyboardButton("🔄 File Converter", callback_data="act_converter"),
                InlineKeyboardButton("📝 PDF/Doc Summary", callback_data="act_pdf_sum"),
            ],
            [
                InlineKeyboardButton("🔙 Main Menu", callback_data="main_menu")
            ],
        ]
        await query.message.edit_text(
            "📄 **PDF & Document Management:**",
            reply_markup=InlineKeyboardMarkup(kb),
            parse_mode="Markdown",
        )

    elif data == "menu_rewards":
        kb = [
            [
                InlineKeyboardButton("🎁 Welcome Bonus", callback_data="act_bonus_wel"),
                InlineKeyboardButton("📅 Daily Bonus", callback_data="act_bonus_daily"),
            ],
            [
                InlineKeyboardButton("🔥 7-Day Streak", callback_data="act_streak"),
                InlineKeyboardButton("🎯 Daily Missions", callback_data="act_missions"),
            ],
            [
                InlineKeyboardButton("📦 Lucky Box", callback_data="act_lucky"),
                InlineKeyboardButton("📺 Reward Ads", callback_data="act_ads"),
            ],
            [
                InlineKeyboardButton("🏆 Leaderboard", callback_data="act_lead"),
                InlineKeyboardButton("🎉 Special Event", callback_data="act_event"),
            ],
            [
                InlineKeyboardButton("🔙 Main Menu", callback_data="main_menu")
            ],
        ]
        await query.message.edit_text(
            "🎁 **Rewards & Bonus System:**",
            reply_markup=InlineKeyboardMarkup(kb),
            parse_mode="Markdown",
        )


def main():
    app = Application.builder().token(TTOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Bot is running...")
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
