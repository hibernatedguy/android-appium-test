import unittest
from random import randint

from config import log
from config import EnglishDuniyaSetup


GRADE_ONE = 1
GRADE_TWO = 2
GRADE_THREE = 3


class LessonTestCase(EnglishDuniyaSetup):

    ###############
    # QUIZ TEST
    ###############
    def open_quiz(self):
        lesson_title = self.find_element_and_wait('by_id', 'lesson-landing-title', 2)
        log.info(lesson_title.text)
        self.find_element_and_click('by_id', 'lesson-landing-resource-assessment-tile', 3)

    def take_quiz(self):
        # WAIT FOR QUESTIONS
        self.wait_for_element('by_css_selector', '.slider-slide', 10)
        questions = self.find_elements_and_wait('by_css_selector',        
                                                '.slider-slide', 10)
        # ITERATE QUESTIONS
        for index, question in enumerate(questions):
            log.info("selecting option for question #" + str(index))
            question.find_element_by_id('question-{}-option-{}'.format(index, randint(0, 1))).click()
            self.find_element_click_and_wait('by_id','quiz-submit', 3)

        # REPORT SUBMIT
        result_page = self.find_element_and_click('by_xpath', '/html/body/ion-nav-view/ion-nav-view/ion-view/ion-content/div[1]/div/div/div[3]/button', 3)

    ###############
    # LESSON TEST
    ###############
    def click_start_button(self):
        self.wait_for_element_and_click('by_id', 'landing-start-button', 30)

    def lesson_landing_back(self):
        log.info('lesson landing back button clicked')
        self.find_element_wait_and_click('by_id', 'lesson-landing-back-button', 10).click()

    def lesson_list_back(self):
        log.info('lesson list back button clicked')
        self.find_element_wait_and_click('by_id', 'lesson-list-back-button', 10).click()

    def lesson_category_home_back(self):
        log.info('lesson category back button clicked')
        self.find_element_wait_and_click('by_id', 'lesson-category-home-button', 10).click()

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
        self.let_me_sleep(10)   # wait for 30sec and get the list of lessons
        lesson_list = self.find_elements_and_wait('by_css_selector', '.cards-holder.cards-md.animated.fadeIn', 5)
        return lesson_list

    def lesson_selection(self):
        for index, lesson in enumerate(self.lesson_list()):
            log.info("lesson" + str(index))
            lesson_id = 'lesson-list-lesson{}-tile'.format(index)
            self.wait_for_element_and_click('by_id', lesson_id, 30)
            self.let_me_sleep(3)

            # open quiz
            self.open_quiz()
            self.take_quiz()

            self.go_back()

    ############################
    # TEST CASES GOES HERE
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
        self.lesson_selection()

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
