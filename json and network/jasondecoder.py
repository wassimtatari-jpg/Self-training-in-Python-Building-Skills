import json

from datetime import datetime

def custom_decoder(dec):
    if "timestamp" in dec : dec["timestamp"]=datetime.fromisoformat(dec["timestamp"])
    return dec


json_string = '''
{
    "name": "Alice",
    "timestamp": "2023-05-15T14:30:00"
}
'''

data=json.loads(json_string,object_hook=custom_decoder)
print(data)
