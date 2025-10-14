import json
import logging

import google.generativeai as genai

from config import GOOGLE_AI_API_KEY, TELEGRAM_TOKEN
from english_polisher import EnglishPolisher
from telegram import Update
from telegram.ext import Application, ContextTypes, MessageHandler, filters

logger = logging.getLogger()
logger.setLevel(logging.INFO)

genai.configure(api_key=GOOGLE_AI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash-lite")
english_polisher = EnglishPolisher(model=model)

app = Application.builder().token(TELEGRAM_TOKEN).build()


async def polish_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    if text:
        logger.info("Received text: %s", text)
        polished_text = english_polisher.polish(text)
        await update.message.reply_text(polished_text)
        logger.info("Polished text sent successfully.")


app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, polish_message))


def lambda_handler(event, context):
    try:
        logger.info(f"Received event: {json.dumps(event)}")
        body = json.loads(event.get("body", "{}"))
        update = Update.de_json(body, app.bot)
        app.update_queue.put_nowait(update)
        return {"statusCode": 200, "body": json.dumps("Update processed successfully.")}

    except Exception as e:
        logger.error("Error processing message: %s", e)
        return {"statusCode": 500, "body": json.dumps("Error processing request.")}
