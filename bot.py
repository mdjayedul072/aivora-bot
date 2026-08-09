from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = 8802980339:"1n1pT08Tgd3pPjTsVoM46pS-JEL-K-Jw

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🤖 AI & Content", callback_data='menu_ai'), InlineKeyboardButton("🎨 Image & Video", callback_data='menu_media')],
        [InlineKeyboardButton("🎙️ Voice & Audio", callback_data='menu_voice'), InlineKeyboardButton("📄 PDF & Docs", callback_data='menu_pdf')],
        [InlineKeyboardButton("🎁 Rewards & Bonus", callback_data='menu_rewards'), InlineKeyboardButton("💰 Wallet & Credits", callback_data='menu_wallet')],
        [InlineKeyboardButton("👥 Referral System", callback_data='menu_referral'), InlineKeyboardButton("💎 Premium Plans", callback_data='menu_premium')],
        [InlineKeyboardButton("👨‍💻 Admin Panel", callback_data='menu_admin'), InlineKeyboardButton("🛡️ Security & Status", callback_data='menu_security')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    msg = "👋 **Aivora All-in-One AI Bot**-এ আপনাকে স্বাগতম!\n\nআপনার প্রয়োজনীয় ক্যাটাগরি বেছে নিন:"
    
    if update.message:
        await update.message.reply_text(msg, reply_markup=reply_markup, parse_mode='Markdown')
    else:
        await update.callback_query.message.edit_text(msg, reply_markup=reply_markup, parse_mode='Markdown')

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data
    user = query.from_user

    if data == 'main_menu':
        await start(update, context)

    elif data == 'menu_ai':
        kb = [
            [InlineKeyboardButton("🤖 AI Chat", callback_data='act_chat'), InlineKeyboardButton("✍️ AI Writing", callback_data='act_writing')],
            [InlineKeyboardButton("🌐 Bangla ↔ English", callback_data='act_trans'), InlineKeyboardButton("🎬 YouTube Title/Desc", callback_data='act_yt')],
            [InlineKeyboardButton("📱 FB/TikTok Caption", callback_data='act_caption'), InlineKeyboardButton("🎥 Shorts/Reels Script", callback_data='act_script')],
            [InlineKeyboardButton("💡 Prompt Generator", callback_data='act_prompt'), InlineKeyboardButton("📚 Study Assistant", callback_data='act_study')],
            [InlineKeyboardButton("🔍 AI Search & Summary", callback_data='act_search')],
            [InlineKeyboardButton("🔙 Main Menu", callback_data='main_menu')]
        ]
        await query.message.edit_text("🤖 **AI & Content Generation Services:**", reply_markup=InlineKeyboardMarkup(kb), parse_mode='Markdown')

    elif data == 'menu_media':
        kb = [
            [InlineKeyboardButton("🎨 AI Image Gen", callback_data='act_img'), InlineKeyboardButton("🖼️ Thumbnail Gen", callback_data='act_thumb')],
            [InlineKeyboardButton("✂️ BG Remove", callback_data='act_bg_rem'), InlineKeyboardButton("🔄 BG Change", callback_data='act_bg_chg')],
            [InlineKeyboardButton("✨ Image Enhance", callback_data='act_enh'), InlineKeyboardButton("📐 Image Resize", callback_data='act_resize')],
            [InlineKeyboardButton("🎥 Video Prompt Gen", callback_data='act_vid_prompt'), InlineKeyboardButton("📝 Subtitle Gen", callback_data='act_sub')],
            [InlineKeyboardButton("🔙 Main Menu", callback_data='main_menu')]
        ]
        await query.message.edit_text("🎨 **Image & Video Tools:**", reply_markup=InlineKeyboardMarkup(kb), parse_mode='Markdown')

    elif data == 'menu_voice':
        kb = [
            [InlineKeyboardButton("🔊 Text → Voice", callback_data='act_ttv'), InlineKeyboardButton("🎤 Voice → Text", callback_data='act_vtt')],
            [InlineKeyboardButton("🇧🇩 Bangla Voice", callback_data='act_bn_voice'), InlineKeyboardButton("🇬🇧 English Voice", callback_data='act_en_voice')],
            [InlineKeyboardButton("🎧 Audio → Text", callback_data='act_att')],
            [InlineKeyboardButton("🔙 Main Menu", callback_data='main_menu')]
        ]
        await query.message.edit_text("🎙️ **Voice & Audio Services:**", reply_markup=InlineKeyboardMarkup(kb), parse_mode='Markdown')

    elif data == 'menu_pdf':
        kb = [
            [InlineKeyboardButton("📄 PDF → Text", callback_data='act_pdf2txt'), InlineKeyboardButton("🖼️ Image → Text (OCR)", callback_data='act_ocr')],
            [InlineKeyboardButton("🔗 PDF Merge", callback_data='act_pdf_merge'), InlineKeyboardButton("✂️ PDF Split", callback_data='act_pdf_split')],
            [InlineKeyboardButton("🔄 File Converter", callback_data='act_converter'), InlineKeyboardButton("📝 PDF/Doc Summary", callback_data='act_doc_sum')],
            [InlineKeyboardButton("🔙 Main Menu", callback_data='main_menu')]
        ]
        await query.message.edit_text("📄 **PDF & Document Management:**", reply_markup=InlineKeyboardMarkup(kb), parse_mode='Markdown')

    elif data == 'menu_rewards':
        kb = [
            [InlineKeyboardButton("🎁 Welcome Bonus", callback_data='act_bonus_wel'), InlineKeyboardButton("📅 Daily Bonus", callback_data='act_bonus_daily')],
            [InlineKeyboardButton("🔥 7-Day Streak", callback_data='act_streak'), InlineKeyboardButton("🎯 Daily Missions", callback_data='act_mission')],
            [InlineKeyboardButton("🎁 Lucky Box", callback_data='act_lucky'), InlineKeyboardButton("📺 Reward Ads", callback_data='act_ads')],
            [InlineKeyboardButton("🏆 Leaderboard", callback_data='act_lead'), InlineKeyboardButton("🎉 Special Event", callback_data='act_event')],
            [InlineKeyboardButton("🔙 Main Menu", callback_data='main_menu')]
        ]
        await query.message.edit_text("🎁 **Rewards & Bonus System:**", reply_markup=InlineKeyboardMarkup(kb), parse_mode='Markdown')

    elif data == 'menu_wallet':
        kb = [
            [InlineKeyboardButton("💳 Balance", callback_data='act_bal'), InlineKeyboardButton("📊 Earned / Spent", callback_data='act_stat')],
            [InlineKeyboardButton("📜 Transactions", callback_data='act_tx'), InlineKeyboardButton("💸 Withdrawal System", callback_data='act_withdraw')],
            [InlineKeyboardButton("🔙 Main Menu", callback_data='main_menu')]
        ]
        await query.message.edit_text("💰 **Wallet & Credit System:**\n\n• Available Credits: 50\n• Total Earned: 100\n• Total Spent: 50", reply_markup=InlineKeyboardMarkup(kb), parse_mode='Markdown')

    elif data == 'menu_referral':
        kb = [
            [InlineKeyboardButton("🔗 Link", callback_data='act_reflink'), InlineKeyboardButton("🏆 Top Referrers", callback_data='act_top_ref')],
            [InlineKeyboardButton("🔙 Main Menu", callback_data='main_menu')]
        ]
        text = f"👥 **Referral System:**\n\n• Personal Link: `https://t.me/AivoraOfficialBot?start={user.id}`\n• Bonus: প্রতি রেফারে ১০ ক্রেডিট + প্রিমিয়াম ডেজ!\n• Anti-Fraud Enabled 🛡️"
        await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(kb), parse_mode='Markdown')

    elif data == 'menu_premium':
        kb = [
            [InlineKeyboardButton("💎 Buy Pro (৳৯৯)", callback_data='act_buy_pro'), InlineKeyboardButton("👑 Buy Premium (৳১৯৯)", callback_data='act_buy_prem')],
            [InlineKeyboardButton("🔙 Main Menu", callback_data='main_menu')]
        ]
        text = "💎 **Premium Plans:**\n\n🆓 **Free Plan:** দিনে ৫ বার মেম্বারশিপ\n💎 **Pro Plan:** ৫০ মেসেজ/দিন + ২০ ইমেজ Gen\n👑 **Premium Plan:** Unlimited AI + Ad-Free + Priority Speed"
        await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(kb), parse_mode='Markdown')

    elif data == 'menu_admin':
        kb = [
            [InlineKeyboardButton("👥 Users Stat", callback_data='act_admin_usr'), InlineKeyboardButton("💰 Revenue", callback_data='act_admin_rev')],
            [InlineKeyboardButton("📢 Ads Mgmt", callback_data='act_admin_ads'), InlineKeyboardButton("🚫 Ban/Unban", callback_data='act_admin_ban')],
            [InlineKeyboardButton("🔙 Main Menu", callback_data='main_menu')]
        ]
        await query.message.edit_text("👨‍💻 **Admin Control Panel:**\n\n• Active Users: 1,240\n• Today Revenue: ৳1,500\n• System Status: Normal", reply_markup=InlineKeyboardMarkup(kb), parse_mode='Markdown')

    elif data == 'menu_security':
        kb = [[InlineKeyboardButton("🔙 Main Menu", callback_data='main_menu')]]
        text = "🛡️ **Security & Anti-Fraud:**\n\n✅ Duplicate Account Protection Active\n✅ Fake Referral Detection On\n✅ Withdrawal Verification Enabled"
        await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(kb), parse_mode='Markdown')

    else:
        kb = [[InlineKeyboardButton("🔙 Back", callback_data='main_menu')]]
        await query.message.edit_text(f"⚙️ **{data.replace('act_', '').upper()}** সার্ভিস বর্তমানে প্রসেসিংয়ে রয়েছে। ইনপুট পাঠান...", reply_markup=InlineKeyboardMarkup(kb), parse_mode='Markdown')

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("All Features Bot Started...")
    app.run_polling()

if __name__ == "__main__":
    main()
