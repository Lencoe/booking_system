from pprint import pprint
from Google import convert_to_RFC_datetime
import retrieve_calendar_data  as data


"""
The pprint module in Python is a utility module that you can use to print data
structures in a readable, pretty way. It's a part of the standard library that's especially 
useful for debugging code dealing with API requests, large JSON files, and data in general.
"""

def booking() :

    calendarId='c_63a388aa328d889170e8d16e600442eb6a8e86a12b75a12b15f7a30c02785eff@group.calendar.google.com'
    # service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    """
    Create an event
    """

    file = open("regist.txt", "r")
    file_lines = file.readlines()
    file.close()

    email = file_lines[0]
    email = email.replace("\n", "")
    service = data.authenticate()
    # events = data.get_events(7)
    # colors = service.colors().get().execute()
    # pprint(colors)
    

    date = input("Enter Date(Format: yyyy-mm-dd): ")
    time = input("Enter Time(Format: hh:mm): ")
    
    events, calendar_events = data.get_volunteer_events()

    if len(events[1]) > 1:
        
        for event in events[1:]:
            
            if len(event) > 1:
                event = event[1].split("T")
                evnt_date = event[0]
                evnt_time = event[1][:5]
                
                if date == evnt_date and time == evnt_time:
                    print("time slot is booked")
                    return
                
    

        # event_data = calendar_events[i]
        # event = events[i][1].split("T")
        
        # evnt_date = event[0]
        # evnt_time = event[1][:5]
        
        # event_id = event_data["id"]
        
        # print(evnt_date,evnt_time)
        
        # if date == evnt_date and time == evnt_time:
        #     # print("IcalendarId am ")
        #     contin = True

    date = date.split("-")
    time = time.split(":")

    date = [int(x) for x in date]
    time = [int(x) for x in time]
    
    year = date[0]
    month = date[1]
    day = date[2]
    
    end_hour,start_hour = time[0],time[0]
    end_minutes,start_minutes = time[1],time[1]
    
    end_minutes = start_minutes+30
    
    if end_minutes == 60 :
        end_hour = start_hour+1
        end_minutes = 0

    hour_adjustment = -2
    event_request_body = {
                        'start': {'dateTime': convert_to_RFC_datetime(year,   month, day, start_hour + hour_adjustment, start_minutes),

                                'timeZone': 'Africa/Johannesburg'
                                },
                        'end':   {'dateTime': convert_to_RFC_datetime(year,   month, day, end_hour + hour_adjustment, end_minutes),
                                'timeZone': 'Africa/Johannesburg'
                                },
                        'summary': 'Book appointment',
                        'description': 'Booking appointment with volunteer.',
                        'colorId': 5,
                        'status': 'confirmed',
                        'visibility': 'public',
                        'location': 'South Africa, Johannesburg',
                        "organizer": {
                         
                            "email": email,
                            "displayName": email.split("@")[0],
                       
                        },
                         'attendees' : [{   "email": email,
                            "displayName": email.split("@")[0],
                       }]
                        }                          
    response = service.events().insert(
        calendarId='c_63a388aa328d889170e8d16e600442eb6a8e86a12b75a12b15f7a30c02785eff@group.calendar.google.com',
        
        body = event_request_body).execute()

    # pprint(response)
    print("A slot successfully created")


