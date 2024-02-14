from Google import convert_to_RFC_datetime
import retrieve_calendar_data  as data
import registry


def booking() :
    
    events, calendar_events = data.get_volunteer_events()
    
    events = [event for event in events[1:] if len(event) > 1 ]

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
    contin = False
    
    for i in range(len(events)):
        event_data = calendar_events[i]
        event = events[i][1].split("T")
        
        evnt_date = event[0]
        evnt_time = event[1][:5]
        
        
        if date == evnt_date and time == evnt_time:
            contin = True
            event_id = event_data["id"]
        
            
            if len(event_data["attendees"]) == 2:
                
                print("Cannot make double booking")
                
                return
            
    if not contin:
        
        print("Invalid slot")       
        


   
    email = registry.get_email()
    if contin:
        event = service.events().get(calendarId=calendarId, eventId=event_id).execute()

        event['attendees'].append({
            'email' :email,
            'status' : "confirmed"
        })

        update = service.events().update(calendarId=calendarId, eventId=event_id, body=event).execute()

        # print(update)
        print("A booking succefully booked")



