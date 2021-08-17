from pymongo import MongoClient
from Service import document_scrap as ds

client = MongoClient()

db = client.scrapping

# db.pastEventsCollection.drop()
#print(db.pastEventsCollection.count())


def scrap_past_events(event_id, event_link):
    pastEventsCollection = db.pastEventsCollection
    events = ds.scrap(event_id, event_link)

    for event in events:
        if not pastEventsCollection.find({"pdf_link": event["pdf_link"]}).count() > 0:
            pastEventsCollection.insert_one(event)


def get_past_event_info():
    list_ans = []
    for doc in db.pastEventsCollection.find():
        list_ans.append(doc)
    return list_ans

