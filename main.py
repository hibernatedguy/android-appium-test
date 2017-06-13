import unittest
import os
from appium import webdriver
from time import sleep
import logging
logging.basicConfig(level=logging.INFO)

PATH = os.path.abspath('/Users/Ashish/Documents/workspace/zaya/projects/apks/zaya-mobile-pipeline-combined2.apk')
context_name = "WEBVIEW"
LET_ME_SLEEP_LONG = 20
LET_ME_SLEEP_SHORT = 10
LET_ME_SLEEP_NAP = 5


class EDTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = 'DeadByCode'
        desired_caps['browserName'] = ''
        desired_caps['autoWebview'] = True
        desired_caps['noReset'] = True
        desired_caps['app'] = PATH

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.log = logging.getLogger('appium-ed-logger # ')

    def closeApp(self):
        self.driver.quit()

    def resetApp(self):
        self.driver.resetApp()

    def appInformation(self):
        print (self.driver.contexts[-1])

    @unittest.skip("network-connection")
    def test_000_network_connection(self):
        self.appInformation()   # print app info
        nc = self.driver.network_connection
        self.assertIsInstance(nc, int)

    @unittest.skip("profilepage")
    def test_00_profilepage(self):
        self.appInformation()   # print app info
        self.driver.resetApp()
        sleep(LET_ME_SLEEP_LONG)
        profile_element = self.driver.find_element_by_id("profile-0").click()
        # el = self.driver.find_element_by_id('profile-0')
        self.assertIsNotNone(profile_element)
        sleep(LET_ME_SLEEP_LONG)

    def test_01_after_profile_button_visibility(self):
        self.appInformation()   # print app info
        sleep(LET_ME_SLEEP_SHORT)
        play_button = self.driver.find_element_by_css_selector('.bubbly-btn.play-button')
        self.assertIsNotNone(play_button)
        self.log.info('play_button found')

        settings_button = self.driver.find_elements_by_xpath("//*[contains(text(), 'Settings')]")
        self.assertIsNotNone(settings_button)
        self.log.info('settings_button found')

        profile_button = self.driver.find_elements_by_xpath("//*[contains(text(),'Profile')]")
        self.assertIsNotNone(profile_button)
        self.log.info('profile_button found')

        recommendation_button = self.driver.find_elements_by_xpath("//*[contains(text(), 'Recommendation')]")
        self.assertIsNotNone(recommendation_button)
        self.log.info('recommendation_button found')

    @unittest.skip("profilepage")
    def test_02_play_button_click(self):
        self.appInformation()   # print app info
        sleep(LET_ME_SLEEP_SHORT)
        play_button = self.driver.find_element_by_css_selector('.bubbly-btn.play-button')
        play_button.click()
        sleep(LET_ME_SLEEP_NAP)
        self.tearDown()

    @unittest.skip("profilepage")
    def test_03_grade_content_test(self):
        self.appInformation()   # print app info
        sleep(LET_ME_SLEEP_SHORT)
        play_button = self.driver.find_element_by_css_selector('.bubbly-btn.play-button')
        play_button.click()
        sleep(LET_ME_SLEEP_SHORT)

        # click on vocabulary
        check_current_active_tab = self.driver.find_element_by_css_selector('.tab-item.ng-binding.active')
        self.assertIsNotNone(check_current_active_tab)


        self.tearDown()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(EDTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
