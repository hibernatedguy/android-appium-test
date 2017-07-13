import unittest
from random import randint

from config import log
from config import EnglishDuniyaSetup


class ProfileTestCase(EnglishDuniyaSetup):
    ##########################################
    # STARTUP CHECKS
    # 1. profile creation
    # 2. grade selection
    # 3. phone number checks
    # 4. take diagnosis
    # 5. select school
    # 6. select
    ##########################################

    def lesson_category_home_back(self):
        self.wait_for_element_and_click('by_id', 'lesson-category-home-button', 10)
        log.info('CLICKED lesson category back button')

    def profile_selection_button_click(self):
        self.wait_for_element_and_click('by_id', 'landing-profiles-button', 30)
        log.info('CLICKED profile button')

    def profile_select(self, profile_id):
        _profile_id = 'profile-{}'.format(profile_id)
        self.wait_for_element_and_click('by_id', _profile_id, 40)
        log.info('SELECTING profile #{}'.format(profile_id))

    def click_start_button(self):
        app_version = self.wait_for_element('by_xpath',
                                            '/html/body/ion-nav-view/ion-nav-view/div/div[1]', 30).text
        log.info("### APP VERSION ### {} ### ".format(app_version))
        self.wait_for_element_and_click('by_id', 'landing-start-button', 30)
        log.info('CLICKED lesson start button')

    ##################
    # TEST CASE GOES HERE
    ##################
    @unittest.skip("profile click")
    def test_000_select_profile(self):
        log.info('profile button click')

    # @unittest.skip("profile selection automation")
    def test_001_profile_selection_automation(self):
        counter = 0
        for count in range(20):
            counter = counter + 1
            log.info('TESTING #{}'.format(counter))
            self.app_informtion("Profile Selection Automation")
            self.profile_selection_button_click()
            self.profile_select(randint(0, 0))
            self.click_start_button()
            self.lesson_category_home_back()
