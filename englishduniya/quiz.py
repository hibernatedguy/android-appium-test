from config import log
from config import EnglishDuniyaSetup

VOCAB = 1
PRACTICE = 2
VIDEO = 3


class QuizTestCase(EnglishDuniyaSetup):

    def open_quiz(self):
        lesson_title = self.find_element_and_wait('by_id', 'lesson-landing-title', 2)
        self.log.info(lesson_title)
        self.find_elements_and_click('by_id', 'lesson-landing-resource-assessment-tile', 3)

    def take_quiz(self):
        # WAIT FOR QUESTIONS
        self.wait_for_element('by_css_selector', '.slider-slide', 0)
        questions = self.find_elements_and_wait('by_css_selector',
                                                '.slider-slide', 0)

        # ITERATE QUESTIONS
        for index, question in enumerate(questions):
            self.log.info("selecting option for question #" + str(index))
            question.find_element_and_click('by_id',
                                            'question-{}-option-{}'.
                                            format(key, randint(0, 1)),
                                            3)
        self.find_element_and_click('quiz-submit')
        self.let_me_sleep(4)

        # REPORT SUBMIT
        result_page = self.find_element_and_click('by_xpath', )
        result_page = self.driver.find_element_by_xpath(
            '/html/body/ion-nav-view/ion-nav-view/ion-view/ion-content/div[1]/div/div/div[3]/button', 3)
