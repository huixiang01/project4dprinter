def test(request):
    
    request_json = request.get_json(silent=True)
    print('hi this is jaryl')
    print(request_json)
    teleuser = request_json['originalDetectIntentRequest']['payload']['data']['from']['first_name']
    teleid = request_json['originalDetectIntentRequest']['payload']['data']['from']['id']
    creds = None

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
    
    tz = pytz.timezone('Asia/Singapore')
    s_time = request_json["queryResult"]["outputContexts"][0]["parameters"]["start.original"]
    e_time = request_json["queryResult"]["outputContexts"][0]["parameters"]["enddate-time.original"]

    the_datetime = tz.localize(datetime.datetime(int(s_time[6:10]), int(s_time[3:5]), int(s_time[:2]), int(s_time[11:13]), int(s_time[13:15])))
    the_datetime2 = tz.localize(datetime.datetime(int(e_time[6:10]), int(e_time[3:5]), int(e_time[:2]), int(e_time[11:13]), int(e_time[13:15])))
    body = {
        "timeMin": the_datetime.isoformat(),
        "timeMax": the_datetime2.isoformat(),
        "timeZone": 'Asia/Singapore',
        "items": [{"id": 'jaryllim@sutd.edu.sg'}]
    }
    eventsResult = service.freebusy().query(body=body).execute()
    cal_dict = eventsResult[u'calendars']

    for cal_name in cal_dict:
        print(cal_name, cal_dict[cal_name]