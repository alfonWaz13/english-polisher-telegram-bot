import google.generativeai as genai


class EnglishPolisher:

    BASE_PROMPT = f"""
    You're an expert English teacher. I'm gonna send you a text that may or may not contain grammar or spelling
    mistakes. In case it sounds natural (as a native speaker would say it), just reply 'Sounds natural' Otherwise,
    correct the mistakes and provide a better version of the text. I don't want you to explain the mistakes, I just want
    the corrected text. Don't use markdown signs like ** and don't put the result between quotes.
    Text: {{user_text}}
    """

    def __init__(self, model: genai.GenerativeModel) -> None:
        self._model = model

    def polish(self, user_text: str) -> str:
        prompt = self.BASE_PROMPT.format(user_text=user_text)
        response = self._model.generate_content(prompt)
        return response.text
