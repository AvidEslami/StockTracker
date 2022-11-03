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
previousApple = []
with open("./StockTrack/values.json") as olData:
    oldVals = json.load(olData)
    KeyValues['money'] = int(oldVals["money"])
    previousApple = oldVals["AAPL"]
    AAPLOwned = oldVals["AAPLOwned"]


#get updated values to compare with trends
conn.request("GET", "/price?symbol=AAPL&format=json", headers=headers)
res = conn.getresponse()
data = res.read()
data = json.loads(data)



#push back data, left most (newest) - right most (oldest)
previousApple[0] = previousApple[1]
previousApple[1] = previousApple[2]
previousApple[2] = float(data['price'])

#check if value has decreased relative to past 3 days
AAPLpriceDrop = True
if (previousApple == sorted(previousApple)):
    AAPLpriceDrop = False


#buy a stock if there has been no price drop
if(AAPLpriceDrop == False):
    if (KeyValues['money']>previousApple[0]):
        AAPLOwned += 1
        KeyValues['money'] -= previousApple[2]
else:
    #sell all? might be good in code but terrrrrrible in practice
    KeyValues['money'] += AAPLOwned*(previousApple[2])
    AAPLOwned = 0
    

KeyValues['AAPL'] = previousApple
KeyValues['AAPLOwned'] = AAPLOwned

print(KeyValues)
money_object = json.dumps(KeyValues)
with open("./StockTrack/values.json", "w") as outfile:
    outfile.write(money_object)

