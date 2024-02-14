import unittest
import sys
from io import StringIO
import main

class Test_booking_system(unittest.TestCase):
        
    def test_main(self):
        sys.stdout = StringIO()
        commands = main.help()
        self.assertEqual(commands , ['\'python3 main.py view-calendar\'                          - displays available booking dates' ,
                     '\'python3 main.py make-booking (\'volunteer\'\\\'student\')\'   - allows bookings to be made' ,
                     '\'python3 main.py reschedule-booking\'                     - allows bookings to be updated' , 
                     '\'python3 main.py cancel-booking\'                         - allows bookings to be cancelled',
                     '\'python3 main.py help\'                                   - displays all available commands'])
        
        
            
            
if __name__ == '__main__':     
    unittest.main()               