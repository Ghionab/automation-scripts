import requests

url="https://finance.yahoo.com/quote/MSFT/history/"
params = {
    "period1": 1734800036,  # Start timestamp
    "period2": 1735231689,  # End timestamp
    "interval": "1d",       # Daily data
    "events": "history",
    "includeAdjustedClose": "true"
}

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
  }

response= requests.get(url, headers=headers)

with open("yahoo.csv","wb") as file:
    file.write(response.content)
print("200")
