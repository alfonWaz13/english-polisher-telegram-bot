import asyncio
import json
import logging
import traceback

import google.generativeai as genai

from config import GOOGLE_AI_API_KEY, TELEGRAM_TOKEN
from english_polisher import EnglishPolisher
from telegram import Update
from telegram.ext import Application, ContextTypes, MessageHandler, filters, CommandHandler

logger = logging.getLogger()
logger.setLevel(logging.INFO)

genai.configure(api_key=GOOGLE_AI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash-lite")
english_polisher = EnglishPolisher(model=model)

app = Application.builder().token(TELEGRAM_TOKEN).build()


async def explanation_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Hey! I'm here to help. Drop me a message to check if it sounds natural in English. Also, you can put a sentence "
        "in other language and get a natural English translation"
    )


async def polish_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    if text:
        logger.info("Received text: %s", text)
        polished_text = english_polisher.polish(text)
        await update.message.reply_text(polished_text)
        logger.info("Polished text sent successfully.")


app.add_handler(CommandHandler("start", explanation_command))
app.add_handler(MessageHandler(filters.TEXT, polish_message))


async def bot_main(telegram_app: Application, event) -> None:
    async with telegram_app:
        await telegram_app.process_update(Update.de_json(json.loads(event["body"]), telegram_app.bot))


def lambda_handler(event, context):
    try:
        logger.info(f"Received event: {json.dumps(event)}")
        asyncio.run(bot_main(app, event))

    except Exception as e:
        traceback.print_exc()
        logger.error("Error processing message: %s", e)
        return {"statusCode": 500, "body": json.dumps("Error processing request.")}
