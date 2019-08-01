from selenium import webdriver
import time
import unittest
import pytest
from POMUltimateQA.Pages.loginPage import LoginPage

class TestLoginValid(unittest.TestCase):

    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = self.webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")
        driver.implicitly_wait(10)
        yield
        driver.close()
        driver.quit()
        print("The test is completed")

    def test_01_login_valid(test_setup):
        driver.get("https://courses.ultimateqa.com/users/sign_in")
        driver.implicitly_wait(10)

        login = LoginPage(driver)
        login.enter_username("test@test.com") #valid test data
        login.enter_password("_test") #valid test data
        login.click_sign_in()

        # result homepage
        time.sleep(2)


