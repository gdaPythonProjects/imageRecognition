

import os

from google.cloud import translate
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "api_key.json"


class Translator():

    def translate(self, word):
        translate_client = translate.Client()

        text = word
        target = 'pl'

        translation = translate_client.translate(
            text,
            target_language=target)
        return translation['translatedText']