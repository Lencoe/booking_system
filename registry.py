import retrieve_calendar_data  as data
import getpass


def get_email():
    
    service = data.authenticate()
  
    
    calendars = []
    page_token = None
    while True:
        calendar_list = service.calendarList().list(pageToken=page_token).execute()
        for calendar_list_entry in calendar_list['items']:
            # print(calendar_list_entry['summary'])
            calendars.append(calendar_list_entry['summary'])
        page_token = calendar_list.get('nextPageToken')
        if not page_token:
            break
        
    # user_email = "thlenco@student.wethinkcode.co.za"
    user_email = None
    
    for calendar in calendars:
        
        if calendar[-26:] == "@student.wethinkcode.co.za":
            
            user_email = calendar
            
    return user_email

def register():
    
    user_email = get_email()
     
    user = None      
            
    if user_email:
        
        user = input("Enter Email: ")
        while True:
            
            if user != user_email:
                
                user = input("Enter correct email: ")
                
            else:
                
                break
            
        if user:
            
            password = getpass.getpass("Create New Password: ")
            
            confirm = getpass.getpass("Confirm Password: ")
            
            
            while True:
                
                if password == confirm:
                    print("successfuly registered.\nUse \'python3 main.py login\' to login.")
                    break
                else:
                    
                    confirm = getpass.getpass("Please enter matching password: ")
            
            
            
        return user, confirm
            
                
    else:
        
        print("Please login using your Student email.")
        
        return 
    
    
