import os


def get_desired_capabilities(app):
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '6.0.1',
        'deviceName': 'DeadByCode',
        'browserName': '',
        'autoWebview': True,
        'newCommandTimeout': 240,
        'noReset': True,
        'app': os.path.abspath('/Users/Ashish/Documents/workspace/zaya/projects/apks/'+app),
    }

    return desired_caps
