import sys
import pytz
import pprint

from datetime import datetime, timedelta
from oauth2client import client
from googleapiclient import sample_tools


def list_calendars(argv):
    # Authenticate and construct service.
    service, flags = sample_tools.init(
        argv, 'calendar', 'v3', __doc__, __file__,
        scope='https://www.googleapis.com/auth/calendar.readonly')

    try:
        page_token = None
        while True:
            calendar_list = service.calendarList().list(
                pageToken=page_token).execute()
            for calendar_list_entry in calendar_list['items']:
                print(calendar_list_entry['summary'])
            page_token = calendar_list.get('nextPageToken')
            if not page_token:
                break

    except client.AccessTokenRefreshError:
        print('The credentials have been revoked or expired, please re-run'
              'the application to re-authorize.')

def list_actions(argv):
	service, flags = sample_tools.init(argv, 'calendar', 'v3', __doc__, __file__,scope='https://www.googleapis.com/auth/calendar.readonly')
	try:
		calendar = service.calendars().get(calendarId='primary').execute()
		print(calendar)

		cest = pytz.timezone('Europe/Paris')
		now = datetime.now(tz=cest) # timezone?
		timeMin = datetime(year=now.year, month=now.month, day=now.day, tzinfo=cest) + timedelta(days=-30)
		timeMin = timeMin.isoformat()
		timeMax = datetime(year=now.year, month=now.month, day=now.day, tzinfo=cest) + timedelta(days=1)
		timeMax = timeMax.isoformat()

		events = service.events().list(calendarId=calendar["summary"],timeMin=timeMin, timeMax=timeMax).execute()
		return events


	except client.AccessTokenRefreshError:
		print('The credentials have been revoked or expired, please re-run''the application to re-authorize.')
