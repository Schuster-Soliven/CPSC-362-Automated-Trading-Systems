import requests
import json

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed with status {response.status_code}")
        return None

url = "https://query1.finance.yahoo.com/v7/finance/quote?symbols=FNGU,FNGD"
data = fetch_data(url)

if data is not None:
    print(json.dumps(data, indent=4))
else:
    print("Failed to fetch data.")
