from bs4 import BeautifulSoup
import requests

def get_c(inp, outp):
    url = f"https://www.x-rates.com/calculator/?from={inp}&to={outp}&amount=1"
    content=requests.get(url).text
    soup=BeautifulSoup(content, 'html.parser')
    currency=soup.find("span", class_="ccOutputRslt" ).get_text()
    print(currency)
    
get_c('EUR', 'INR')