import requests
from bs4 import BeautifulSoup as bs
import json
from Constant import constants
from Models import PDFInfo


def find_events_link(past_events):
    events_link = []
    for p in past_events:
        events_link.append(p.find("a")["href"])
    return events_link


def find_pdf_info(pdfs, title, date, past_events_info):
    for pdf in pdfs:
        pdf_title = pdf.get_text()
        href = pdf["href"]
        pdf_info = PDFInfo.PDFInfo(title, date, pdf_title, href)
        past_events_info.append(pdf_info.__dict__)
    return past_events_info


def find_past_events_info(events_link):
    past_events_info = []  # title, date, [{"pdfTitle": "pdfLink"}]

    for link in events_link:
        address = requests.get(link)
        soup_address = bs(address.content)
        title = soup_address.find("div", attrs={"class": "wd_title wd_event_title detail_header"}).get_text()
        date = soup_address.find("div", attrs={"class": "item_date wd_event_sidebar_item wd_event_date"}).get_text()
        pdfs = soup_address.select("div.wd_event_info a")
        pdf_info_list = find_pdf_info(pdfs, title, date, past_events_info)
        # past_event_info = EventCompleteInfo.EventCompleteInfo(title, date, pdf_info_list)
        # past_events_info.append(pdf_info_list)
    return past_events_info


def find_past_events_info_for_fb(json_object):
    past_events_info = []

    for event in json_object["GetEventListResult"]:
        attachments = event["Attachments"]
        for attachment in attachments:
            pdf_info = PDFInfo.PDFInfo(event["Title"], event["EndDate"], attachment["Title"], attachment["Url"])
            past_events_info.append(pdf_info.__dict__)
    return past_events_info


def find_past_events_info_for_informa(json_object):
    past_events_info = []

    for event in json_object["files"]:
        pdf_info = PDFInfo.PDFInfo(event["category"], event["updated_at"], event["title"], event["url"])
        past_events_info.append(pdf_info.__dict__)
    return past_events_info


def scrap(event_id, href):
    if event_id == "id1":
        return scrap_for_weyerhaeuser(href)
    elif event_id == "id2":
        return scrap_for_fb(href)
    elif event_id == "id3":
        event_data = []
        for link in constants.events_informa:
            event_info = scrap_for_informa(link)
            for event in event_info:
                event_data.append(event)
        return event_data


def scrap_for_weyerhaeuser(href):
    r = requests.get(href)
    soup = bs(r.content)
    pastEvents = soup.select("div.wd_event")
    eventsLink = find_events_link(pastEvents)
    return find_past_events_info(eventsLink)


def scrap_for_fb(href):
    address = requests.get(href)
    return find_past_events_info_for_fb(address.json())


def scrap_for_informa(href):
    address = requests.get(href)
    s = address.text
    my_prefix = "jQuery1830500746899123085_1629202578914("
    s = s[len(my_prefix):]
    s = s[:-1]
    s = json.loads(s)
    return find_past_events_info_for_informa(s)
