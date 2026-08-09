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

# Render Web Server Setup
class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Bot is alive and running!")

    def log_message(self, format, *args):
        return

def run_web_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), HealthCheckHandler)
    server.serve_forever()

threading.Thread(target=run_web_server, daemon=True).start()

# Bot Token Setup
TOKEN = os.environ.("TOKEN = "8802980339:AAGuhzlHo-fBfh2UHgGqDRwvaFci73xRsY")

# Menus & Handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("🤖 AI & Content", callback_data="menu_ai"),
            InlineKeyboardButton("🎨 Image & Media", callback_data="menu_media"),
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
    msg = (
        "✨ **Welcome to Aivora All-in-One AI Bot!** ✨\n\n"
        "আপনার প্রয়োজনীয় সেবাটি পেতে নিচের মেনু থেকে অপশন নির্বাচন করুন:"
    )

    if update.message:
        await update.message.reply_text(msg, reply_markup=reply_markup, parse_mode="Markdown")
    elif update.callback_query:
        await update.callback_query.message.edit_text(msg, reply_markup=reply_markup, parse_mode="Markdown")

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "main_menu":
        await start(update, context)

    elif data == "menu_ai":
        kb = [
            [
                InlineKeyboardButton("💬 Smart Chat", callback_data="act_chat"),
                InlineKeyboardButton("✍️ Content Writer", callback_data="act_writer"),
            ],
            [
                InlineKeyboardButton("🌐 Translator", callback_data="act_trans"),
                InlineKeyboardButton("🎬 YouTube Assistant", callback_data="act_yt"),
            ],
            [InlineKeyboardButton("🔙 Main Menu", callback_data="main_menu")],
        ]
        text = "🤖 **AI & Content Generation Services:**\n\nযেকোনো বিষয়ে প্রশ্ন করতে বা কনটেন্ট তৈরি করতে অপশন সিলেক্ট করুন।"
        await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(kb), parse_mode="Markdown")

    elif data == "menu_media":
        kb = [
            [
                InlineKeyboardButton("🖼️ Text to Image", callback_data="act_img"),
                InlineKeyboardButton("🧹 Background Remover", callback_data="act_bgrem"),
            ],
            [
                InlineKeyboardButton("🔍 Upscale Image", callback_data="act_upscale"),
                InlineKeyboardButton("🎥 Short Video Gen", callback_data="act_video"),
            ],
            [InlineKeyboardButton("🔙 Main Menu", callback_data="main_menu")],
        ]
        text = "🎨 **Image & Media Services:**\n\nAI ছবি জেনারেট বা ইমেজ এডিটিং সেবার জন্য অপশন বেছে নিন।"
        await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(kb), parse_mode="Markdown")

    elif data == "menu_voice":
        kb = [
            [
                InlineKeyboardButton("🗣️ Text to Speech", callback_data="act_tts"),
                InlineKeyboardButton("🎙️ Voice Cloning", callback_data="act_voice_clone"),
            ],
            [
                InlineKeyboardButton("🎵 AI Music Gen", callback_data="act_music"),
            ],
            [InlineKeyboardButton("🔙 Main Menu", callback_data="main_menu")],
        ]
        text = "🎙️ **Voice & Audio Services:**\n\nভয়েস ওভার ও অডিও তৈরির ফিচার নির্বাচন করুন।"
        await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(kb), parse_mode="Markdown")

    elif data == "menu_pdf":
        kb = [
            [
                InlineKeyboardButton("📄 PDF Summarizer", callback_data="act_pdf_sum"),
                InlineKeyboardButton("📝 CV/Resume Builder", callback_data="act_cv"),
            ],
            [
                InlineKeyboardButton("📊 Excel Data Extraction", callback_data="act_excel"),
            ],
            [InlineKeyboardButton("🔙 Main Menu", callback_data="main_menu")],
        ]
        text = "📄 **PDF & Document Tools:**\n\nপিডিএফ সারসংক্ষেপ ও সিভি তৈরির টুল বেছে নিন।"
        await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(kb), parse_mode="Markdown")

    elif data == "menu_rewards":
        kb = [
            [
                InlineKeyboardButton("🎁 Daily Bonus (+5 Credits)", callback_data="act_daily_claim"),
            ],
            [
                InlineKeyboardButton("🏆 Leaderboard", callback_data="act_leaderboard"),
            ],
            [InlineKeyboardButton("🔙 Main Menu", callback_data="main_menu")],
        ]
        text = "🎁 **Daily Rewards & Bonus:**\n\nপ্রতিদিন ফ্রিতে ক্রেডিট পান এবং লিডারবোর্ড দেখুন।"
        await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(kb), parse_mode="Markdown")

    elif data == "menu_wallet":
        kb = [
            [
                InlineKeyboardButton("💳 Balance: 20 Credits", callback_data="act_bal"),
                InlineKeyboardButton("➕ Add Credits", callback_data="act_add_credit"),
            ],
            [
                InlineKeyboardButton("📜 Transaction History", callback_data="act_history"),
            ],
            [InlineKeyboardButton("🔙 Main Menu", callback_data="main_menu")],
        ]
        text = "💰 **Wallet & Credits:**\n\nআপনার একাউন্টের ব্যালেন্স ও হিস্ট্রি চেক করুন।"
        await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(kb), parse_mode="Markdown")

    elif data == "menu_referral":
        kb = [
            [
                InlineKeyboardButton("🔗 Get Referral Link", callback_data="act_ref_link"),
            ],
            [InlineKeyboardButton("🔙 Main Menu", callback_data="main_menu")],
        ]
        text = (
            "👥 **Referral System:**\n\n"
            "বন্ধুদের রেফার করুন এবং প্রতি রেফারে ১০ ক্রেডিট আয় করুন!\n"
            "আপনার রেফারেল লিংক পেতে নিচের বাটনে ক্লিক করুন।"
        )
        await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(kb), parse_mode="Markdown")

    elif data == "menu_premium":
        kb = [
            [
                InlineKeyboardButton("⭐ Monthly ($2 / 200 BDT)", callback_data="act_plan_m"),
            ],
            [
                InlineKeyboardButton("🚀 Unlimited Yearly ($15)", callback_data="act_plan_y"),
            ],
            [InlineKeyboardButton("🔙 Main Menu", callback_data="main_menu")],
        ]
        text = (
            "💎 **Premium Plans:**\n\n"
            "আনলিমিটেড অ্যাক্সেস পেতে প্রিমিয়াম মেম্বারশিপ গ্রহণ করুন।\n"
            "পেমেন্ট মাধ্যম: bKash / Nagad / Crypto"
        )
        await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(kb), parse_mode="Markdown")

    elif data == "menu_admin":
        kb = [
            [
                InlineKeyboardButton("📊 Total Users: 1", callback_data="act_admin_stat"),
                InlineKeyboardButton("📢 Broadcast Message", callback_data="act_admin_bc"),
            ],
            [InlineKeyboardButton("🔙 Main Menu", callback_data="main_menu")],
        ]
        text = "👨‍💻 **Admin Control Panel:**\n\nঅ্যাডমিন সেটিংস ও বডকাস্ট ফিচার।"
        await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(kb), parse_mode="Markdown")

    elif data == "menu_status":
        kb = [
            [
                InlineKeyboardButton("🟢 Server Status: Online", callback_data="act_status_check"),
            ],
            [InlineKeyboardButton("🔙 Main Menu", callback_data="main_menu")],
        ]
        text = "🛡️ **Security & System Status:**\n\nসার্ভার লেটেন্সি ও স্ট্যাটাস সম্পূর্ণ নরমাল রয়েছে।"
        await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(kb), parse_mode="Markdown")

    elif data.startswith("act_"):
        kb = [[InlineKeyboardButton("🔙 Main Menu", callback_data="main_menu")]]
        await query.message.edit_text(
            f"⚡ **Feature Active:** `{data}`\n\nধন্যবাদ! শীঘ্রই ফিচারটির কাজ চলমান।",
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
