from fastapi import FastAPI
from Mongo import mongo_client
from Constant import constants
from Models import EventCompleteInfo

app = FastAPI()


@app.get("/events")
def get_event_info():
    events_list = mongo_client.get_past_event_info()
    ans = []
    for item in events_list:
        event = EventCompleteInfo.EventCompleteInfo(item["event_title"], item["event_date"], item["pdf_title"],
                                                    item["pdf_link"])
        ans.append(event)
    return ans


@app.get("/scrap/{event_id}")
def scrap_event(event_id):
    mongo_client.scrap_past_events(event_id, constants.events_link[event_id])
    return "scrapped successfully. Visit /events to view"

