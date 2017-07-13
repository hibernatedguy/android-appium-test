import unittest
from random import randint

from config import log
from config import EnglishDuniyaSetup

GRADE_ONE = 1
GRADE_TWO = 2
GRADE_THREE = 3

GRADE_SKILL_VOCAB = 1
GRADE_SKILL_GRAMMAR = 2
GRADE_SKILL_READING = 3
GRADE_SKILL_LISTENING = 4


class LessonTestCase(EnglishDuniyaSetup):
    ##########################################
    # APPLICATION BUTTONS
    # 1. lesson back buttons
    # 2. lesson list back buttons
    # 3. lesson category home buttons
    ##########################################
    def lesson_landing_back(self):
        log.info('lesson landing back button clicked')
        self.wait_for_element_and_click('by_id', 'lesson-landing-back-button', 10)

    def lesson_list_back(self):
        log.info('lesson list back button clicked')
        self.wait_for_element_and_click('by_id', 'lesson-list-back-button', 10)

    def lesson_category_home_back(self):
        log.info('lesson category back button clicked')
        self.wait_for_element_and_click('by_id', 'lesson-category-home-button', 10)

    ##########################################
    # QUIZ TEST
    # 1. open quiz
    # 2. take quiz
    # 3. take recommended lesson
    ##########################################

    def open_quiz(self):
        log.info("opening quiz..")
        lesson_title = self.find_element_and_wait('by_id', 'lesson-landing-title', 2)
        log.info("TAKING QUIZ FOR {}".format(lesson_title.text))
        self.wait_for_element_and_click('by_id', 'lesson-landing-resource-assessment-tile', 4)

    def take_quiz(self):
        log.info("taking quiz..")
        # WAIT FOR QUESTIONS
        self.wait_for_element('by_css_selector', '.slider-slide', 30)
        questions = self.find_elements_and_wait('by_css_selector',
                                                '.slider-slide', 5)
        # ITERATE QUESTIONS
        for index, question in enumerate(questions):
            log.info("selecting option for question #" + str(index))
            question.find_element_by_id('question-{}-option-{}'.format(index, randint(0, 1))).click()
            self.find_element_click_and_wait('by_id', 'quiz-submit', 3)

        # REPORT SUBMIT
        self.wait_for_element_and_click(
            'by_xpath', '/html/body/ion-nav-view/ion-nav-view/ion-view/ion-content/div[1]/div/div/div[3]/button', 10)

    def take_recommended_lesson(self):
        log.info("TAKING RECOMMENDED LESSON")
        self.find_element_wait_and_click('by_id', 'landing-start-button', 20)
        self.open_quiz()
        self.take_quiz()

    ##########################################
    # VOCAB TEST CASES
    # 1. open vocab
    # 2. take vocab ui content
    ##########################################
    def open_vocan_ui(self):
        log.info('OPENING vocabui')
        self.wait_for_element_and_click('by_id', 'lesson-landing-resource-vocabulary-tile', 10)

    def take_vocab_ui(self):
        log.info('TAKING vocabui')

        try:
            # wait for the next button to appear and flash cards
            self.wait_for_element('by_css_selector', '.sbtn.sbtn-arrow-forward', 50)
            self.wait_for_element('by_css_selector', '.flash-card.align-middle', 50)

            # prepare the list of vocab cards
            vocab_cards = self.find_elements_and_wait('by_css_selector', '.flash-card.align-middle', 2)
            log.info("AVAILABLE VOCAB CARDS #{}".format(len(vocab_cards)))

            for key, vocab_card in enumerate(vocab_cards):
                log.info('SELECTING {} vocab-card'.format(key + 1))
                # wait for the next-vocab button to appear and click

                self.wait_for_element_and_click('by_css_selector', '.sbtn.sbtn-arrow-forward', 30)
                self.let_me_sleep(5)

                # check if submit-vocab button is available
                submit_button_inactive = self.find_elements_and_wait('by_css_selector',
                    '.sbtn.sbtn-arrow-finish.ng-hide', 0)

                if not submit_button_inactive:
                    # finish vocab
                    self.wait_for_element_and_click('by_css_selector', '.sbtn.sbtn-arrow-finish', 30)
                    self.let_me_sleep(3)
                    log.info('SUBMIT vocab')
                    break
                else:
                    log.info('submit_button_inactive not visible')

            self.find_element_wait_and_click(
                'by_css_selector', '.animated.pulse.infinite.cbtn.cbtn-block.cbtn-yellow', 3)
        except Exception as e:
            log.info('Something went wrong please check your appium log : {}'.format(e))
            pass

    #####################
    # VIDEO TEST CASES
    #####################
    def open_video(self):
        log.info('OPENING video')
        self.wait_for_element_and_click('by_id', 'lesson-landing-resource-resource-tile', 30)

    def take_video(self):
        ''' watch video and go back '''
        log.info('PLAYING video')
        self.wait_for_element_and_click('by_css_selector', '.animated.pulse.infinite.cbtn.cbtn-block.cbtn-yellow', 300)

    ##############################
    # APP NAVIGATIONS
    # 1. start button click
    # 2. lesson grade selections
    # 3. skill selection
    # 4. lesson list
    # 5. lesson resource selections
    # 6. lesson consumption
    ##############################

    def click_start_button(self):
        app_version = self.wait_for_element('by_xpath',
                                            '/html/body/ion-nav-view/ion-nav-view/div/div[1]', 30).text
        log.info("### APP VERSION ### {} ### ".format(app_version))
        self.wait_for_element_and_click('by_id', 'landing-start-button', 30)

    def lesson_grade_selection(self, grade_item):
        log.info("selecting grade #{}".format(grade_item))
        self.wait_for_element_and_click('by_id', 'lesson-category-grade{}-tab'.format(grade_item), 30)

    def lesson_grade_skill_selection(self, skill_item):
        log.info("selecting skill #{}".format(skill_item))

        vocab_lesson_button = self.wait_for_element('by_id', 'lesson-category-vocabulary-tile', 30)
        grammar_lesson_button = self.wait_for_element('by_id', 'lesson-category-grammar-tile', 30)
        reading_lesson_button = self.wait_for_element('by_id', 'lesson-category-reading-tile', 30)
        listening_lesson_button = self.wait_for_element('by_id', 'lesson-category-listening-tile', 30)

        skill_list = {1: vocab_lesson_button, 2: grammar_lesson_button,
                      3: reading_lesson_button, 4: listening_lesson_button}
        skill_list.get(skill_item).click()

    def lesson_list(self):
        log.info('PREPARE lesson list..')
        self.let_me_sleep(6)   # wait for 30sec and get the list of lessons
        lesson_list = self.find_elements_and_wait('by_css_selector', '.cards-holder.cards-md', 3)
        log.info("TESTING FOR #{} lessons.".format(len(lesson_list)))
        return lesson_list

    def lesson_resource_selection(self):
        ''' decide which resource to play.
        1. check quiz/practice available
        2. check vocabulary available
        3. check video available
        4. check recommended lesson available'''
        lesson_title = self.find_element_and_wait('by_id', 'lesson-landing-title', 2).text

        log.info('OPENING lesson #{}'.format(lesson_title))
        log.info('CHECK available resources')

        # wait for 3sec
        self.let_me_sleep(3)

        # check resource availability
        quiz_button = self.find_elements_and_wait('by_id', 'lesson-landing-resource-assessment-tile', 0)
        vocab_button = self.find_elements_and_wait('by_id', 'lesson-landing-resource-vocabulary-tile', 0)
        recommendation_button = self.find_elements_and_wait('by_id', 'landing-start-button', 0)
        video_resource_button = self.find_elements_and_wait('by_id', 'lesson-landing-resource-resource-tile', 0)

        if video_resource_button:
            log.info('video content available')
            self.open_video()
            self.take_video()
            # log.info('video resource is available')
        else:
            log.info('NO video content')

        if quiz_button is not None:
            log.info('quiz resource is available')
            self.open_quiz()
            self.take_quiz()
        else:
            log.info('NO quiz resource')

        if vocab_button:
            log.info('vocab content is available')
            self.open_vocan_ui()
            self.take_vocab_ui()
        else:
            log.info('NO vocab content')

        if recommendation_button:
            log.info('recommended lesson is available')
        else:
            log.info('NO recommendation content')

    def lesson_selection(self):
        ''' select lesson from lesson list
            1. get the lesson list
            2. open lesson
            3. select resource based on the availability
            4. close the once all the resources are consumed
        '''
        for index, lesson in enumerate(self.lesson_list()):
            log.info("lesson #{}".format(index))
            lesson_id = 'lesson-list-lesson{}-tile'.format(index)

            self.wait_for_element_and_click('by_id', lesson_id, 30)
            self.let_me_sleep(5)

            # resource check
            self.lesson_resource_selection()

            # select available resource
            self.lesson_landing_back()

    ##############################################
    # TEST CASES GOES HERE
    #
    # 1. lesson selection
    # 2. open skill page and go back iterations
    # 3. grade 1 content consumption
    # 4. grade 2 content consumption
    # 5. grade 3 content consumption
    ##############################################
    @unittest.skip("start lesson selection")
    def test_101_start_lesson_selection(self):
        self.click_start_button()
        self.let_me_sleep(3)
        self.go_back()

    @unittest.skip("lesson selection in loop")
    def test_102_start_lesson_selection_loop(self):
        count = 0
        for counter in range(40):
            count = count + 1
            log.info('PROCESSING #{}'.format(count))
            self.click_start_button()
            self.let_me_sleep(2)
            self.go_back()

    ##############################
    # GRADE 1 CONTANT TESTCASES
    # CAN AUTOMATE BY LOOPING GRADE_SKILLS
    # INTENTIONALLY CREATED
    ##############################
    # @unittest.skip("grade1_VOCAB")
    def test_103_start_take_grade_1_content_VOCAB(self):
        self.app_informtion("grade_1_content_VOCAB")

        self.click_start_button()
        self.let_me_sleep(2)
        self.lesson_grade_selection(GRADE_ONE)
        self.lesson_grade_skill_selection(GRADE_SKILL_VOCAB)
        self.lesson_selection()

    # @unittest.skip("grade1_GRAMMAR")
    def test_104_start_take_grade_1_content_GRAMMAR(self):
        self.app_informtion("grade_1_content_GRAMMAR")

        # log.info("lesson test")
        self.click_start_button()
        self.let_me_sleep(2)
        self.lesson_grade_selection(GRADE_ONE)
        self.lesson_grade_skill_selection(GRADE_SKILL_GRAMMAR)
        self.lesson_selection()

    # @unittest.skip("grade1_READING")
    def test_105_start_take_grade_1_content_READING(self):
        self.app_informtion("grade_1_content_READING")

        self.click_start_button()
        self.let_me_sleep(2)
        self.lesson_grade_selection(GRADE_ONE)
        self.lesson_grade_skill_selection(GRADE_SKILL_READING)
        self.lesson_selection()

    # @unittest.skip("grade1_LISTENING")
    def test_106_start_take_grade_1_content_LISTENING(self):
        self.app_informtion("grade_1_content_LISTENING")

        self.click_start_button()
        self.let_me_sleep(2)
        self.lesson_grade_selection(GRADE_ONE)
        self.lesson_grade_skill_selection(GRADE_SKILL_LISTENING)
        self.lesson_selection()

    ##############################
    # GRADE 2 CONTANT TESTCASES
    # CAN AUTOMATE BY LOOPING GRADE_SKILLS
    # INTENTIONALLY CREATED
    ##############################
    # @unittest.skip("grade2_VOCAB")
    def test_107_start_take_grade_2_content_VOCAB(self):
        self.app_informtion("grade_2_content_VOCAB")

        self.click_start_button()
        self.let_me_sleep(2)
        self.lesson_grade_selection(GRADE_TWO)
        self.lesson_grade_skill_selection(GRADE_SKILL_VOCAB)
        self.lesson_selection()

    # @unittest.skip("grade2_GRAMMAR")
    def test_108_start_take_grade_2_content_GRAMMAR(self):
        self.app_informtion("grade_2_content_GRAMMAR")

        self.click_start_button()
        self.let_me_sleep(2)
        self.lesson_grade_selection(GRADE_TWO)
        self.lesson_grade_skill_selection(GRADE_SKILL_GRAMMAR)
        self.lesson_selection()

    # @unittest.skip("grade2_READING")
    def test_109_start_take_grade_2_content_READING(self):
        self.app_informtion("grade_2_content_READING")

        self.click_start_button()
        self.let_me_sleep(2)
        self.lesson_grade_selection(GRADE_TWO)
        self.lesson_grade_skill_selection(GRADE_SKILL_READING)
        self.lesson_selection()

    # @unittest.skip("grade2_LISTENING")
    def test_110_start_take_grade_2_content_LISTENING(self):
        self.app_informtion("grade_2_content_LISTENING")

        self.click_start_button()
        self.let_me_sleep(2)
        self.lesson_grade_selection(GRADE_TWO)
        self.lesson_grade_skill_selection(GRADE_SKILL_LISTENING)
        self.lesson_selection()

    ##############################
    # GRADE 3 CONTANT TESTCASES
    # CAN AUTOMATE BY LOOPING GRADE_SKILLS
    # INTENTIONALLY CREATED
    ##############################
    # @unittest.skip("grade3_VOCAB")
    def test_111_start_take_grade_3_content_VOCAB(self):
        self.app_informtion("grade_3_content_VOCAB")

        self.click_start_button()
        self.let_me_sleep(2)
        self.lesson_grade_selection(GRADE_THREE)
        self.lesson_grade_skill_selection(GRADE_SKILL_VOCAB)
        self.lesson_selection()

    # @unittest.skip("grade3_GRAMMAR")
    def test_112_start_take_grade_3_content_GRAMMAR(self):
        self.app_informtion("grade_3_content_GRAMMAR")

        self.click_start_button()
        self.let_me_sleep(2)
        self.lesson_grade_selection(GRADE_THREE)
        self.lesson_grade_skill_selection(GRADE_SKILL_GRAMMAR)
        self.lesson_selection()

    # @unittest.skip("grade3_READING")
    def test_113_start_take_grade_3_content_READING(self):
        self.app_informtion("grade_3_content_READING")

        self.click_start_button()
        self.let_me_sleep(2)
        self.lesson_grade_selection(GRADE_THREE)
        self.lesson_grade_skill_selection(GRADE_SKILL_READING)
        self.lesson_selection()

    # @unittest.skip("grade3_LISTENING")
    def test_114_start_take_grade_3_content_LISTENING(self):
        self.app_informtion("grade_3_content_LISTENING")

        self.click_start_button()
        self.let_me_sleep(2)
        self.lesson_grade_selection(GRADE_THREE)
        self.lesson_grade_skill_selection(GRADE_SKILL_LISTENING)
        self.lesson_selection()
