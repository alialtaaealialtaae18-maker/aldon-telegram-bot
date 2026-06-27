from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "ضع_التوكن_الجديد_هنا"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("🎁 بونص ترحيبي", callback_data="bonus"),
            InlineKeyboardButton("💳 حسابات مجانية", callback_data="accounts")
        ],
        [
            InlineKeyboardButton("🔥 عروض", callback_data="offers"),
            InlineKeyboardButton("💰 مواقع وبوتات الربح", callback_data="sites")
        ],
        [
            InlineKeyboardButton("📢 قنوات التوصيات", callback_data="channels")
        ]
    ]

    await update.message.reply_text(
        "👑 ALDON | الدون\n\n"
        "مرحبًا بك في البوت الرسمي\n\n"
        "اختر الخدمة المطلوبة:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "bonus":
        text = "🎁 هنا ستظهر جميع البونصات الترحيبية."

    elif query.data == "accounts":
        text = "💳 هنا ستظهر الحسابات المجانية."

    elif query.data == "offers":
        text = "🔥 هنا ستظهر جميع العروض."

    elif query.data == "sites":
        text = "💰 هنا ستظهر مواقع وبوتات الربح."

    elif query.data == "channels":
        text = "📢 هنا ستظهر قنوات التوصيات."

    else:
        text = "غير معروف"

    await query.edit_message_text(text)


app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(buttons))

app.run_polling()
