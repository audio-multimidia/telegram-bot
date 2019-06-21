import json
from core.audio import audio_to_text


TRANSCRIPTS_FILE = "./src/test/transcripts.json"
AUDIOS_PATH = "./src/test/audios/"

def test_with_input ():
    with open(TRANSCRIPTS_FILE) as json_file:
        data = json.load(json_file)
        
        for key in data:
            print (data[key]["transcription"])
            print (audio_to_text(AUDIOS_PATH + key + ".wav"))



test_with_input()