import unittest

from config import log
from config import EnglishDuniyaSetup


GRADE_ONE = 1
GRADE_TWO = 2
GRADE_THREE = 3


class LessonTestCase(EnglishDuniyaSetup):
    
    def click_start_button(self):
        self.wait_for_element_and_click('by_id', 'landing-start-button', 30)

    def lesson_landing_back(self):
        log.info('lesson landing back button clicked')
        self.find_element_wait_and_click('by_id','lesson-landing-back-button', 10).click()

    def lesson_list_back(self):
        self.log.info('lesson list back button clicked')
        self.find_element_wait_and_click('by_id','lesson-list-back-button', 10).click()

    def lesson_category_home_back(self):
        self.log.info('lesson category back button clicked')
        self.find_element_wait_and_click('by_id','lesson-category-home-button', 10).click()
    
    def lesson_grade_selection(self, grade_item):
        self.wait_for_element_and_click('by_id', 'lesson-category-grade{}-tab'.format(grade_item), 30)
    
    def lesson_grade_skill_selection(self, skill_item):
        vocab_lesson_button = self.wait_for_element('by_id', 'lesson-category-vocabulary-tile', 30)
        grammar_lesson_button = self.wait_for_element('by_id', 'lesson-category-grammar-tile', 30)
        reading_lesson_button = self.wait_for_element('by_id', 'lesson-category-reading-tile', 30)
        listening_lesson_button = self.wait_for_element('by_id', 'lesson-category-listening-tile', 30)

        skill_list = {1: vocab_lesson_button, 2: grammar_lesson_button,
                      3: reading_lesson_button, 4: listening_lesson_button}

        skill_list.get(skill_item).click()

    def lesson_list(self):
        lesson_list = self.find_element_and_wait('by_css_selector')

    def lesson_selection(self):




    ############################
    ## TEST CASES GOES HERE
    ############################
    @unittest.skip("start lesson selection")
    def test_lesson_001_start_lesson_selection(self):
        self.click_start_button()
        self.let_me_sleep(3)
        self.go_back()
    
    @unittest.skip("lesson selection in loop")
    def test_lesson_002_start_lesson_selection_loop(self):
        for counter in range(100):
            self.click_start_button()
            self.let_me_sleep(2)
            self.go_back()
    
    # @unittest.skip("grade1")
    def test_lesson_003_start_take_grade_1_content(self):
        self.click_start_button()
        self.let_me_sleep(2)
        self.lesson_grade_selection(GRADE_ONE)
        self.lesson_grade_skill_selection(1)

    @unittest.skip("grade2")
    def test_lesson_004_start_take_grade_2_content(self):
        self.click_start_button()
        self.let_me_sleep(2)
        self.lesson_grade_selection(GRADE_TWO)
        self.lesson_grade_skill_selection(2)

    @unittest.skip("grade3")
    def test_lesson_005_start_take_grade_3_content(self):
        self.click_start_button()
        self.let_me_sleep(2)
        self.lesson_grade_selection(GRADE_THREE)
        self.lesson_grade_skill_selection(2)