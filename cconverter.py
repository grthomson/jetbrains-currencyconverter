import requests
import json

#inputcurr is what we're selling

inputcurr = str.lower(input())

#fetch json record for inputcurr

rates = requests.get("https://floatrates.com/daily/" + inputcurr + ".json")

#parse to .text

parsedrates = json.loads(rates.text)

#initialise empty cache

ratescache = {}

# if inputcurr is not usd or eur, add inputcurr/usd and inputcurr/eur rates to cache

if inputcurr.lower() != "usd":
    usdrecord = parsedrates["usd"]
    usdrate = usdrecord["rate"]
    ratescache["usd"] = usdrate
if inputcurr.lower() != "eur":
    eurrecord = parsedrates["eur"]
    eurrate = eurrecord["rate"]
    ratescache["eur"] = eurrate

while True:
    outputcurr = str.lower(input())  #outputcurr is what we're buying
    if outputcurr == '':             #break and exit on a blank outputcurr
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
    #if outputcurr not a key in cache, fetch and parse rate from json and store as new key:value pair
    moneyreceived = round(inputcoins * ratescache[outputcurr], 2)
    print(f"You received {moneyreceived} {outputcurr.upper()}.")


