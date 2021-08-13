from pymongo import MongoClient
import document_scrap as ds
client = MongoClient()

db = client.scrapping


pastEventsCollection = db.pastEventsCollection
result = pastEventsCollection.insert_many(ds.scrap("https://investor.weyerhaeuser.com/events-and-presentations"))

list_ans = []
for doc in pastEventsCollection.find():
    list_ans.append(doc)

print(list_ans)
