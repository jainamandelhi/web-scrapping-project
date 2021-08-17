import requests
from bs4 import BeautifulSoup as bs
from time import sleep
import json


address = requests.get("https://investor.fb.com/feed/Event.svc/GetEventList?apiKey=F37D4FC40D0E4774887D6827E95013D5&eventSelection=0&eventDateFilter=0&includeFinancialReports=true&includePresentations=true&includePressReleases=true&sortOperator=1&pageSize=-1&tagList=&includeTags=true&year=-1&excludeSelection=0")
data = address.json()
print(data)
"""soup_address = bs(address.text, "html.parser")
print(soup_address.prettify())
blocks = soup_address.select("p")
s = ""
for block in blocks:
  s = s + block.get_text()
json_object = json.loads(s)
print(json_object)
"""