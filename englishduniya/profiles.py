import unittest

from config import log
from config import EnglishDuniyaSetup


class AppStartupChecks(EnglishDuniyaSetup):
    ##########################################
    # STARTUP CHECKS
    # 1. profile creation
    # 2. grade selection
    # 3. phone number checks
    # 4. take diagnosis
    # 5. select school
    # 6. select
    ##########################################

    @unittest.skip("create profile")
    def test_lesson_000_start_create_profile(self):
        log.info('create profile test')
