import unittest
from appium import webdriver
from time import sleep
import logging
from desired_capabilities import (get_desired_capabilities, SLEEP_SHORT,
                                  SLEEP_LONG, SLEEP_QUICK, check_device_availability,
                                  random_numbers)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from random import randint

from lesson import LessonTestCase
###########################
# Actual Code Starts Here
###########################
class EnglishDuniyaUnitTest):
    ''' English Duniya App Testing
    '''
    def setUp(self):
            desired_caps = get_desired_capabilities('269.apk')

        # web driver remote access
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        
        # self.driver.switch_to.context(self.driver.contexts[-1])
        self.profile_score=0

    def closeApp(self):
        self.driver.quit()

    def resetApp(self):
        self.driver.resetApp()

    def goBack(self):
        self.driver.back()


if __name__ == '__main__':
    check_device_availability()
    suite=unittest.TestLoader().loadTestsFromTestCase(EnglishDuniyaUnitTest)
    unittest.TextTestRunner(verbosity = 2).run(suite)
