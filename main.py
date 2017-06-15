import unittest
from appium import webdriver
from time import sleep
import logging
import desired_capabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

logging.basicConfig(level=logging.INFO)
context_name = "WEBVIEW"

LET_ME_SLEEP_LONG = 20
LET_ME_SLEEP_SHORT = 10
LET_ME_SLEEP_NAP = 5
LET_ME_SLEEP_QUICK = 2


class EDTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities('zaya-mobile-pipeline-combined3.apk')

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

    @unittest.skip("profilepage play button click")
    def test_02_play_button_click(self):
        self.appInformation()   # print app info
        sleep(LET_ME_SLEEP_SHORT)
        play_button = self.driver.find_element_by_css_selector('.bubbly-btn.play-button')
        play_button.click()
        sleep(LET_ME_SLEEP_NAP)
        self.tearDown()

    # @unittest.skip("grade content test")
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
        # quiz_button = self.driver.find_element_by_xpath('/html/body/ion-nav-view/ion-nav-view/div/ion-content/div/div/div[1]')
        # vocab_button = self.driver.find_element_by_xpath('/html/body/ion-nav-view/ion-nav-view/div/ion-content/div/div/div[2]')
        quiz_button = self.driver.find_element_by_xpath('/html/body/ion-nav-view/ion-nav-view/div/div/div[1]/button')

        # testing quiz
        quiz_button.click()
        self.log.info("quiz item clicked")
        sleep(LET_ME_SLEEP_SHORT)

        # question lists
        # import ipdb; ipdb.set_trace()
        self.log.info("waiting for question lists")
        # questions = WebDriverWait(self.driver, LET_ME_SLEEP_LONG).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, "slider-slides"))
        # )

        # //*[@id="tour-container"]/div[2]/div[1]
        import ipdb; ipdb.set_trace()
        questions = self.driver.find_elements_by_xpath('//*[@id="tour-container"]/div[2]/div[1]')
        self.log.info("question list available")
        for question in questions:
            print (question)
        #
        # counter = 0
        # for question in questions:
        #     counter = counter + 1
        #     self.log.info("selecting option for question #"+str(key))
        #     sleep(LET_ME_SLEEP_QUICK)
        #     question.find_element_by_id('question-{}-option-{}'.format(counter, 1)).click()
        #
        #     # submit question
        #     self.driver.find_element_by_id('quiz-submit').click()
        #     self.log.info("submitting answer for question #"+str(counter))

        sleep(LET_ME_SLEEP_NAP)
        # submit report
        #self.driver.find_element_by_css_selector('.sbtn.sbtn-next-yellow').click()

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
        registration_submit_button_click = self.driver.find_element_by_id('register-submit-name').click()

        sleep(LET_ME_SLEEP_NAP)
        gender_selection_boy = self.driver.find_element_by_xpath('//*[@id="radio-gender-male"]').click()

        sleep(LET_ME_SLEEP_NAP)
        submit_gender_form = self.driver.find_element_by_id('register-submit-gender').click()

        grade_selection = self.driver.find_element_by_id('radio-grade-3').click()

        sleep(LET_ME_SLEEP_NAP)
        submit_grade_form = self.driver.find_element_by_id('register-submit-grade').click()

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
