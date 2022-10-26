import http.client
import json
import time

conn = http.client.HTTPSConnection("twelve-data1.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "6a64084255msh51ad42634a01a45p11b294jsnabe18ede9956",
    'X-RapidAPI-Host': "twelve-data1.p.rapidapi.com"
    }

priceDict = {}
#while (True):
conn.request("GET", "/price?symbol=AAPL&format=json", headers=headers)
#time.sleep(10)
res = conn.getresponse()
data = res.read()
data = json.loads(data)
priceDict['AAPL'] = data['price']
print(priceDict)
price_object = json.dumps(priceDict)
with open("./StockTrack/values.json", "w") as outfile:
    outfile.write(price_object)

