from fastapi import FastAPI
import mongo_client
import Constants
import EventCompleteInfo

app = FastAPI()


@app.get("/events/{event_id}")
def get_event_info(event_id):
    events_list = mongo_client.get_past_event_info(Constants.events_db[event_id], Constants.events_link[event_id])
    ans = []
    for item in events_list:
        event = EventCompleteInfo.EventCompleteInfo(item["event_title"], item["event_date"], item["pdf_title"],
                                                    item["pdf_link"])
        ans.append(event)
    return ans


