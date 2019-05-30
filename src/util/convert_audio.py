from pydub import AudioSegment
from constants import *

def ogg_to_mp3 (fileName):
    audio = AudioSegment.from_ogg(PATH + fileName)

    new_path = PATH + fileName.replace(OGG_EXTENSION, MP3_EXTENSION)
    audio.export(new_path, format=MP3)
    
    return new_path

def mp3_to_ogg (fileName):
    audio = AudioSegment.from_mp3(PATH + fileName)

    new_path = PATH + fileName.replace(MP3_EXTENSION, OGG_EXTENSION)
    audio.export(new_path, format=OGG)
    
    return new_path