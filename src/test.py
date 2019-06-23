import json
from core.audio import audio_to_text
from core.audio import recognize_keywords

TRANSCRIPTS_FILE = "./src/test/transcripts.json"
AUDIOS_PATH = "./src/test/audios/"

def test_audio_to_text ():
    with open(TRANSCRIPTS_FILE) as json_file:
        data = json.load(json_file)
        
        for key in data:
            print (data[key]["transcription"])
            print (audio_to_text(AUDIOS_PATH + key + ".wav"))

def test_reconigze_words ():
    with open(TRANSCRIPTS_FILE) as json_file:
        data = json.load(json_file)
        
        for key in data:
            print (data[key]["transcription"])
            print (data[key]["keywords"])
            print (recognize_keywords(AUDIOS_PATH + key + ".wav", data[key]["keywords"]))


# test_reconigze_words()
# test_audio_to_text()