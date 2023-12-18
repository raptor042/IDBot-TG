import os
from dotenv import load_dotenv

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    ConversationHandler,
    filters
)

import logging

from __web3__.index import create_did_IDBot

logging.basicConfig(format="%(asctime)s -%(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)
load_dotenv()

START, CREATE, END = range(3)

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    logger.info(f"{user.username} started a conversation.")

    context.user_data["username"] = user.username

    keyboard = [
        [InlineKeyboardButton("Connect your DIDBot Identity 🚀", callback_data="connect")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    reply_msg = f"<b>Hello {user.username} 🎉, Welcome to the IDBot Protocol 🤖,</b>\n\n<b>Problem Statement:</b>\n<i>In an era of rapid digital innovation, the rise of fraudulent projects and scams has become a critical concern. Investors are increasingly vulnerable to deceitful practices, and establishing trust has never been more challenging.</i>\n\n<b>Solution Overview:</b>\n<i>IDBot emerges as a beacon of trust in this digital landscape. Through decentralized identity verification, cutting-edge cryptography, and a robust anti-scam protocol, IDBot redefines how trust is built and maintained in online interactions.</i>"

    await update.message.reply_html(text=reply_msg, reply_markup=reply_markup)

    return START

async def connect(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    username = context.user_data["username"]
    logger.info(f"{username} is creating a DIDBot Identity.")

    keyboard = [
        [InlineKeyboardButton("YES", callback_data="dev-yes")],
        [InlineKeyboardButton("NO", callback_data="dev-no")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    reply_msg = f"<b>Are you are Web3 Developer 👾?</b>"

    await query.message.reply_html(text=reply_msg, reply_markup=reply_markup)

    return CREATE

async def end(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    username = context.user_data["username"]
    logger.info(f"{username} ended the conversation.")

    reply_msg = f"<b>See you soon {username} 👋.</b>\n\n<b>Why IDBot?</b>\n<b>1.Decentralization: </b><i>Trust is no longer vested in centralized entities, mitigating single points of failure and reducing the risk of breaches.</i>\n\n<b>Zero-Knowledge Proofs: </b><i> Users can validate their identity without exposing sensitive information, ensuring privacy and security.</i>\n\n<b>Selective Disclosure: </b><i>Empowers users to control the information they share, enhancing privacy and user autonomy.</i>\n\n<b>Anti-Scam Protocol: </b><i> Vigilant measures are in place to detect and prevent fraudulent activities, safeguarding investors.</i>"

    await query.message.reply_html(reply_msg)

    return END

def main() -> None:
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            START: [
                CallbackQueryHandler(start, pattern="^start$"),
                CallbackQueryHandler(create, pattern="^connect$")
            ],
            CREATE: [
                CallbackQueryHandler(dev, pattern="^dev-"),
            ],
            END: [
                CallbackQueryHandler(end, pattern="^end$")
            ]
        },
        fallbacks=[CallbackQueryHandler(end, pattern="^end$")]
    )

    app.add_handler(conv_handler)

    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()