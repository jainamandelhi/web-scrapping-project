import requests
import json
from bs4 import BeautifulSoup as bs

r = requests.get("https://investor.weyerhaeuser.com/events-and-presentations")
soup = bs(r.content)

pastEvents = soup.select("div.wd_event")

eventsLink = []
for p in pastEvents:
    eventsLink.append(p.find("a")["href"])

pastEventsInfo = []  # title, date, [{"pdfTitle": "pdfLink"}]


class PastEventInfo:
    def __init__(self, title, date, pdfInfo):
        self.title = title
        self.date = date
        self.pdfInfo = pdfInfo


class PdfInfo:
    def __init__(self, title, href):
        self.title = title
        self.href = href


for link in eventsLink:
    address = requests.get(link)
    soupAddress = bs(address.content)
    title = soupAddress.find("div", attrs={"class": "wd_title wd_event_title detail_header"}).get_text()
    date = soupAddress.find("div", attrs={"class": "item_date wd_event_sidebar_item wd_event_date"}).get_text()
    pdfInfoList = []
    pdfs = soupAddress.select("div.wd_event_info a")
    for pdf in pdfs:
        pdfTitle = pdf.get_text()
        href = pdf["href"]
        pdfList = {pdfTitle: href}
        pdfInfoList.append(pdfList)
    pastEventInfo = {"title": title, "date": date, "links": pdfInfoList}
    pastEventsInfo.append(pastEventInfo)

#print(pastEventsInfo)

import pymongo
from pymongo import MongoClient
client = MongoClient()
print(client)

db = client.scrapping

pastEventsCollection = db.pastEventsCollection
print(pastEventsCollection)
result = pastEventsCollection.insert_many(pastEventsInfo)

import pprint

listAns = []
for doc in pastEventsCollection.find():
    listAns.append(doc)

print(listAns)

