from __future__ import print_function
import datetime
import pickle
import os
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pytz
import datetime
from flask import escape, Flask, make_response, jsonify, request
from pylogflow import IntentMap
import requests
import json

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])
    service.events().delete(calendarId='primary', eventId='0o62hu9kavqrufb5ebeh3t29sl').execute()

if __name__ == '__main__':
    main()




'''
def test(request):
    result = intentMap.execute_intent(request.json)
    print('hello this is me')
    print(result)  
    return jsonify(result) 

def intentTest(request):
    #print(request)
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    service = build('calendar', 'v3', credentials=creds)
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])
    if not events:
        print('No upcoming events found.')
    testlist = ['Please enter your index here']
    for index, event in enumerate(events):
        start = event['start'].get('dateTime', event['start'].get('date'))
        testlist.append('{} {} {} \n'.format(index, start, event['summary']))
        print(index, start, event['summary'], 'hello i have succeeded')
    return {'fulfillmentText': ' '.join(testlist), 'fulfillmentlist': testlist}

def delete1(request):
    print(request)
    idx = int(request["queryResult"]["queryText"])
    print(idx)
    print('jaryl is a smart person and he knows it too')
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    service = build('calendar', 'v3', credentials=creds)
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])
    if not events:
        print('No upcoming events found.')
    testlist = ['Are you sure you want to delete the following event?']
    for index, event in enumerate(events):
        start = event['start'].get('dateTime', event['start'].get('date'))
        testlist.append('{} {} {} \n'.format(index, start, event['summary']))
    print(testlist)
    return {'fulfillmentText': 'Are you sure you want to delete the following event {}'.format(testlist[idx])}
def delete2(request):
    if request['queryResult']["queryText"] == 'YES':
        #run deletion code 
        #service.events().delete(calendarId='primary', eventId='0o62hu9kavqrufb5ebeh3t29sl').execute()
    else:
        return {'fulfillmentText': 'Your booking has not been removed. Please try again.'}
    return {'fulfillmentText':'Your booking has been removed. Please make another booking if you wish to'}
def schedule1(request):
    return {'fulfillmentText': 'Please input your start date/time according to the format listed: (DD/MM/YY TIME 01/03/2020 1600)'}
def schedule2(request):
    return {'fulfillmentText': 'Please input your end date/time according to the format listed: (DD/MM/YY TIME 01/03/2020 1700)'}
def schedule3(request):
    return {'fulfillmentText': 'Do you confirm your booking from {} to {} ? (YES/NO)'.format(
        request["queryResult"]["outputContexts"][0]["parameters"]["start.original"], 
        request["queryResult"]["outputContexts"][0]["parameters"]["enddate-time.original"]
    )}
def schedule4(request):
    print(request)
    print('hello jaryl')
    
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    service = build('calendar', 'v3', credentials=creds)
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time

    tz = pytz.timezone('Asia/Singapore')
    s_time = request["queryResult"]["outputContexts"][1]['parameters']['start.original']
    e_time = request["queryResult"]["outputContexts"][0]['parameters']['enddate-time.original']
    the_datetime = tz.localize(datetime.datetime(int(s_time[6:10]), int(
        s_time[3:5]), int(s_time[:2]), int(s_time[11:13]), int(s_time[13:15])))
    the_datetime2 = tz.localize(datetime.datetime(int(e_time[6:10]), int(
        e_time[3:5]), int(e_time[:2]), int(e_time[11:13]), int(e_time[13:15])))
    body = {
        "timeMin": the_datetime.isoformat(),
        "timeMax": the_datetime2.isoformat(),
        "timeZone": 'Asia/Singapore',
        "items": [{"id": 'jaryllim@sutd.edu.sg'}]
    }
    eventsResult = service.freebusy().query(body=body).execute()
    cal_dict = eventsResult[u'calendars']
    for cal_name in cal_dict:
        print(cal_name, cal_dict[cal_name])
        if len(cal_dict[cal_name]['busy']) == 0 and 'YES' in request['queryResult']['queryText']:
            print('You can create an event here')
            teleuser, teleid = 0, 1
            start_datetime = tz.localize(datetime.datetime(int(s_time[6:10]), int(
                s_time[3:5]), int(s_time[:2]), int(s_time[11:13]), int(s_time[13:15])))
            stop_datetime = tz.localize(datetime.datetime(int(e_time[6:10]), int(
                e_time[3:5]), int(e_time[:2]), int(e_time[11:13]), int(e_time[13:15])))
    event = {'summary': 'My Printer Booking',
                'description': 'Hi {username} is your telegram ID: {telegramid}'.format(username=teleuser, telegramid=teleid),
                'start': {
                    'dateTime': start_datetime.isoformat(),
                    'timeZone': 'Asia/Singapore',
                },
                'end': {
                    'dateTime': stop_datetime.isoformat(),
                    'timeZone': 'Asia/Singapore',
                }}
    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Event created: %s' % (event.get('htmlLink')))
    return {'fulfillmentText': 'Congratulations, your booking has been made!'}

intentMap = IntentMap()
intentMap.add('Delete Calender Event - Choose List(1)', intentTest)
intentMap.add('Delete Calender Event - Check(2)',delete1)
intentMap.add('Delete Calender Event - Confirmed', delete2)
intentMap.add('Book Slot - Start Time (1)', schedule1)
intentMap.add('Book Slot - End Time (2)', schedule2)
intentMap.add('Book Slot Confirmation (3)',schedule3)
intentMap.add('BookSlot - Confirmed (4)', schedule4)

#teleuser = request_json['originalDetectIntentRequest']['payload']['data']['from']['first_name']
#teleid = request_json['originalDetectIntentRequest']['payload']['data']['from']['id']'''

    