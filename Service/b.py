import requests
from bs4 import BeautifulSoup as bs
from time import sleep
import json

headers = {"cookie":"ASP.NET_SessionId=54fdvkoft30df3b4v1ego1eq; _ga=GA1.2.187890047.1629194699; _gid=GA1.2.1071652028.1629365143; AWSALB=nYuj3j/TH85GACNKznQvFiSvE/t0lcIUG2BOmMLFVhCcUWndQn3G2MB31kWcd2UxReaQRUzsycMCkLSSMshGN3Uh7li2AZTuYzAYLHKWYJBMzUzrd1E5gL4Ymwbu; AWSALBCORS=nYuj3j/TH85GACNKznQvFiSvE/t0lcIUG2BOmMLFVhCcUWndQn3G2MB31kWcd2UxReaQRUzsycMCkLSSMshGN3Uh7li2AZTuYzAYLHKWYJBMzUzrd1E5gL4Ymwbu; _gat=1; _gat_INVDSitecore=1",
           "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
           }
address = requests.get("https://ir.homedepot.com/events-and-presentations",headers=headers)
data = bs(address.content)
print(data.prettify())
"""soup_address = bs(address.text, "html.parser")
print(soup_address.prettify())
blocks = soup_address.select("p")
s = ""
for block in blocks:
  s = s + block.get_text()
json_object = json.loads(s)
print(json_object)
"""