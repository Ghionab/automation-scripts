import requests
import json

url="https://languagetool.org/http-api/check"
data={
    "text": "tis is not right mon",
    "language":"auto"
}
response=requests.post(url,data=data)
result=json.loads(response.text)
print(result)