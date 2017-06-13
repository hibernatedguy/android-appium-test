import os

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

def get_desired_capabilities(app):
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '5.0',
        'deviceName': 'Android Emulator',
        'app': PATH('../../apps/' + app),
        'newCommandTimeout': 240
    }

    return desired_caps
