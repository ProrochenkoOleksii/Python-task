from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ReplyKeyboardMarkup
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    keyboard = [
        [InlineKeyboardButton("Interesting", callback_data="1")],
        [InlineKeyboardButton("Help", callback_data="2")],
        [InlineKeyboardButton("Contact", callback_data="3")],
        [InlineKeyboardButton("About us", callback_data="4")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_html(f"Hi {user.mention_html()}!\nPlease choose:", reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query

    await query.answer()
    if query.data=='1':
        # await query.edit_message_text(text=f" price 1\n price 2\n price 3")

        message_text = "<a href='https://kids.nationalgeographic.com/animals'> INTERESTING LINK </a>"
        await query.edit_message_text(text=message_text, parse_mode='HTML')
    elif query.data=='2':
        await query.edit_message_text(text=f"For help call 911")
    elif query.data=='3':
        await query.edit_message_text(text=f"Phone number: +3884329830")
    elif query.data=='4':
        await query.edit_message_text(text=f"All about us")



async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Use /start to test this bot.")


def main() -> None:
    application = Application.builder().token("6914507875:AAGdiuTBJhYEJa3j9gLEpu9_-b_elB2g-y4").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(CommandHandler("help", help_command))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()







