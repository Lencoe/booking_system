import getpass
import os 
import registry
import sys
import retrieve_calendar_data
import create_slot
import create_booking
import booking_cancellation
import typer



app = typer.Typer()


@app.command()
def register():
    file = os.path.exists("regist.txt")
    if not file:
        user, email = registry.register()
        reg = open("regist.txt", "w+")
        reg.write(user+"\n"+email)
        reg.close()
    if file:
        print('You are already registered.')
        return file
    
    
@app.command()    
def login():
    if not os.path.exists("regist.txt"):
        
        print("you are not registered.\nPlease use \'python3 main.py register\' to register.")
        
        return 
    
    login_file = os.path.exists("login_token.txt")
    
    if not login_file:
        
        file = open("regist.txt", "r")
        
        detail_list = file.readlines()
        
        counter = 4
        
        while counter > 0:
            
            user_email = input("Enter Your Email Address: ")
            
            user_password = getpass.getpass("Enter Password: ")
            
            if user_email+"\n" not in detail_list or user_password not in detail_list:
                print("Invalid user details!!!")
                counter -= 1
                continue
                
            else:
                print("Login successful!\nUse \'python3 main.py help\' to display all available commands.")
                
                token = open("login_token.txt", "w+")
                token.write(user_email+"\n"+user_password)
                token.close()
                return True
            
        print("Please Try again Later!!!")
    else:
        print("You are already logged in")
        

@app.command()
def view_calendar():
    if os.path.exists("login_token.txt"):
        retrieve_calendar_data.main()
    else:
        print('Login required.\nUse \'python3 main.py login\' to login.')    
            

@app.command()
def make_booking(role: str):
    print(sys.argv)
    if os.path.exists("login_token.txt"):
        role = role.lower()
        if role == "volunteer" :
            retrieve_calendar_data.main()
            create_slot.booking()        
        elif role == "student" :
            retrieve_calendar_data.main()
            create_booking.booking()
        else:
            print('invalid!')
    else:
        print('Login required.\nUse \'python3 main.py login\' to login.')        
                      

@app.command()
def cancel_booking(role: str):
    with open("regist.txt", "r") as file:
        list_of_lines = file.readlines()
    user_email = list_of_lines[0].replace("\n", "")
    
    if os.path.exists("login_token.txt"):
        role = role.lower()
        if role == "volunteer" :
            retrieve_calendar_data.main()
            booking_cancellation.cancel_slot(user_email)
        elif role == "student" :
            retrieve_calendar_data.main()
            booking_cancellation.cancel_booking(user_email)
         
         
@app.command()
def help():
    help_commands = """'python3 main.py view-calendar\'                          - displays available booking dates',
'python3 main.py make-booking (\'volunteer\'\\\'student\')\'   - allows bookings to be made',
'python3 main.py reschedule-booking'                     - allows bookings to be updated', 
'python3 main.py cancel-booking'                         - allows bookings to be cancelled',
'python3 main.py help'                                  - displays all available commands',
'python3 main.py sign-out'                               - signs user out of the system"""                      
    print(help_commands)
    return help_commands    
    


@app.command()
def sign_out():
    
    if os.path.exists("login_token.txt"): 
        print("Successfully logged out.")
        os.remove("login_token.txt") 
    else:
        print("You have already successfully logged out.")
      
    
if __name__ == "__main__":
    app()    