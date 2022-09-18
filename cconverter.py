# write your code here!

import requests
import json

inputcurr = str.lower(input())

rates = requests.get("https://floatrates.com/daily/" + inputcurr + ".json")
# print(r.text)
parsedrates = json.loads(rates.text)

ratescache = {}

if inputcurr.lower() != "usd":
    usdrecord = parsedrates["usd"]
    usdrate = usdrecord["rate"]
    ratescache["usd"] = usdrate
if inputcurr.lower() != "eur":
    eurrecord = parsedrates["eur"]
    eurrate = eurrecord["rate"]
    ratescache["eur"] = eurrate

# BEGINNING OF LOOP

while True:
    outputcurr = str.lower(input())
    if outputcurr == '':
        break
    
    inputcoins = float(input())
    print("Checking the cache...")
    if outputcurr in ratescache:
        print("Oh! It is in the cache!")
    else:
        print("Sorry, but it is not in the cache!")
        r = requests.get("https://floatrates.com/daily/" + inputcurr + ".json")
        parsedr = json.loads(r.text)
        outputrecord = parsedr[outputcurr]
        newrate = outputrecord["rate"]
        ratescache[outputcurr] = newrate
    
    moneyreceived = round(inputcoins * ratescache[outputcurr], 2)
    print(f"You received {moneyreceived} {outputcurr.upper()}.")

# END OF LOOP

