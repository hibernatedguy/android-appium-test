import unittest

from desired_capabilities import check_device_availability
from lesson import LessonTestCase
from profiles import AppStartupChecks


###########################
# Actual Code Starts Here
###########################
class MainTestRunner(AppStartupChecks, LessonTestCase):
    ''' English Duniya App Testing
    '''
    pass


if __name__ == '__main__':
    check_device_availability()
    suite = unittest.TestLoader().loadTestsFromTestCase(MainTestRunner)
    unittest.TextTestRunner(verbosity=2).run(suite)
