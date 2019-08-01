from selenium import webdriver
import time
import unittest
from POMUltimateQA.Pages.loginPage import LoginPage

class TestLoginInvalidEmail(unittest.TestCase):

    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = self.webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")
        driver.implicitly_wait(10)
        yield
        driver.close()
        driver.quit()
        print("The test is completed")

    def test_03_login_invalid_email(test_setup):
        driver = test_setup.driver

        driver.get("https://courses.ultimateqa.com/users/sign_in")
        driver.implicitly_wait(10)

        login = LoginPage(driver)
        login.enter_username("testtest.com")  # invalid test data
        login.enter_password("_test")  # valid test data
        login.click_sign_in()

        time.sleep(2)

