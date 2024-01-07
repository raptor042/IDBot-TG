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

from __api__.index import getUser, getIDBotNumber, getName, getDescription, getEmail, getAge, getCountry, getState, getPhone, getAddress, getScore, getProfilePic, getProjects

import logging

logging.basicConfig(format="%(asctime)s -%(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)
load_dotenv()

START, CONNECT, END = range(3)

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    try:
        user = update.message.from_user
        logger.info(f"{user.username} started a conversation.")

        context.user_data["username"] = user.username

        keyboard = [
            [InlineKeyboardButton("Connect your IDBot Account 🚀", callback_data="connect")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        reply_msg = f"<b>Hello {user.username} 🎉, Welcome to the IDBot Protocol 🤖.</b>\n\n<b>Problem Statement:</b>\n<i>In an era of rapid digital innovation, the rise of fraudulent projects and scams has become a critical concern. Investors are increasingly vulnerable to deceitful practices, and establishing trust has never been more challenging.</i>\n\n<b>Solution Overview:</b>\n<i>IDBot emerges as a beacon of trust in this digital landscape. Through decentralized identity verification, cutting-edge cryptography, and a robust anti-scam protocol, IDBot redefines how trust is built and maintained in online interactions.</i>"

        await update.message.reply_html(text=reply_msg, reply_markup=reply_markup)

        return START
    except Exception as e:
        print(e)
        logging.error("An error occured while processing this command.")

        reply_msg = f"<b>🚨 {user.username}, An error occured while processing your request.</b>"
        await update.message.reply_html(text=reply_msg)

async def connect(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    username = context.user_data["username"]
    logger.info(f"{username} is connecting IDBot Identity.")

    keyboard = [
        [InlineKeyboardButton("Connect via Wallet Address 👾", callback_data="connect-wallet")],
        [InlineKeyboardButton("Connect via IDBot Number 🤖", callback_data="connect-id")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    reply_msg = f"<b>🔰 You can conect your IDBot account in two ways:</b>\n\n<i>✅ Via your Wallet Address</i>\n<i>✅ Via your IDBot Number</i>\n\n<b>🚨 Make your the address or number you enter is correct and the same you used when creating your IDBot account.</b>"

    await query.message.reply_html(text=reply_msg, reply_markup=reply_markup)

    return CONNECT

async def connect_wallet(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    username = context.user_data["username"]
    logger.info(f"{username} is connecting wallet address.")

    reply_msg = f"<b>🔰 Enter your wallet address?</b>\n\n<i>🚨 Make your the address or number you enter is correct and the same you used when creating your IDBot account.</i>"

    await query.message.reply_html(text=reply_msg)

    return CONNECT

async def connect_id(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    username = context.user_data["username"]
    logger.info(f"{username} is connecting IDBot Number")

    reply_msg = f"<b>🔰 Enter your IDBot number?</b>\n\n<i>🚨 Make your the address or number you enter is correct and the same you used when creating your IDBot account.</i>"

    await query.message.reply_html(text=reply_msg)

    return CONNECT

async def connectWallet(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    logger.info(f"{user.username} connected wallet address.")

    print(update.message.text.strip())

    idbot_number = getIDBotNumber(update.message.text.strip())
    print(idbot_number)

    context.user_data["profile"] = update.message.text.strip()
    context.user_data["id"] = idbot_number
    print(context.user_data["profile"], context.user_data["id"])

    keyboard = [
        [InlineKeyboardButton("End Conversation 👋", callback_data="end")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    reply_msg = f"<b>Congratulations {user.username} 🎉, You have successfully connected your wallet address to the IDBot 👾.</b>"

    await update.message.reply_html(text=reply_msg, reply_markup=reply_markup)

    return CONNECT

async def connectID(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    logger.info(f"{user.username} connected wallet address.")

    print(update.message.text.strip())

    profile = getUser(update.message.text.strip())
    print(profile)

    context.user_data["id"] = update.message.text.strip()
    context.user_data["profile"] = profile
    print(context.user_data["id"], context.user_data["profile"])

    keyboard = [
        [InlineKeyboardButton("End Conversation 👋", callback_data="end")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    reply_msg = f"<b>Congratulations {user.username} 🎉, You have successfully connected your IDBot number to the IDBot 👾.</b>"

    await update.message.reply_html(text=reply_msg, reply_markup=reply_markup)

    return CONNECT

async def end(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    username = context.user_data["username"]
    logger.info(f"{username} ended the conversation.")

    reply_msg = f"<b>See you soon {username} 👋.</b>\n\n<b>Why IDBot?</b>\n<b>1.Decentralization: </b><i>Trust is no longer vested in centralized entities, mitigating single points of failure and reducing the risk of breaches.</i>\n\n<b>Zero-Knowledge Proofs: </b><i> Users can validate their identity without exposing sensitive information, ensuring privacy and security.</i>\n\n<b>Selective Disclosure: </b><i>Empowers users to control the information they share, enhancing privacy and user autonomy.</i>\n\n<b>Anti-Scam Protocol: </b><i> Vigilant measures are in place to detect and prevent fraudulent activities, safeguarding investors.</i>"

    await query.message.reply_html(reply_msg)

    return END

async def name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user = update.message.from_user
        logger.info(f"{user.username} is querying for name info.")

        args = context.args

        if len(args) == 1:
            name = getName(args[0])
            print(name)

            reply_msg = f"<i>🔰 The name associated with the profile is '<b>{name}</b>'</i>"
            await update.message.reply_html(text=reply_msg)
        else:
            name = getName(context.user_data["profile"])
            print(name)

            reply_msg = f"<i>🔰 The name associated with your profile is '<b>{name}</b>'</i>"
            await update.message.reply_html(text=reply_msg)
    except Exception as e:
        print(e)
        logging.error("An error occured while processing this command.")

        reply_msg = f"<b>🚨 {user.username}, An error occured while processing your request.</b>"
        await update.message.reply_html(text=reply_msg)

async def description(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user = update.message.from_user
        logger.info(f"{user.username} is querying for description info.")

        args = context.args

        if len(args) == 1:
            description = getDescription(args[0])
            print(description)

            reply_msg = f"<i>🔰 The description associated with the profile is '<b>{description}</b>'</i>"
            await update.message.reply_html(text=reply_msg)
        else:
            description = getDescription(context.user_data["profile"])
            print(description)

            reply_msg = f"<i>🔰 The description associated with your profile is '<b>{description}</b>'</i>"
            await update.message.reply_html(text=reply_msg)
    except Exception as e:
        print(e)
        logging.error("An error occured while processing this command.")

        reply_msg = f"<b>🚨 {user.username}, An error occured while processing your request.</b>"
        await update.message.reply_html(text=reply_msg)

async def email(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user = update.message.from_user
        logger.info(f"{user.username} is querying for email info.")

        args = context.args

        if len(args) == 1:
            email = getEmail(args[0])
            print(email)

            reply_msg = f"<i>🔰 The email associated with the profile is '<b>{email}</b>'</i>"
            await update.message.reply_html(text=reply_msg)
        else:
            email = getEmail(context.user_data["profile"])
            print(email)

            reply_msg = f"<i>🔰 The email associated with your profile is '<b>{email}</b>'</i>"
            await update.message.reply_html(text=reply_msg)
    except Exception as e:
        print(e)
        logging.error("An error occured while processing this command.")

        reply_msg = f"<b>🚨 {user.username}, An error occured while processing your request.</b>"
        await update.message.reply_html(text=reply_msg)

async def age(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user = update.message.from_user
        logger.info(f"{user.username} is querying for age info.")

        args = context.args

        if len(args) == 1:
            age = getAge(args[0])
            print(age)

            reply_msg = f"<i>🔰 The age associated with the profile is '<b>{age}</b>'</i>"
            await update.message.reply_html(text=reply_msg)
        else:
            age = getAge(context.user_data["profile"])
            print(age)

            reply_msg = f"<i>🔰 The age associated with your profile is '<b>{age}</b>'</i>"
            await update.message.reply_html(text=reply_msg)
    except Exception as e:
        print(e)
        logging.error("An error occured while processing this command.")

        reply_msg = f"<b>🚨 {user.username}, An error occured while processing your request.</b>"
        await update.message.reply_html(text=reply_msg)

async def country(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user = update.message.from_user
        logger.info(f"{user.username} is querying for country info.")

        args = context.args

        if len(args) == 1:
            country = getCountry(args[0])
            print(country)

            reply_msg = f"<i>🔰 The country associated with the profile is '<b>{country}</b>'</i>"
            await update.message.reply_html(text=reply_msg)
        else:
            country = getCountry(context.user_data["profile"])
            print(country)

            reply_msg = f"<i>🔰 The country associated with your profile is '<b>{country}</b>'</i>"
            await update.message.reply_html(text=reply_msg)
    except Exception as e:
        print(e)
        logging.error("An error occured while processing this command.")

        reply_msg = f"<b>🚨 {user.username}, An error occured while processing your request.</b>"
        await update.message.reply_html(text=reply_msg)

async def state(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user = update.message.from_user
        logger.info(f"{user.username} is querying for state info.")

        args = context.args

        if len(args) == 1:
            state = getState(args[0])
            print(state)

            reply_msg = f"<i>🔰 The state associated with the profile is '<b>{state}</b>'</i>"
            await update.message.reply_html(text=reply_msg)
        else:
            state = getState(context.user_data["profile"])
            print(state)

            reply_msg = f"<i>🔰 The state associated with your profile is '<b>{state}</b>'</i>"
            await update.message.reply_html(text=reply_msg)
    except Exception as e:
        print(e)
        logging.error("An error occured while processing this command.")

        reply_msg = f"<b>🚨 {user.username}, An error occured while processing your request.</b>"
        await update.message.reply_html(text=reply_msg)

async def phone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user = update.message.from_user
        logger.info(f"{user.username} is querying for phone info.")

        args = context.args

        if len(args) == 1:
            phone = getPhone(args[0])
            print(phone)

            reply_msg = f"<i>🔰 The phone associated with the profile is '<b>{phone}</b>'</i>"
            await update.message.reply_html(text=reply_msg)
        else:
            phone = getPhone(context.user_data["profile"])
            print(phone)

            reply_msg = f"<i>🔰 The phone associated with your profile is '<b>{phone}</b>'</i>"
            await update.message.reply_html(text=reply_msg)
    except Exception as e:
        print(e)
        logging.error("An error occured while processing this command.")

        reply_msg = f"<b>🚨 {user.username}, An error occured while processing your request.</b>"
        await update.message.reply_html(text=reply_msg)

async def address(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user = update.message.from_user
        logger.info(f"{user.username} is querying for address info.")

        args = context.args

        if len(args) == 1:
            address = getAddress(args[0])
            print(address)

            reply_msg = f"<i>🔰 The address associated with the profile is '<b>{address}</b>'</i>"
            await update.message.reply_html(text=reply_msg)
        else:
            address = getAddress(context.user_data["profile"])
            print(address)

            reply_msg = f"<i>🔰 The address associated with your profile is '<b>{address}</b>'</i>"
            await update.message.reply_html(text=reply_msg)
    except Exception as e:
        print(e)
        logging.error("An error occured while processing this command.")

        reply_msg = f"<b>🚨 {user.username}, An error occured while processing your request.</b>"
        await update.message.reply_html(text=reply_msg)

async def profile_pic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user = update.message.from_user
        logger.info(f"{user.username} is querying for profile_pic info.")

        args = context.args

        if len(args) == 1:
            profile_pic = getProfilePic(args[0])
            print(profile_pic)

            reply_msg = f"<i>🔰 The profile_pic associated with the profile is '<b>{profile_pic}</b>'</i>"
            await update.message.reply_html(text=reply_msg)
        else:
            profile_pic = getProfilePic(context.user_data["profile"])
            print(profile_pic)

            reply_msg = f"<i>🔰 The profile_pic associated with your profile is '<b>{profile_pic}</b>'</i>"
            await update.message.reply_html(text=reply_msg)
    except Exception as e:
        print(e)
        logging.error("An error occured while processing this command.")

        reply_msg = f"<b>🚨 {user.username}, An error occured while processing your request.</b>"
        await update.message.reply_html(text=reply_msg)

async def score(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user = update.message.from_user
        logger.info(f"{user.username} is querying for score info.")

        args = context.args

        if len(args) == 1:
            score = getScore(args[0])
            print(score)

            reply_msg = f"<i>🔰 The score associated with the profile is '<b>{score}</b>'</i>"
            await update.message.reply_html(text=reply_msg)
        else:
            score = getScore(context.user_data["profile"])
            print(score)

            reply_msg = f"<i>🔰 The score associated with your profile is '<b>{score}</b>'</i>"
            await update.message.reply_html(text=reply_msg)
    except Exception as e:
        print(e)
        logging.error("An error occured while processing this command.")

        reply_msg = f"<b>🚨 {user.username}, An error occured while processing your request.</b>"
        await update.message.reply_html(text=reply_msg)

async def projects(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user = update.message.from_user
        logger.info(f"{user.username} is querying for projects info.")

        args = context.args

        if len(args) == 1:
            projects = getProjects(args[0])

            if(len(projects["projects"]) > 0):
                reply_msg = f"<i>🔰 The profile has '<b>{len(projects['projects'])}</b>' project(s) 🚀.</i>\n\n"

                for project in projects["projects"]:
                    reply_msg += f"<b>🎖 Name : </b><i>{project[0]}</i>\n<b>📝 Description : </b><i>{project[1]}</i>\n<b>📍 Contract Address : </b><i>{project[2]}</i>\n<b>🛡 Blockchain : </b><i>{project[3]}</i>\n<b>📌 Linktree : </b><i>{project[4]}</i>\n<b>📉 HoneyPot : </b><i>{project[5]}</i>\n<b>📈 Rugged : </b><i>{project[6]}</i>\n<b>🏅 Reputation Score : </b><i>{project[7]}</i>\n\n"

                    await update.message.reply_html(text=reply_msg)
            else:
                reply_msg = f"<i>🔰 The profile has '<b>{len(projects['projects'])}</b>' project(s).</i>"
                await update.message.reply_html(text=reply_msg)
        else:
            projects = getProjects(context.user_data["profile"])

            if(len(projects["projects"]) > 0):
                reply_msg = f"<i>🔰 Your profile has '<b>{len(projects['projects'])}</b>' project(s) 🚀.</i>\n\n"

                reply_msg += f"<b>🎖 Name : </b><i>{project[0]}</i>\n<b>📝 Description : </b><i>{project[1]}</i>\n<b>📍 Contract Address : </b><i>{project[2]}</i>\n<b>🛡 Blockchain : </b><i>{project[3]}</i>\n<b>📌 Linktree : </b><i>{project[4]}</i>\n<b>📉 HoneyPot : </b><i>{project[5]}</i>\n<b>📈 Rugged : </b><i>{project[6]}</i>\n<b>🏅 Reputation Score : </b><i>{project[7]}</i>\n\n"

                await update.message.reply_html(text=reply_msg)
            else:
                reply_msg = f"<i>🔰 Your profile has '<b>{len(projects['projects'])}</b>' project(s).</i>"
                await update.message.reply_html(text=reply_msg)
    except Exception as e:
        print(e)
        logging.error("An error occured while processing this command.")

        reply_msg = f"<b>🚨 {user.username}, An error occured while processing your request.</b>"
        await update.message.reply_html(text=reply_msg)

def main() -> None:
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            START: [
                CallbackQueryHandler(start, pattern="^start$"),
                CallbackQueryHandler(connect, pattern="^connect$")
            ],
            CONNECT: [
                CallbackQueryHandler(connect_wallet, pattern="^connect-wallet$"),
                CallbackQueryHandler(connect_id, pattern="^connect-id$"),
                MessageHandler(filters.Regex("^0x"), connectWallet),
                MessageHandler(filters.Regex("[0-9]"), connectID)
            ],
            END: [
                CallbackQueryHandler(end, pattern="^end$")
            ]
        },
        fallbacks=[CallbackQueryHandler(end, pattern="^end$")]
    )

    name_handler = CommandHandler("name", name)
    description_handler = CommandHandler("description", description)
    email_handler = CommandHandler("email", email)
    age_handler = CommandHandler("age", age)
    country_handler = CommandHandler("country", country)
    state_handler = CommandHandler("state", state)
    phone_handler = CommandHandler("phone", phone)
    address_handler = CommandHandler("address", address)
    profile_pic_handler = CommandHandler("profile_pic", profile_pic)
    score_handler = CommandHandler("score", score)
    projects_handler = CommandHandler("projects", projects)

    app.add_handler(conv_handler)
    app.add_handler(name_handler)
    app.add_handler(description_handler)
    app.add_handler(email_handler)
    app.add_handler(age_handler)
    app.add_handler(country_handler)
    app.add_handler(state_handler)
    app.add_handler(phone_handler)
    app.add_handler(address_handler)
    app.add_handler(profile_pic_handler)
    app.add_handler(score_handler)
    app.add_handler(projects_handler)

    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()