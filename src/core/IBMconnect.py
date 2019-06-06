
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
        print(result)
        if ("error" in result.keys()):
            return result["code_description"]
        else:
            return result['results']

blockedWords = { 'cu': True, 'porra': True } # Mock

audio = AudioSegment.from_wav("test-pt.wav") # original audio
timestamps = [] # Timestamps
response = audio_to_text('./test-pt.wav')
for i in response:
    for j in (i['alternatives'][0]['timestamps']):
        timestamps.append(j)
secs = 1000
edited = AudioSegment.empty()
for i in timestamps:
    print(i)
    if not i[0] in blockedWords.keys():
        edited += audio[i[1] * secs : i[2] * secs] # Concat with chunck that is not blocked

print(edited) # final audio 
edited.export("./result.wav", format="wav")