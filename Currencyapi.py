from flask import Flask,jsonify
from bs4 import BeautifulSoup
import requests

def get_c(inp, outp):
    url = f"https://www.x-rates.com/calculator/?from={inp}&to={outp}&amount=1"
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
def main(inp,outp):
    rate=get_c(inp, outp)
    rate_dictionary={"input": inp, "output": outp, "rate":rate }
    return jsonify(rate_dictionary)

app.run(host="0.0.0.0")