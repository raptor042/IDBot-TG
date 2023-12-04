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
        [InlineKeyboardButton("Create DIDBot Identity 🚀", callback_data="create")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    reply_msg = f"<b>Hello {user.username} 🎉, Welcome to the IDBot Protocol 🤖,</b>\n\n<b>Problem Statement:</b>\n<i>In an era of rapid digital innovation, the rise of fraudulent projects and scams has become a critical concern. Investors are increasingly vulnerable to deceitful practices, and establishing trust has never been more challenging.</i>\n\n<b>Solution Overview:</b>\n<i>IDBot emerges as a beacon of trust in this digital landscape. Through decentralized identity verification, cutting-edge cryptography, and a robust anti-scam protocol, IDBot redefines how trust is built and maintained in online interactions.</i>"

    await update.message.reply_html(text=reply_msg, reply_markup=reply_markup)

    return START

async def create(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
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

async def dev(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    [_, data] = query.data.split("-", 1)
    print(data)

    username = context.user_data["username"]
    logger.info(f"{username} is a DEV.") if data == "yes" else logger.info(f"{username} is not a DEV.")

    reply_msg = f"<b>What is your Full Name ?</b>\n\n<b>🚨 Warning:</b>\n<i>When entering your please do so in this format:</i>\n\n<b>Name:...Your Full Name....</b>\n\n<i>🚫 If you do not use this format, your name will not be recognized!!!</i>"

    await query.message.reply_html(text=reply_msg)

    return CREATE

async def name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    logger.info(f"{user.username} entered his/her name.")

    [_, text] = update.message.text.split(":", 1)
    print(text)

    context.user_data["full-name"] = text.strip()

    reply_msg = f"<b>What is your Email Address ?</b>\n\n<b>🚨 Warning:</b>\n<i>When entering your please do so in this format:</i>\n\n<b>Email:...Your Email Address....</b>\n\n<i>🚫 If you do not use this format, your name will not be recognized!!!</i>"

    await update.message.reply_html(text=reply_msg)

    return CREATE

async def email(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    logger.info(f"{user.username} entered his/her email address.")

    [_, text] = update.message.text.split(":", 1)
    print(text)

    context.user_data["email-address"] = text.strip()

    reply_msg = f"<b>What is your Phone Number ?</b>\n\n<b>🚨 Warning:</b>\n<i>When entering your please do so in this format:</i>\n\n<b>Phone:...Your Phone Number....</b>\n\n<i>🚫 If you do not use this format, your name will not be recognized!!!</i>"

    await update.message.reply_html(text=reply_msg)

    return CREATE

async def phone(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    logger.info(f"{user.username} entered his/her age.")

    [_, text] = update.message.text.split(":", 1)
    print(text)

    context.user_data["phone-number"] = text.strip()

    reply_msg = f"<b>What is your Legal Age ?</b>\n\n<b>🚨 Warning:</b>\n<i>When entering your please do so in this format:</i>\n\n<b>Age:...Your Age....</b>\n\n<i>🚫 If you do not use this format, your name will not be recognized!!!</i>"

    await update.message.reply_html(text=reply_msg)

    return CREATE

async def age(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    logger.info(f"{user.username} entered his/her phone number.")

    [_, text] = update.message.text.split(":", 1)
    print(text)

    context.user_data["age"] = text.strip()

    reply_msg = f"<b>Which Country do you reside in ?</b>\n\n<b>🚨 Warning:</b>\n<i>When entering your please do so in this format:</i>\n\n<b>Country:...Your Country....</b>\n\n<i>🚫 If you do not use this format, your name will not be recognized!!!</i>"

    await update.message.reply_html(text=reply_msg)

    return CREATE

async def country(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    logger.info(f"{user.username} entered his/her country.")

    [_, text] = update.message.text.split(":", 1)
    print(text)

    context.user_data["country"] = text.strip()

    reply_msg = f"<b>Which State do you reside in ?</b>\n\n<b>🚨 Warning:</b>\n<i>When entering your please do so in this format:</i>\n\n<b>State:...Your State....</b>\n\n<i>🚫 If you do not use this format, your name will not be recognized!!!</i>"

    await update.message.reply_html(text=reply_msg)

    return CREATE

async def state(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    logger.info(f"{user.username} entered his/her state.")

    [_, text] = update.message.text.split(":", 1)
    print(text)

    context.user_data["state"] = text.strip()

    reply_msg = f"<b>What is your Passport Number ?</b>\n\n<b>🚨 Warning:</b>\n<i>When entering your please do so in this format:</i>\n\n<b>Passport:...Your Passport Number....</b>\n\n<i>🚫 If you do not use this format, your name will not be recognized!!!</i>"

    await update.message.reply_html(text=reply_msg)

    return CREATE

async def passport(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    logger.info(f"{user.username} entered his/her passort number.")

    [_, text] = update.message.text.split(":", 1)
    print(text)

    context.user_data["passort-number"] = text.strip()

    data = {
        "name" : context.user_data["full-name"],
        "email" : context.user_data["email-address"],
        "phone" : context.user_data["phone-number"],
        "age" : context.user_data["age"],
        "country" : context.user_data["country"],
        "state" : context.user_data["state"],
        "passport" : context.user_data["passort-number"]
    }

    JSON = create_did_IDBot(data=data)
    print(JSON)

    keyboard = [
        [InlineKeyboardButton("End Conversation 👋", callback_data="end")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    reply_msg = f"<b>Congratulations {user.username} 🎉, Your Decentralized IDBot Identity has been successfully created 👾.</b>\n\n"

    await update.message.reply_html(text=reply_msg, reply_markup=reply_markup)

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
                CallbackQueryHandler(create, pattern="^create$")
            ],
            CREATE: [
                CallbackQueryHandler(dev, pattern="^dev-"),
                MessageHandler(filters.Regex("^Name:"), name),
                MessageHandler(filters.Regex("^Email:"), email),
                MessageHandler(filters.Regex("^Phone:"), phone),
                MessageHandler(filters.Regex("^Age:"), age),
                MessageHandler(filters.Regex("^Country:"), country),
                MessageHandler(filters.Regex("^State:"), state),
                MessageHandler(filters.Regex("^Passport:"), passport),
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