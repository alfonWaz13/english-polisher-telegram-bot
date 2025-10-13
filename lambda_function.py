import json
import logging
import os

import google.generativeai as genai
import requests

from config import GOOGLE_AI_API_KEY, TELEGRAM_TOKEN
from english_polisher import EnglishPolisher

logger = logging.getLogger()
logger.setLevel(logging.INFO)

genai.configure(api_key=GOOGLE_AI_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash-lite')
english_polisher = EnglishPolisher(model=model)


def lambda_handler(event, context):
    try:
        logger.info(f"Received event: {json.dumps(event)}")
        body = json.loads(event.get('body', "{}"))
        message = body.get('message', {})
        chat_id = message.get('chat', {}).get('id')
        text = message.get('text', '')

        if text:
            logger.info("Received text: %s", text)
            polished_text = english_polisher.polish(text)
            logger.info("Polished text: %s. Sending response to chat_id: %s", polished_text, chat_id)

            requests.post(f"https://api.telegram.org/bot{os.environ.get(TELEGRAM_TOKEN)}/sendMessage",
                        json={"chat_id": chat_id, "text": polished_text})
            logger.info("Response sent successfully.")

        return {
            'statusCode': 200,
            'body': json.dumps('Update processed successfully.')
        }

    except Exception as e:
        logger.error("Error processing message: %s", e)
        return {
            'statusCode': 500,
            'body': json.dumps('Error processing request.')
        }