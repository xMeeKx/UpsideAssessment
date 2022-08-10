import os
import pytest
from appium import webdriver

EXECUTOR = 'http://127.0.0.1:4723/wd/hub'
ANDROID_APP_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'android_apps')

#protection from more than one apk in directory
apk_files = [f for f in os.listdir(ANDROID_APP_DIR) if f.endswith('.apk')]
assert len(apk_files) == 1, 'App directory can only contain one app file'
ANDROID_APP_PATH = os.path.join(ANDROID_APP_DIR, apk_files.pop(0))

@pytest.fixture
def app_driver():
    driver = webdriver.Remote(
        command_executor=EXECUTOR,
        desired_capabilities={
            "deviceName": "emulator-5554",
            "platformName": "Android",
            "appPackage": "com.upside.consumer.android.beta",
            "appWaitActivity": "com.upside.consumer.android.activities.MainActivity",
            "app": "C:/apkfiles/app-betabs-debug.apk",
            "autoGrantPermissions": "true"
        }
    )

    yield driver
    driver.quit()