from flask import Flask,jsonify
from bs4 import BeautifulSoup
import requests

def get_c(input, output):
    url = f"https://www.x-rates.com/calculator/?from={input}&to={output}&amount=1"
    content=requests.get(url).text
    soup=BeautifulSoup(content, 'html.parser')
    currency=soup.find("span", class_="ccOutputRslt" ).get_text()
    #print(currency)
    return currency

app=Flask(__name__)
  
@app.route("/")
def home():
    return "<h1>Currenct Rate</h1>"

@app.route(f"/api/<inp>-<outp>")
def main(input,output):
    rate=get_c(input, output)
    rate_dictionary={"input": input, "output": output, "rate":rate }
    return jsonify(rate_dictionary)

app.run(host="0.0.0.0")
