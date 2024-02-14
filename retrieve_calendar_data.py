from __future__ import print_function
from pprint import pprint
import csv

"""

__future__ module is a built-in module in Python that is used to inherit new features,
that will be available in the new Python versions.
This module includes all the latest functions which were not present in the
previous version in Python.
"""

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from tabulate import tabulate



"""
Scopes express the permissions you request users to authorize for your app and allow
your project to access specific types of private user data from their Google Account
"""
SCOPES = 'https://www.googleapis.com/auth/calendar', 'https://www.googleapis.com/auth/calendar.events'


def authenticate():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
 
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    service = build('calendar', 'v3', credentials=creds)
    return service


def get_volunteer_events():
    """Retrieves volunteer calendar data"""
    
    calendar_events = []
    
    try:    
        service = authenticate()
        time_now = datetime.datetime.utcnow()
        now = datetime.datetime.utcnow().isoformat() + 'Z'  
        number_of_events = datetime.timedelta(days = 7)
        
        n =  (time_now + number_of_events).isoformat() + 'Z'
       
        events_result = service.events().list(calendarId = 'c_63a388aa328d889170e8d16e600442eb6a8e86a12b75a12b15f7a30c02785eff@group.calendar.google.com',
                        timeMin=now, timeMax= n, singleEvents = True, orderBy = 'startTime').execute()
        events = events_result.get('items', [])
        
        my_events = [[count +1] for count in range(len(events))]
    
     
        count = 0
       
        for event in events:
         
           
            calendar_events.append(event)
            title = event["summary"]
            start = event['start'].get('dateTime', event['start'].get('date'))
            name = (event["creator"].get("email"))
            my_events[count].append(start)
            my_events[count].append(title)
            my_events[count].append(name)
            
            
            if len(event.get("attendees"))< 2:
                
                my_events[count].append("Available")
            else:
                my_events[count].append("Booked")
            count +=1
       
        
        titles = ["Slot Number", "dateTime", "Title", "Volunteer Name", "Status"]
        my_events.insert(0, titles)    
        
        return my_events, calendar_events
 
    except HttpError as error:
        print('An error occurred: %s' % error)


def get_student_events():
    """Retrieves student calendar data"""

    try:    
        service = authenticate()
        time_now = datetime.datetime.utcnow()
        now = datetime.datetime.utcnow().isoformat() + 'Z'  
        number_of_events = datetime.timedelta(days = 7)
        
        n =  (time_now + number_of_events).isoformat() + 'Z'
        
        events_result = service.events().list(calendarId = 'c_63a388aa328d889170e8d16e600442eb6a8e86a12b75a12b15f7a30c02785eff@group.calendar.google.com',
                        timeMin=now, timeMax= n, singleEvents = True, orderBy = 'startTime').execute()
        events = events_result.get('items', [])
        
        

        if not events:
            print('No upcoming events found.')
            return

        
        my_events = [[count +1] for count in range(len(events))]
        
        count = 0
        for event in events:
            title = event["summary"]
            start = event['start'].get('dateTime', event['start'].get('date'))
            name = (event["creator"].get("email"))
            my_events[count].append(start)
            my_events[count].append(title)
            my_events[count].append(name)
            
            
            if len(event.get("attendees"))< 2:
                
                my_events[count].append("Available")
            else:
                my_events[count].append("Booked")
            count +=1
       
        
        titles = ["Slot Number", "dateTime", "Title", "Volunteer Name", "Status"]
        my_events.insert(0, titles)
        
        return my_events
 
    except HttpError as error:
        print('An error occurred: %s' % error)


def  get_current_date():
    """ 
    This function returns today's date
    """
    today = datetime.date.today() 
    print("Today's date is: ", today)
 


def create_table(data):
    """Tabulates the events"""

    get_current_date()
    print(tabulate(data, headers = 'firstrow', tablefmt = 'grid'))
    
    with open('test.txt', 'w') as outputfile:
         outputfile.write(tabulate(data, headers = 'firstrow', tablefmt = 'grid'))



def main():
    """main function"""
    volunteer_data, calendar_events = get_volunteer_events()
    student_data = get_student_events()
    create_table(volunteer_data)
    print()
