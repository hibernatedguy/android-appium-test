import unittest
from config import check_device_availability
from lesson import LessonTestCase

###########################
# Actual Code Starts Here
###########################
class MainTestRunner(LessonTestCase):
    ''' English Duniya App Testing
    '''
    pass


if __name__ == '__main__':
    check_device_availability()
    suite=unittest.TestLoader().loadTestsFromTestCase(MainTestRunner)
    unittest.TextTestRunner(verbosity = 2).run(suite)