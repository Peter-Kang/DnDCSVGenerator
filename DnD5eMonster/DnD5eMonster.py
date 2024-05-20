import json
import requests

def GetJson():
    #it has to be sequential, the json has the address of the next page if one exists
    results = []
    url:str = f"https://api.open5e.com/monsters/?format=json&ordering=challenge_rating"
    hasNext:bool = True
    while hasNext:
        try:
            rep = requests.get(url)
            if(rep.status_code == 200):
                payload = rep.json()
                #next URL  
                if payload['next'] != None:
                    #get the next url
                    url = payload['next']
                else: 
                    hasNext = False
            for monster in payload['results']:
                results.append(monster)
        except requests.exceptions.RequestException as e:
            print(f"Error getting mosnter info {e.strerror}")
    return results

def WriteJson(results:json):
    for monster in results:
        pass
    pass

def main():
    results = GetJson()
    WriteJson(results)

main()