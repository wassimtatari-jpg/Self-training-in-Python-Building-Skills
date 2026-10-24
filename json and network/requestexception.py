import requests

try:
    reponse=requests.get("https://openlibrary.org/search.json?q=bad+war")
    reponse.raise_for_status()
except requests.HTTPError as err:
    print(f"HTTP Error ocurred {err}")
except Exception as err:
    print(f"Error {err} ocurred")
else:
    print("success")