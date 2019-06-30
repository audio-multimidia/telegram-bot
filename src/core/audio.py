
import logging

from ibm_watson import SpeechToTextV1
from pydub import AudioSegment
from pydub.generators import Sine
import json
import config
from constants import *

bip = Sine(500)

speech_to_text = SpeechToTextV1(
    iam_apikey= config.get(WATSON_API_KEY),
    url= config.get(URL_SPEECH_TO_TEXT)
)

def audio_to_text(filePath):
    with open(filePath, 'rb') as audio_file:
        logging.info ("Executing speech to text")

        result = speech_to_text.recognize(
            audio_file, content_type='audio/wav', timestamps=True, model="pt-BR_NarrowbandModel",
            word_confidence=True, profanity_filter=False).get_result()

        if ("error" in result.keys()):
            return result["code_description"]
        else:
            return result['results']

def recognize_keywords(filePath, keywords):
    with open(filePath, 'rb') as audio_file:
        logging.info ("Executing speech to text")

        result = speech_to_text.recognize(
            audio_file, content_type='audio/wav', timestamps=True, model="pt-BR_NarrowbandModel",
            keywords=keywords, keywords_threshold=0.5, profanity_filer=False).get_result()

        if ("error" in result.keys()):
            return result["code_description"]["keywords_result"]
        else:
            return result['results']


def word_block_audio(filePath, blockedWords):
    audio = AudioSegment.from_wav(filePath) # original audio
    timestamps = [] # Timestamps
    response = audio_to_text(filePath)


    for i in response:
        for j in (i['alternatives'][0]['timestamps']):
            logging.info ("Found word: ")
            logging.info (j)
            timestamps.append(j)


    secs = 1000
    edited = AudioSegment.empty()

    logging.info ("Cropping audio")
    for i in timestamps:
        if not i[0] in blockedWords.keys():
            edited += audio[i[1] * secs : i[2] * secs] # Concat with chunck that is not blocked
        else:
            edited += bip.to_audio_segment((i[2] - i[1]) * secs)
    
    new_audio_path = filePath.replace(WAV_EXTENSION, "-result.wav")
    
    logging.info ("Exporting file " + new_audio_path)
    edited.export(new_audio_path, format=WAV)

    logging.info ("Returning audio")
    return new_audio_path