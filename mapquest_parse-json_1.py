import urllib.parse
import requests
main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Roma, Italia"
dest = "Frascati, Italia"
key = "ddwXo09jT2z6OxAfkqZqZ3jz69fmYYSB"
url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
json_data = requests.get(url).json()
print(json_data)
