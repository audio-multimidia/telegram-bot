import json
from constants import *

with open(CONFIG_FILE) as json_file:  
    data = json.load(json_file)
    
def get(key):
    return data[key]