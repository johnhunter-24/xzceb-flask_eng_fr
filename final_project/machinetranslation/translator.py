import os
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv


load_dotenv()

my_api_key = os.environ['apikey']
my_url = os.environ['url']
my_version = os.environ['version']


authenticator = IAMAuthenticator(my_api_key)
language_translator = LanguageTranslatorV3(
    version = my_version,
    authenticator = authenticator
)

language_translator.set_service_url(my_url)


def english_to_french(english_text):
    try:
        translation = language_translator.translate(
            text = english_text,
            model_id = 'en-fr').get_result()

        french_text = translation['translations'][0]['translation']
        return french_text
    except ApiException as ex:
        error = "Method failed with status code " + str(ex.code) + ": " + ex.message
        return error


def french_to_english(french_text):
    try:
        translation = language_translator.translate(
            text = french_text,
            model_id = 'fr-en').get_result()
        english_text = translation['translations'][0]['translation']
        return english_text
    except ApiException as ex:
        error = "Method failed with status code " + str(ex.code) + ": " + ex.message
        return error
