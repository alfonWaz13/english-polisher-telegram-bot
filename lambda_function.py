import json
import logging

import google.generativeai as genai

from config import GOOGLE_AI_API_KEY
from english_polisher import EnglishPolisher

logger = logging.getLogger()
logger.setLevel(logging.INFO)

genai.configure(api_key=GOOGLE_AI_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash-lite')
english_polisher = EnglishPolisher(model=model)


def lambda_handler(event, context):
    try:
        return {
            'statusCode': 200,
            'body': json.dumps('Update processed successfully.')
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps('Error processing request.')
        }