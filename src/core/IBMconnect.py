
from ibm_watson import SpeechToTextV1
from pydub import AudioSegment
import json
import config
from constants import *


speech_to_text = SpeechToTextV1(
    iam_apikey= config.get(WATSON_API_KEY),
    url= config.get(URL_SPEECH_TO_TEXT)
)

def audio_to_text(filePath):
    with open(filePath, 'rb') as audio_file:
        result = speech_to_text.recognize(
            audio_file, content_type='audio/wav', timestamps=True, model="pt-BR_NarrowbandModel",
            word_confidence=True, profanity_filer=False).get_result()
        if (result["error"]):
            return result["code_description"]
        else:
            return result['results'][0]['alternatives'][0]['timestamps']

blockedWords = {'estando': True, 'mano': True}
audio = AudioSegment.from_wav("test-pt.wav")

timestamps = audio_to_text('./test-pt.wav')
print(timestamps)
secs = 1000
edited = []

# for i in timestamps:
#     if not i[0] in blockedWords.keys():
#         edited.append(audio[i[1] * secs : i[2] * secs])