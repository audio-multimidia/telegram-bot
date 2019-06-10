import logging

from pydub import AudioSegment
from constants import *

def ogg_to_wav (fileName):
    logging.info("Converting " + fileName + " to wav")

    audio = AudioSegment.from_ogg(PATH + fileName)

    new_path = PATH + fileName.replace(OGG_EXTENSION, WAV_EXTENSION)
    audio.export(new_path, format=WAV, tags={"artist": "@WordBlocker"})
    
    logging.info (fileName + " converted to " + new_path)
    return new_path