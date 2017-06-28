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

logging.basicConfig(level=logging.INFO)

SKILL_VOCAB_UI = 1
SKILL_GRAMMAR = 2
SKILL_READING = 3
SKILL_LISTENING = 4


class EDTestCase(unittest.TestCase):
    ''' English Duniya App testing.
    '''

    #####################
    # application setup and settings goes here
    #####################
    def setUp(self):
        desired_caps = get_desired_capabilities('ed-240.apk')

        # web driver remote access
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.profile_score = 0
        self.log = logging.getLogger('ed-logger # ')

    def closeApp(self):
        self.driver.quit()

    def resetApp(self):
        self.driver.resetApp()

    def goBack(self):
        self.driver.back()

    def lesson_landing_back(self):
        self.log.info('lesson landing back button clicked')
        self.driver.find_element_by_id('lesson-landing-back-button').click()

    def lesson_list_back(self):
        self.log.info('lesson list back button clicked')
        self.driver.find_element_by_id('lesson-list-back-button').click()

    def lesson_category_home_back(self):
        self.log.info('lesson category back button clicked')
        self.driver.find_element_by_id('lesson-category-home-button').click()

    #####################
    # profile related stuff goes here
    #####################
    def check_current_state(self):
        sleep(SLEEP_QUICK)
        if self.driver.find_elements_by_xpath('/html/body/ion-nav-view/ion-nav-view/ion-view/ion-content/div/div[2]/button'):
            self.log.info('STATE : school selection form')
            return "school-select"
        elif self.driver.find_elements_by_id('landing-profiles-button'):
            self.log.info('STATE : landing profile page')
            return "landing-profile-page"
        elif self.driver.find_elements_by_xpath('/html/body/ion-nav-view/ion-nav-view/ion-view/div/div/div[2]/button'):
            self.log.info('STATE : diagnosis page')
            return 'diagnosis-screen'
        elif self.driver.find_elements_by_id('profile-0'):
            self.log.info('STATE : profile selection page')
            return 'profile-selection-page'
        elif self.driver.find_elements_by_id('profile-0') and self.driver.find_elements_by_id('profile-add'):
            self.log.info('STATE : profile create page')
            return 'can-create-profile'

    def enter_username(self):
        sleep(SLEEP_QUICK)
        self.driver.find_element_by_id('key-A').click()
        self.driver.find_element_by_id('key-B').click()
        self.driver.find_element_by_id('key-C').click()
        self.driver.find_element_by_id('key-D').click()
        self.driver.find_element_by_id('key-E').click()
        self.driver.find_element_by_id('register-submit-name').click()

    def select_gender(self):
        self.driver.find_element_by_id('radio-gender-male').click()
        self.driver.find_element_by_id('register-submit-gender').click()

    def select_class(self):
        self.driver.find_element_by_id('radio-grade-4').click()
        self.driver.find_element_by_id('register-submit-grade').click()

    def select_school(self):

        city = self.driver.find_element_by_xpath('/html/body/ion-nav-view/ion-nav-view/ion-view/ion-content/div/div[1]/div/ion-search-select[1]/div/input')
        locality = self.driver.find_element_by_xpath('/html/body/ion-nav-view/ion-nav-view/ion-view/ion-content/div/div[1]/div/ion-search-select[2]/div/input')
        school = self.driver.find_element_by_xpath('/html/body/ion-nav-view/ion-nav-view/ion-view/ion-content/div/div[1]/div/ion-search-select[3]/div/input')

        city.click()
        city.send_keys('Mumbai')

        locality.click()
        locality.send_keys('Adai')

        school.click()
        school.send_keys('Others')

    def enter_phone_number(self):
        pass

    def select_profile(self):
        profile = self.driver.find_element_by_id('profile-0')
        self.profile_score = int(profile.find_element_by_css_selector('.font-xl.font-bright-gold.ng-binding').text)
        self.log.info("Current Score "+str(self.profile_score))
        profile.click()

    def profile_add(self):
        profile_add = self.driver.find_elements_by_id('profile-add')
        if profile_add:
            profile_add[0].click()
        else:
            self.log.info('Profile creation limit exceeded.')
            self.closeApp()

    def open_profile_list(self):
        sleep(SLEEP_QUICK)

        profiles_button = self.driver.find_element_by_id('landing-profiles-button')
        profiles_button.click()

        sleep(SLEEP_QUICK)

    def app_launch_without_profile(self):
        pass

    # app launch with atleast one profile
    def app_launch_with_profile(self):
        sleep(SLEEP_SHORT)
        profile = self.driver.find_elements_by_id('profile-0')
        if profile:
            return profile[0]
        else:
            return None

    #####################
    # content related stuff goes here
    #####################
    def take_diagnosis(self):
        # start diagnosis button click
        self.driver.find_element_by_xpath('/html/body/ion-nav-view/ion-nav-view/ion-view/div/div/div[2]/button').click()

    def open_skill(self):
        self.driver.find_element_by_id('landing-start-button').click()

    def skill_selection(self, skill_map=None):
        grade_random = randint(1, 3)
        grade_selection = self.driver.find_element_by_id('lesson-category-grade{}-tab'.format(grade_random))
        self.log.info(grade_selection.text)

        grade_selection.click()

        vocab_lesson_button = self.driver.find_element_by_id('lesson-category-vocabulary-tile')
        grammar_lesson_button = self.driver.find_element_by_id('lesson-category-grammar-tile')
        reading_lesson_button = self.driver.find_element_by_id('lesson-category-reading-tile')
        listening_lesson_button = self.driver.find_element_by_id('lesson-category-listening-tile')

        skill_list = {1: vocab_lesson_button, 2: grammar_lesson_button, 3: reading_lesson_button, 4: listening_lesson_button}

        if skill_map:
            skill_list.get(skill_map).click()
        else:
            skill_list.get(randint(1, 3)).click()

    def lesson_selection(self):
        lesson_id = 'lesson-list-lesson{}-tile'.format(randint(1,1))
        self.log.info('LESSON #>>'+lesson_id)
        lesson_item = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, lesson_id)))
        lesson_item.click()
        sleep(SLEEP_QUICK)

    def open_quiz(self):
        lesson_title = self.driver.find_element_by_id('lesson-landing-title').text
        self.log.info(lesson_title)
        self.driver.find_element_by_id('lesson-landing-resource-assessment-tile').click()

    def open_vocabulary(self):
        lesson_title = self.driver.find_element_by_id('lesson-landing-title').text
        self.log.info(lesson_title)

        resource_vocab = self.driver.find_elements_by_id('lesson-landing-resource-vocabulary-tile')
        if resource_vocab:
            resource_vocab[0].click()
        else:
            self.log.info("No VOCAB UI for "+lesson_title)
            self.closeApp()

    def open_recommendation(self):
        lesson_title = self.driver.find_element_by_id('lesson-landing-title').text
        self.log.info(lesson_title)
        self.driver.find_element_by_id('lesson-landing-next-lesson').click()

    def take_quiz(self):
        sleep(SLEEP_SHORT)
        questions = self.driver.find_elements_by_css_selector('.slider-slide')
        for key, question in enumerate(questions):
            self.log.info("selecting option for question #"+str(key))
            sleep(SLEEP_QUICK)
            question.find_element_by_id('question-{}-option-{}'.format(key, randint(0, 1))).click()
            self.driver.find_element_by_id('quiz-submit').click()
            self.log.info("submitting answer for question #"+str(key))
            sleep(SLEEP_QUICK)
        sleep(SLEEP_QUICK)
        # submit report        
        result_page = self.driver.find_element_by_xpath('/html/body/ion-nav-view/ion-nav-view/ion-view/ion-content/div[1]/div/div/div[3]/button')
        self.log.info("closing report page")
        result_page.click()

    def take_vocaab_ui(self):
        try:
            next_button = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".sbtn.sbtn-arrow-forward")))
            self.log.info("next button is visible")
            vocab_cards = self.driver.find_elements_by_css_selector(".flash-card.align-middle")
            self.log.info("all vocab cards are available")

            for key, vocab_card in enumerate(vocab_cards):
                next_button_active = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".sbtn.sbtn-arrow-forward")))
                next_button_active.click()
                self.log.info("VocabCard #"+str(key))
                sleep(SLEEP_QUICK)

                submit_button_inactive = self.driver.find_elements_by_css_selector(".sbtn.sbtn-arrow-finish.ng-hide")
                if not submit_button_inactive:
                    self.log.info('submit button visible')
                    submit_button_active = self.driver.find_element_by_css_selector(".sbtn.sbtn-arrow-finish")
                    sleep(SLEEP_QUICK)
                    submit_button_active.click()
                    self.log.info('submit button clicked')

            sleep(SLEEP_QUICK)
            submit_button = self.driver.find_element_by_xpath("/html/body/ion-nav-view/ion-nav-view/ion-view/ion-content/div[1]/div/div/div[3]/button")
            submit_button.click()
            self.profile_score_new = self.profile_score_old + 3
            self.log.info("Report Page clicked")
        except Exception as e:
            self.log.info('Something went wrong please check your appium log')
            pass

    #####################
    # test cases goes here
    #####################
    @unittest.skip("profile creation")
    def test_001_profile_creation(self):
        # check if app is launched first time or not
        current_state = self.check_current_state()
        if 'school-select' == current_state:
            self.select_school()
        elif 'diagnosis-screen' == current_state:
            self.take_diagnosis()
        elif 'can-create-profile' == current_state or current_state == "profile-selection-page":
            self.open_profile_list()
            self.profile_add()
            self.enter_username()
            self.select_gender()
            self.select_class()
            self.select_school()
        else:
            self.open_profile_list()
            self.profile_add()
            self.enter_username()
            self.select_gender()
            self.select_class()
            self.select_school()

    @unittest.skip("profile switch")
    def test_002_profile_switch(self):
        # check if app is launched first time or not
        current_state = self.check_current_state()
        if current_state == "profile-selection-page":
            self.select_profile()
        else:
            self.open_profile_list()
            self.select_profile()

    @unittest.skip("take quiz")
    def test_003_take_quiz(self):
        current_state = self.check_current_state()
        if current_state == "profile-selection-page":
            self.select_profile()
            sleep(SLEEP_QUICK)

        self.open_skill()
        self.skill_selection()
        self.lesson_selection()
        self.open_quiz()
        self.take_quiz()

        sleep(SLEEP_SHORT)
        self.closeApp()

    @unittest.skip("take vocab")
    def test_004_take_vocabui(self):
        current_state = self.check_current_state()
        if current_state == "profile-selection-page":
            self.select_profile()
            sleep(SLEEP_QUICK)

        self.open_skill()
        self.skill_selection(SKILL_VOCAB_UI)
        self.lesson_selection()
        self.open_vocabulary()
        self.take_vocaab_ui()

        sleep(SLEEP_SHORT)
        self.closeApp()

    # BREAK IT
    # @unittest.skip("breaking")
    def test_001_break_it(self):
        current_state = self.check_current_state()
        if current_state == "profile-selection-page":
            self.select_profile()
            sleep(SLEEP_QUICK)

        for counter in range(50):
            self.log.info('TEST #'+str(counter))

            self.open_skill()
            self.skill_selection()
            self.lesson_selection()
            self.open_quiz()
            self.take_quiz()

            self.lesson_landing_back()
            sleep(SLEEP_QUICK)

            self.lesson_list_back()
            sleep(SLEEP_QUICK)

            self.lesson_category_home_back()
            sleep(SLEEP_QUICK)

            # test vocabUI

            # self.open_skill()
            # self.skill_selection(SKILL_VOCAB_UI)
            # self.lesson_selection()
            # self.open_vocabulary()
            # self.take_vocaab_ui()

            sleep(SLEEP_SHORT)




###########################
# Actual Code Starts Here
###########################
if __name__ == '__main__':
    check_device_availability()
    suite = unittest.TestLoader().loadTestsFromTestCase(EDTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)