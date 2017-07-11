import os
import subprocess
from random import randint


def get_desired_capabilities(app):
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '5.1.1',
        'deviceName': 'Galaxy J2',
        'browserName': '',
        'autoWebview': True,
        'autoGrantPermissions': True,
        'resetKeyboard': True,
        'noReset': True,
        'newCommandTimeout': 240,
        'app': os.path.abspath('/Volumes/Monk/workspace/zaya/apk/' + app),
    }

    return desired_caps


##################
# CONSTANTS
##################
CONTEXT_NAME = "WEBVIEW"
SLEEP_LONG = 20
SLEEP_SHORT = 10
SLEEP_QUICK = 3
RANDOM_START = 1

CRED = '\033[91m'
CEND = '\033[0m'


def check_device_availability():
    command = subprocess.getoutput("adb devices")
    if len(command.split()) == 4 or "offline" in command:
        print (CRED + "Oops! There is no AndroidDevice. available for testing.\nPlease connect AndroidDevice and try again." + CEND)
        exit()


def random_numbers(RANDOM_END):
    return randint(RANDOM_START, RANDOM_END)
