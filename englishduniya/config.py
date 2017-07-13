import logging
import unittest
from time import sleep
import datetime

from appium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from desired_capabilities import (get_desired_capabilities)

log_date = datetime.datetime.now().date().isoformat()

logging.basicConfig(filename='ed-logger___'+log_date+'__.log', level=logging.INFO, format='%(asctime)s : %(message)s')
log = logging.getLogger('ed-logger # ')


class EnglishDuniyaSetup(unittest.TestCase):

    ''' English Duniya App Testing
    '''

    def setUp(self):
        desired_caps = get_desired_capabilities('311_ta_bundle.apk')
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

        self.profile_score = 0

        self.default_wait = 3
        self.quick_wait = 5
        self.short_wait = 10
        self.long_wait = 30

        self.config_wait_for_element = {
            'by_id': By.ID,
            'by_css_selector': By.CSS_SELECTOR,
            'by_xpath': By.XPATH,
        }

        self.config_find_element = {
            'by_id': self.driver.find_element_by_id,
            'by_css_selector': self.driver.find_element_by_css_selector,
            'by_xpath': self.driver.find_element_by_xpath,
        }

        self.config_find_elements = {
            'by_id': self.driver.find_elements_by_id,
            'by_css_selector': self.driver.find_elements_by_css_selector,
            'by_xpath': self.driver.find_elements_by_xpath,
        }

    ####################
    # CUSTOM METHODS
    ####################
    def let_me_sleep(self, wait_time):
        return sleep(wait_time)

    # App Information
    def app_informtion(self, message):
        log.info("### {} --- {} ###".format(message, self.driver.contexts[-1]))

    ##################
    # WAIT FOR ELEMENT
    ##################
    def wait_for_element(self, method, element_key, wait_time):
        return WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located((self.config_wait_for_element.get(method), element_key)))

    def wait_for_element_and_click(self, method, element_key, wait_time):
        _elemet = WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located((self.config_wait_for_element.get(method), element_key)))
        _elemet.click()

    ############
    # FIND ELEMENTS
    ############
    def find_element_and_wait(self, method, element_key, wait_time=0):
        sleep(wait_time)
        return self.config_find_element.get(method)(element_key)

    def find_element_wait_and_click(self, method, element_key, wait_time=0):
        sleep(wait_time)
        select_element = self.config_find_element.get(method)(element_key)
        select_element.click()

    def find_element_click_and_wait(self, method, element_key, wait_time=0):
        select_element = self.config_find_element.get(method)(element_key)
        select_element.click()
        sleep(wait_time)

    ############
    # ELEMENTS
    ############
    def find_elements_and_wait(self, method, element_key, wait_time=0):
        sleep(wait_time)
        return self.config_find_elements.get(method)(element_key)

    ####################
    # HARDWARE BUTTONS
    ####################
    def close_app(self):
        log.info('CLOSING APP')
        self.driver.quit()

    def go_back(self):
        log.info('BACK BUTTON PRESSED')
        self.driver.back()

    def reset_app(self):
        log.info('RESETTING APP')
        self.driver.reset()
