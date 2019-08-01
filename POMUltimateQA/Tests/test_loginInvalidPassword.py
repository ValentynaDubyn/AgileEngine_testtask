from selenium import webdriver
import time
import unittest
import pytest
from POMUltimateQA.Pages.loginPage import LoginPage

class TestLoginInvPass(unittest.TestCase):
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = self.webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")
        driver.implicitly_wait(10)
        yield
        driver.close()
        driver.quit()
        print("The test is completed")


    def test_02_login_invalid_password(test_setup):
        driver = test_setup.driver

        driver.get("https://courses.ultimateqa.com/users/sign_in")
        driver.implicitly_wait(10)

        login = LoginPage(driver)
        login.enter_username("test@test.com") #valid test data
        login.enter_password("test_test") #invalid password
        login.click_sign_in()
        login.incorrect_credentials_message()
        time.sleep(2)

