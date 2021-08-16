from pymongo import MongoClient
from Service import document_scrap as ds

client = MongoClient()

db = client.scrapping

# pastEventsCollection = db.pastEventsCollection

# print(pastEventsCollection in db.list_collection_names())

"""if "scrapping" in client.list_database_names():
    print("You successfully created test database.")
else:
    print("test database was not created.")
"""
#db.pastEventsCollection.drop()


def get_past_event_info(event_collection, event_link):
    list_ans = []
    if event_collection not in db.list_collection_names():
        event_collection_db = db[event_collection]
        event_collection_db.insert_many(ds.scrap(event_link))
    for doc in db[event_collection].find():
        list_ans.append(doc)
    return list_ans


#ans = get_past_event_info("pastEventsCollection", "https://investor.weyerhaeuser.com/events-and-presentations")
