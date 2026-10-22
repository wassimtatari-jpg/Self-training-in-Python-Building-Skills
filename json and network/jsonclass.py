import json
from datetime import datetime

class Customcode(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,datetime):return obj.isoformat()
        return super().default(obj)

data = {
    "name": "Alice",
    "timestamp": datetime.now()
}

string_json=json.dumps(data,cls=Customcode,indent=4)
print(string_json)
