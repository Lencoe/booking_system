from pprint import pprint
from Google import convert_to_RFC_datetime
import retrieve_calendar_data  as data


"""
The pprint module in Python is a utility module that you can use to print data
structures in a readable, pretty way. It's a part of the standard library that's especially 
useful for debugging code dealing with API requests, large JSON files, and data in general.
"""

def cancel_slot(user_email) :

    calendarId='c_63a388aa328d889170e8d16e600442eb6a8e86a12b75a12b15f7a30c02785eff@group.calendar.google.com'
   

    """
    Create an event
    """

    file = open("regist.txt", "r")
    file_lines = file.readlines()
    file.close()

    email = file_lines[0]
    email = email.replace("\n", "")
    service = data.authenticate()


    date = input("Enter Date(Format: yyyy-mm-dd): ")
    time = input("Enter Time(Format: hh:mm): ")
    
    event_id = None
    
    events, calendar_events = data.get_volunteer_events()


    for event in calendar_events:
        
        event_datetime = event["start"]["dateTime"].split("T")
        event_date = event_datetime[0]
        event_time = event_datetime[1][:5]
        

                
        if date == event_date and time == event_time:
            
            if user_email != event["creator"]["email"]:
                
                print("You cannot cancel someone else's booking")
                return
            
            if len(event["attendees"]) > 1:
                
                print("You cannot cancel a booked slot")
            else:
                event_id = event["id"]
                
        
            
            
    if event_id:
            


        service.events().delete(calendarId=calendarId, eventId=event_id).execute()

   

def cancel_booking(user_email):
    
    calendarId='c_63a388aa328d889170e8d16e600442eb6a8e86a12b75a12b15f7a30c02785eff@group.calendar.google.com'



    file = open("regist.txt", "r")
    file_lines = file.readlines()
    file.close()

    email = file_lines[0]
    email = email.replace("\n", "")
    service = data.authenticate()

    

    date = input("Enter Date(Format: yyyy-mm-dd): ")
    time = input("Enter Time(Format: hh:mm): ")
    
    event_id = None
    
    events, calendar_events = data.get_volunteer_events()


    for event in calendar_events:
        
        event_datetime = event["start"]["dateTime"].split("T")
        event_date = event_datetime[0]
        event_time = event_datetime[1][:5]
        
    
                
        if date == event_date and time == event_time:
            
            if user_email != event["attendees"][1]["email"]:
                
                print("You cannot cancel someone else's booking")
                return
            
            if len(event["attendees"]) < 2:
                
                print("There is no booking")
                
            if len(event["attendees"]) > 1:
                
                event_id = event["id"]
                
        
            
            
    if event_id:

        calendarId='c_63a388aa328d889170e8d16e600442eb6a8e86a12b75a12b15f7a30c02785eff@group.calendar.google.com'
            

        event = service.events().get(calendarId=calendarId, eventId=event_id).execute()

  
        attendee_2 = event["attendees"][1]
        event["attendees"].remove(attendee_2)
        

        service.events().update(calendarId=calendarId, eventId=event_id, body=event).execute()


def main():
    
    pass