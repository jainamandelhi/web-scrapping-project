import requests
from bs4 import BeautifulSoup as bs

import EventCompleteInfo
import PDFInfo


def find_events_link(past_events):
    events_link = []
    for p in past_events:
        events_link.append(p.find("a")["href"])
    return events_link


def find_past_events_info(events_link):
    past_events_info = []  # title, date, [{"pdfTitle": "pdfLink"}]

    for link in events_link:
        address = requests.get(link)
        soup_address = bs(address.content)
        title = soup_address.find("div", attrs={"class": "wd_title wd_event_title detail_header"}).get_text()
        date = soup_address.find("div", attrs={"class": "item_date wd_event_sidebar_item wd_event_date"}).get_text()
        pdf_info_list = []
        pdfs = soup_address.select("div.wd_event_info a")
        for pdf in pdfs:
            pdf_title = pdf.get_text()
            href = pdf["href"]
            pdf_info = PDFInfo.PDFInfo(pdf_title, href)
            pdfList = {pdf_info.title: pdf_info.link}
            pdf_info_list.append(pdfList)
        past_event_info = EventCompleteInfo.EventCompleteInfo(title, date, pdf_info_list)
        past_events_info.append(past_event_info.__dict__)
    return past_events_info


def scrap(href):
    r = requests.get(href)
    soup = bs(r.content)
    pastEvents = soup.select("div.wd_event")
    eventsLink = find_events_link(pastEvents)
    return find_past_events_info(eventsLink)
