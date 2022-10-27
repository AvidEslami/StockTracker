import http.client
import json
import time

conn = http.client.HTTPSConnection("twelve-data1.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "6a64084255msh51ad42634a01a45p11b294jsnabe18ede9956",
    'X-RapidAPI-Host': "twelve-data1.p.rapidapi.com"
    }

#take in previous values to return to working state
KeyValues = {}
with open("./StockTrack/values.json") as olData:
    oldVals = json.load(olData)
    KeyValues['money'] = int(oldVals["money"])

#get updated values to compare with trends
conn.request("GET", "/price?symbol=AAPL&format=json", headers=headers)
res = conn.getresponse()
data = res.read()
data = json.loads(data)

KeyValues['AAPL'] = data['price']
print(KeyValues)
money_object = json.dumps(KeyValues)
with open("./StockTrack/values.json", "w") as outfile:
    outfile.write(money_object)

