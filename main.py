import unittest
from appium import webdriver
from time import sleep
import logging
import desired_capabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

logging.basicConfig(level=logging.INFO)
context_name = "WEBVIEW"

LET_ME_SLEEP_LONG = 20
LET_ME_SLEEP_SHORT = 7
LET_ME_SLEEP_NAP = 5
LET_ME_SLEEP_QUICK = 2
BACK_BUTTON_KEY_CODE = 4

NO_CONNECT = 0
AIRPLANE_MODE_CONNECT = 1
WIFI_MODE_CONNECT = 2
DATA_MODE_CONNECT = 4
ALL_NETWORK_MODE_CONNECT = 6

class EDTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities('26june2017.apk')

        # web driver remote access
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.log = logging.getLogger('appium-ed-logger # ')

    def closeApp(self):
        self.driver.quit()

    def resetApp(self):
        self.driver.resetApp()

    def goBack(self):
        self.driver.back()

    def appInformation(self):
        print (self.driver.contexts[-1])

    def assertEqualMethodCheck(self, element, msg):
        negative_msg = '{} not found'.format(msg)
        positive_msg = '{} found'.format(msg)
        return self.log.info(negative_msg) if self.assertIsNotNone(element) else self.log.info(positive_msg)

    def enableFlightMode(self,context):
        driver.mobile.set_network_connection(self.driver.mobile.AIRPLANE_MODE)

    def enableDataMode(self,context):
        driver.mobile.set_network_connection(self.driver.mobile.AIRPLANE_MODE)

    def enableWifiMode(self,context):
        driver.mobile.set_network_connection(self.driver.mobile.AIRPLANE_MODE)

    def enableAllMode(self,context):
        driver.mobile.set_network_connection(self.driver.mobile.AIRPLANE_MODE)

    @unittest.skip("check network-connection")
    def test_000_get_network_connection(self):
        self.appInformation()   # print app info
        nc = self.driver.network_connection
        self.assertIsInstance(nc, int)

    @unittest.skip("set network connection")
    def test_000_set_network_connection(self):
        nc = self.driver.network_connection
        self.assertIsInstance(nc, int)

    @unittest.skip("profilepage")
    def test_001_network_connection(self):
        nc = self.driver.set_network_connection(ConnectionType.DATA_ONLY)
        self.assertIsInstance(nc, int)
        self.assertEqual(nc, ConnectionType.DATA_ONLY)

    @unittest.skip("profilepage")
    def test_00_profilepage(self):
        self.appInformation()   # print app info
        self.driver.resetApp()
        sleep(LET_ME_SLEEP_LONG)
        profile_element = self.driver.find_element_by_id("profile-0").click()
        # el = self.driver.find_element_by_id('profile-0')
        self.assertIsNotNone(profile_element)
        sleep(LET_ME_SLEEP_LONG)

    @unittest.skip("profilepage button visibility")
    def test_01_after_profile_button_visibility(self):
        self.appInformation()   # print app info
        sleep(LET_ME_SLEEP_SHORT)
        play_button = self.driver.find_element_by_css_selector('.bubbly-btn.play-button')
        self.assertEqualMethodCheck(play_button, 'play button')

        settings_button = self.driver.find_element_by_xpath("//*[contains(text(), 'Settings')]")
        self.assertEqualMethodCheck(settings_button, 'settings button')

        profile_button = self.driver.find_element_by_xpath("//*[contains(text(),'Profile')]")
        self.assertEqualMethodCheck(profile_button, 'profile button')

        recommendation_button = self.driver.find_element_by_xpath("//*[contains(text(), 'Recommendation')]")
        recommendation_button.click()
        self.assertEqualMethodCheck(recommendation_button, 'recommendation button')

    def select_grade_content(self):
        content_play_button = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/ion-nav-view/ion-nav-view/div/div[3]/button")))
        content_play_button.click()

        sleep(LET_ME_SLEEP_SHORT)

        select_category = self.driver.find_element_by_xpath('/html/body/ion-nav-view/ion-nav-view/div/ion-content/div/div/div/div[1]')
        select_category.click()

        # load_content_button = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/ion-nav-view/ion-nav-view/div/div[3]/button")))
        # sleep(LET_ME_SLEEP_QUICK)        
        # load_content_button.click()

        # self.goBack()        

    def choose_profile(self):
        choose_profile_button = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/ion-nav-view/ion-nav-view/div/div[2]/button")))
        choose_profile_button.click()

        select_profile = self.driver.find_element_by_xpath('//*[@id="choose-profile-view"]/div/div/div[1]')
        select_profile.click()


    # @unittest.skip("profilepage play button click")
    def test_02_play_button_click(self):
        self.appInformation()   # print app info

        # for x in range(50):
        #     self.select_grade_content()
        #     sleep(LET_ME_SLEEP_SHORT)
        #     self.goBack()
        #     sleep(LET_ME_SLEEP_QUICK)
        #     self.goBack()

        for x in range(50):
            self.choose_profile()
            sleep(LET_ME_SLEEP_QUICK)
            self.select_grade_content()
            sleep(LET_ME_SLEEP_SHORT)
            self.goBack()
            sleep(LET_ME_SLEEP_SHORT)
            self.goBack()

        # skill tag click
        # self.driver.find_element_by_xpath("/html/body/ion-nav-view/ion-nav-view/div/ion-content/div/div/div[1]/div[1]/a").click()
        # sleep(LET_ME_SLEEP_QUICK)
        # self.log.info("skill tag clicked")
        #
        # available_cards = self.driver.find_elements_by_css_selector(".cards-holder")
        # import ipdb; ipdb.set_trace()
        # self.driver.scroll(available_cards[0], available_cards[-1])


        # action = TouchAction(self.driver)
        # action.press(element_to_pull, x=10, y=10).move_to(x=10, y=400).release().perform()


    def quiz_question_test(self):

        self.log.info("quiz item clicked")
        sleep(LET_ME_SLEEP_SHORT)

        # question lists
        self.log.info("waiting for question lists")

        # //*[@id="tour-container"]/div[2]/div[1]
        questions = self.driver.find_elements_by_css_selector('.slider-slide')
        self.log.info("question list available")

        for key, question in enumerate(questions):
            self.log.info("selecting option for question #"+str(key))
            sleep(LET_ME_SLEEP_QUICK)
            question.find_element_by_id('question-{}-option-{}'.format(key, 1)).click()

            # submit question
            self.driver.find_element_by_id('quiz-submit').click()
            self.log.info("submitting answer for question #"+str(key))
            sleep(LET_ME_SLEEP_QUICK)

        sleep(LET_ME_SLEEP_NAP)
        # submit report
        self.driver.find_element_by_css_selector('.sbtn.sbtn-next-yellow').click()

    def vocab_ui_test(self):
        self.log.info('VocabUI clicked ')
        sleep(LET_ME_SLEEP_NAP)
        try:
            next_button = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".sbtn.sbtn-arrow-forward")))
            self.log.info("next button is visible")
            vocab_cards = self.driver.find_elements_by_css_selector(".flash-card.align-middle")
            self.log.info("all vocab cards are available")

            for key, vocab_card in enumerate(vocab_cards):
                next_button_active = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".sbtn.sbtn-arrow-forward")))
                next_button_active.click()
                self.log.info("VocabCard #"+str(key))
                sleep(LET_ME_SLEEP_QUICK)

                submit_button_inactive = self.driver.find_elements_by_css_selector(".sbtn.sbtn-arrow-finish.ng-hide")
                if not submit_button_inactive:
                    self.log.info('submit button visible')
                    submit_button_active = self.driver.find_element_by_css_selector(".sbtn.sbtn-arrow-finish")
                    submit_button_active.click()
                    self.log.info('submit button clicked')

            sleep(LET_ME_SLEEP_QUICK)
            submit_button = self.driver.find_element_by_id("result-next")
            submit_button.click()
            self.log.info("Report Page clicked")

        except Exception as e:
            pass

    @unittest.skip("grade content test")
    def test_03_grade_content_quiz_test(self):
        sleep(LET_ME_SLEEP_SHORT)

        # playbutton click
        self.driver.find_element_by_css_selector('.bubbly-btn.play-button').click()
        sleep(LET_ME_SLEEP_QUICK)
        self.log.info("play button clicked")

        # skill tag click
        self.driver.find_element_by_xpath("/html/body/ion-nav-view/ion-nav-view/div/ion-content/div/div/div[1]/div[1]/a").click()
        sleep(LET_ME_SLEEP_QUICK)
        self.log.info("skill tag clicked")

        # lesson item click
        self.driver.find_element_by_xpath('//*[@id="content-list-view"]/ion-content/div/div[1]/a').click()
        self.log.info("lesson item clicked")
        sleep(LET_ME_SLEEP_QUICK)

        #quiz button
        quiz_button = self.driver.find_element_by_xpath('/html/body/ion-nav-view/ion-nav-view/div/ion-content/div/div/div[1]')
        vocab_button = self.driver.find_element_by_xpath('/html/body/ion-nav-view/ion-nav-view/div/ion-content/div/div/div[2]')

        # TESTING QUIZ QUESTIONS
        quiz_button.click()
        self.quiz_question_test()

        # TESTING VOCABULARY QUESTIONS
        vocab_button.click()
        self.vocab_ui_test()

        sleep(LET_ME_SLEEP_LONG)
        self.closeApp()

    @unittest.skip("grade content list search")
    def test_04_grade_content_list_search(self):
        sleep(LET_ME_SLEEP_NAP)

        # playbutton click
        play_button = self.driver.find_element_by_css_selector('.bubbly-btn.play-button')
        play_button.click()

        # skill tag click
        self.driver.find_element_by_xpath("/html/body/ion-nav-view/ion-nav-view/div/ion-content/div/div/div[1]/div[1]/a").click()
        sleep(LET_ME_SLEEP_QUICK)

        search_bar = self.driver.find_element_by_xpath('//*[@id="content-list-view"]/div/label/input')
        search_bar.click()
        search_bar.send_keys("colours")

        sleep(LET_ME_SLEEP_QUICK)

        lesson_list_item = self.driver.find_element_by_xpath('//*[@id="content-list-view"]/ion-content/div/div[1]/a')
        lesson_list_item.click()

        sleep(LET_ME_SLEEP_SHORT)

        self.goBack()
        self.goBack()
        self.goBack()

        sleep(LET_ME_SLEEP_SHORT)

        self.closeApp()

    @unittest.skip("profile registration")
    def test_04_profile_registration(self):
        self.appInformation()
        sleep(LET_ME_SLEEP_NAP)

        key_f = self.driver.find_element_by_id('key-F').click()
        key_u = self.driver.find_element_by_id('key-u').click()
        key_k = self.driver.find_element_by_id('key-K').click()
        key_r = self.driver.find_element_by_id('key-R').click()
        key_e = self.driver.find_element_by_id('key-E').click()

        sleep(LET_ME_SLEEP_NAP)
        self.driver.find_element_by_id('register-submit-name').click()

        sleep(LET_ME_SLEEP_NAP)
        self.driver.find_element_by_xpath('//*[@id="radio-gender-male"]').click()

        sleep(LET_ME_SLEEP_NAP)
        self.driver.find_element_by_id('register-submit-gender').click()

        self.driver.find_element_by_id('radio-grade-3').click()

        sleep(LET_ME_SLEEP_NAP)
        self.driver.find_element_by_id('register-submit-grade').click()

        sleep(LET_ME_SLEEP_LONG)

    @unittest.skip("phone number registration")
    def test_05_profile_phone_registration(self):
        self.appInformation()

        sleep(LET_ME_SLEEP_NAP)

        self.driver.find_element_by_xpath('/html/body/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div/div/div[5]/virtual-numpad/div[3]/a[3]').click()
        self.driver.find_element_by_xpath('/html/body/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div/div/div[5]/virtual-numpad/div[1]/a[1]').click()
        self.driver.find_element_by_xpath('/html/body/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div/div/div[5]/virtual-numpad/div[1]/a[2]').click()
        self.driver.find_element_by_xpath('/html/body/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div/div/div[5]/virtual-numpad/div[1]/a[3]').click()
        self.driver.find_element_by_xpath('/html/body/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div/div/div[5]/virtual-numpad/div[2]/a[1]').click()
        self.driver.find_element_by_xpath('/html/body/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div/div/div[5]/virtual-numpad/div[2]/a[2]').click()
        self.driver.find_element_by_xpath('/html/body/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div/div/div[5]/virtual-numpad/div[2]/a[3]').click()
        self.driver.find_element_by_xpath('/html/body/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div/div/div[5]/virtual-numpad/div[3]/a[1]').click()
        self.driver.find_element_by_xpath('/html/body/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div/div/div[5]/virtual-numpad/div[3]/a[2]').click()
        self.driver.find_element_by_xpath('/html/body/ion-nav-view/ion-nav-view/div/ion-view/ion-content/div/div/div[5]/virtual-numpad/div[3]/a[3]').click()

        self.driver.find_element_by_css_selector('.sbtn.sbtn-next.sbtn-next-blue').click()

        sleep(LET_ME_SLEEP_LONG)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(EDTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
