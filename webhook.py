import pandas as pd
import csv

def subscribeAdd(URL: str, Type: bool) -> bool:
    try:
        f = open("Data/test.csv", "a", encoding="utf-8", newline='')
        d = csv.writer(f)
        d.writerow([URL,Type])

        return True
    
    except Exception as errorMessage:
        print(errorMessage)
        return False
    
def subscribeInfo() -> dict:
    return pd.read_csv("Data/test.csv").to_dict()



import requests

class Push:
    def __init__(self, URL: str) -> None:
        self.URL = URL

    def JSON() -> bool:
        headers = {
            'accept': 'application/json',
        }

        response = requests.post(self.URL, headers=headers)
        pass

    def FormURL() -> bool:
        response = requests.post(self.URL, headers=headers)
        pass

