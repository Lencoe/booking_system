import unittest
from io import StringIO
import sys
from unittest.mock import patch
import main


class MyTestCase(unittest.TestCase):
    def test_help_function(self):
        output = main.help()
        

        self.assertEqual("""'python3 main.py view-calendar\'                          - displays available booking dates',
'python3 main.py make-booking (\'volunteer\'\\\'student\')\'   - allows bookings to be made',
'python3 main.py reschedule-booking'                     - allows bookings to be updated', 
'python3 main.py cancel-booking'                         - allows bookings to be cancelled',
'python3 main.py help'                                  - displays all available commands',
'python3 main.py sign-out'                               - signs user out of the system""", output)

   

if __name__ == '__main__':
    unittest.main()
